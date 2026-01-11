import json
from app.core.config import DATA_FILE
from pathlib import Path
from typing import Optional, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_FILE = DATA_DIR / "translations.json"
def save_translation(data: Dict) -> None:
    """
    Save translation data.
    - Ensures only ONE file exists
    - Overrides old file safely
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Remove old file if exists
    if DATA_FILE.exists():
        DATA_FILE.unlink()

    # Write new file
    DATA_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

def read_translation() -> Optional[Dict[str, Any]]:
    """
    Read translation data safely.
    Returns None if:
    - File does not exist
    - File is empty
    """
    if not DATA_FILE.exists():
        return None

    content = DATA_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return None

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None

def delete_translations():
    if DATA_FILE.exists():
        DATA_FILE.unlink()
