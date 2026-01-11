from pydantic import RootModel,BaseModel
from typing import Dict, Any

class TranslatedPayload(BaseModel):
    project_name: str
    languages: Dict[str, str]
    data: Dict[str, Any]
