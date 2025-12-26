from datetime import datetime
from pathlib import Path
import os

LOG_FILE = Path("/opt/zaios/logs/audit.log")

def log(action: str, target: str = "", details: str = ""):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    user = os.getenv("USER", "unknown")
    timestamp = datetime.utcnow().isoformat()

    line = f"{timestamp} | user={user} | action={action} | target={target} | {details}\n"
    LOG_FILE.write_text(LOG_FILE.read_text() + line if LOG_FILE.exists() else line)
