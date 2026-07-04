import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("history.json")


def log_conversation(data):
    data["timestamp"] = datetime.now().isoformat()

    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = []
    else:
        history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    return []