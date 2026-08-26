import requests
from src.event_model import jsonToEventModel
from datetime import datetime, timedelta
import os
import hashlib

#paths
HASH_OUTPUT_DIR = "dist"
CALENDAR_OUTPUT_DIR ="dist/calendars"
HASH_FILE = os.path.join(HASH_OUTPUT_DIR, "last_hash.txt")
ICS_FILE = os.path.join(CALENDAR_OUTPUT_DIR, "boun_calendar.ics")

#Create files if they dont exist
os.makedirs(HASH_OUTPUT_DIR, exist_ok=True)
os.makedirs(CALENDAR_OUTPUT_DIR, exist_ok=True)

#Calculate SHA256 of the raw_text(the api response) to detect changes
def calculate_hash(raw_text):
    return hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

#Save SHA256 of the current_text for later comparison
def save_hash(raw_text):
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        f.write(raw_text)


#Return whether the calendar has changed
def is_cal_changed():
    if not os.path.exists(HASH_FILE) or not os.path.exists(ICS_FILE):
        save_hash(current_hash)
        return True

    with open(HASH_FILE, "r", encoding="utf-8") as f:
        old_hash = f.read().strip()

    if old_hash != current_hash:
        save_hash(current_hash)
        return True
    else:
        return False


response = requests.get("https://akademiktakvim.bogazici.edu.tr/tr/json?type=4")


raw_json = response.json()
raw_events = [jsonToEventModel(event) for event in raw_json]

current_hash = calculate_hash(str(response.text))

#Return events that end within the last 15 days or later
def get_events():
    events = []
    for raw_event in raw_events:
        if datetime.now() - timedelta(15) <= raw_event.end_date:
            events.append(raw_event)
    return events
        