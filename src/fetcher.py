import requests
from src.event_model import jsonToEventModel
from datetime import datetime, timedelta
import os
import hashlib

#paths
HASH_OUTPUT_DIR = "dist"
CALENDAR_OUTPUT_DIR ="dist/calendars"
TR_HASH_FILE = os.path.join(HASH_OUTPUT_DIR, "last_tr_hash.txt")
EN_HASH_FILE = os.path.join(HASH_OUTPUT_DIR, "last_en_hash.txt")
ICS_FILE = os.path.join(CALENDAR_OUTPUT_DIR, "boun_calendar.ics")
TR_YADYOK_ICS_FILE = os.path.join(CALENDAR_OUTPUT_DIR, "boun_tr_yadyok_calendar.ics")
EN_YADYOK_ICS_FILE = os.path.join(CALENDAR_OUTPUT_DIR, "boun_en_yadyok_calendar.ics")
EN_ICS_FILE = os.path.join(CALENDAR_OUTPUT_DIR, "boun_en_calendar.ics")

#Create files if they dont exist
os.makedirs(HASH_OUTPUT_DIR, exist_ok=True)
os.makedirs(CALENDAR_OUTPUT_DIR, exist_ok=True)

#Calculate SHA256 of the raw_text(the api response_tr) to detect changes
def calculate_hash(raw_text):
    return hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

#Save SHA256 of the current_text for later comparison
def save_tr_hash(raw_text):
    with open(TR_HASH_FILE, "w", encoding="utf-8") as f:
        f.write(raw_text)

def save_en_hash(raw_text):
    with open(EN_HASH_FILE, "w", encoding="utf-8") as f:
        f.write(raw_text)

#Return whether the calendar has changed
def is_tr_cal_changed():
    if not os.path.exists(TR_HASH_FILE) or not os.path.exists(ICS_FILE) or not os.path.exists(TR_YADYOK_ICS_FILE):
        save_tr_hash(current_tr_hash)
        return True

    with open(TR_HASH_FILE, "r", encoding="utf-8") as f:
        old_hash = f.read().strip()

    if old_hash != current_tr_hash:
        save_tr_hash(current_tr_hash)
        return True
    else:
        return False

def is_en_cal_changed():
    if not os.path.exists(EN_HASH_FILE) or not os.path.exists(EN_ICS_FILE) or not os.path.exists(EN_YADYOK_ICS_FILE):
        save_en_hash(current_en_hash)
        return True

    with open(EN_HASH_FILE, "r", encoding="utf-8") as f:
        old_hash = f.read().strip()

    if old_hash != current_en_hash:
        save_en_hash(current_en_hash)
        return True
    else:
        return False

response_tr = requests.get("https://akademiktakvim.bogazici.edu.tr/tr/json?type=4", timeout=10)
response_en = requests.get("https://akademiktakvim.bogazici.edu.tr/en/json?type=4", timeout=10)


raw_tr_json = response_tr.json()
raw_tr_events = [jsonToEventModel(event) for event in raw_tr_json]

current_tr_hash = calculate_hash(str(response_tr.text))


raw_en_json = response_en.json()
raw_en_events = [jsonToEventModel(event) for event in raw_en_json]

current_en_hash = calculate_hash(str(response_en.text))

#Return events that end within the last 60 days or later
def get_tr_events():
    events = []
    for raw_event in raw_tr_events:
        if raw_event.end_date >= datetime.now() - timedelta(60):
            events.append(raw_event)
    return events

def get_en_events():
    events = []
    for raw_event in raw_en_events:
        if raw_event.end_date >= datetime.now() - timedelta(60):
            events.append(raw_event)
    return events  

def get_yadyok_events(raw_events):
    events = []
    for raw_event in raw_events:
        if raw_event.kat_id == "25":
            events.append(raw_event)
    return events  
