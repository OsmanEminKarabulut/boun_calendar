# Boğaziçi Academic Calendar Sync

Automated iCalendar (`.ics`) feed for Boğaziçi University's official academic calendar.

[![Update Academic Calendar](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml/badge.svg)](https://github.com/OsmanEminKarabulut/boun_calendar/actions/workflows/update_calendar.yml)

---

## Subscription URL

Copy the URL below to subscribe in your calendar application (Google Calendar, Apple Calendar, Outlook):

```text
https://raw.githubusercontent.com/OsmanEminKarabulut/boun_calendar/main/dist/calendars/boun_calendar.ics
```

---

## How to Subscribe

- **Google Calendar:** Open [Google Calendar](https://calendar.google.com) > Click **+** next to _Other calendars_ > Select **From URL** > Paste the URL.
- **Apple Calendar (macOS / iOS):** Open Calendar > Select _File_ > _New Calendar Subscription..._ > Paste the URL.
- **Outlook:** Open Calendar > _Add calendar_ > _Subscribe from web_ > Paste the URL.

---

## Features

- **Daily Auto-Sync:** Automated via GitHub Actions to track official calendar updates daily.
- **All-Day & Timed Support:** Properly preserves whole-day events and timed events in `Europe/Istanbul` timezone.
- **No Duplicates:** Uses persistent `UID`s compliant with RFC 5545 for clean in-place updates.

---

## Local Setup

```bash
git clone https://github.com/OsmanEminKarabulut/boun_calendar.git
cd boun_calendar

python -m venv venv
# Windows: venv\Scripts\activate | Unix: source venv/bin/activate
pip install -r requirements.txt

python main.py
```
