# app/config.py

MODEL_NAMES = {
    "event_analysis": "facebook/bart-large-mnli",
    "text_generator": "gpt2"
}

FACT_CHECK_API = "https://en.wikipedia.org/api/rest_v1/page/summary"

HISTORY_FILE = "history.json"
FEEDBACK_FILE = "feedback.json"

BASE_URL = "http://127.0.0.1:8000"