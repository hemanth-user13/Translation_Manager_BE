from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timedelta
from core.config import DATA_FILE

def cleanup_translation():
    if not DATA_FILE.exists():
        return 
    modefied_time=datetime.utcfromtimestamp(DATA_FILE.stat().st_mtime)
    if datetime.utcnow()-modefied_time>timedelta(hours=1):
        DATA_FILE.unlink()

def start_scheduler():
    scheduler=BackgroundScheduler()
    scheduler.add_job(cleanup_translation,"interval",hours=1)
    scheduler.start()