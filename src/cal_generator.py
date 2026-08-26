from icalendar import Calendar, Event
from datetime import datetime
import os

#paths
OUTPUT_DIR = "dist/calendars"
ICS_FILE = os.path.join(OUTPUT_DIR, "boun_calendar.ics")

def generate_cal(events):

    #Calendar configuration
    cal = Calendar()
    cal.add('prodid', '-//Bogazici Calendar//bogazici.edu.tr//')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'Boğaziçi Üniversitesi Akademik Takvim')
    cal.add('x-wr-timezone', 'Europe/Istanbul')


    #Create an Event object for each item and add it to the calendar
    for e in events:
        event = Event()

        #This uid is important. It prevents duplicating the events in the calendar.
        event.add('uid', f"boun-{e.id}@bogazici.edu.tr")  
        event.add('summary', e.adi)                       
        event.add('dtstamp', datetime.now())     

        if e.is_all_day:
            event.add("dtstart", e.start_date.date())
            event.add("dtend", e.end_date.date())

        else:
            event.add('dtstart', e.start_date)
            event.add('dtend', e.end_date)

        aciklama_metni = f"Kategori: {e.kategori_adi}\n"
        if e.kulup:
            aciklama_metni += f"Kulüp: {e.kulup}\n"
        if e.link:
            aciklama_metni += f"Detaylar: {e.link}"
            event.add('url', e.link)

        cal.add_component(event)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ICS_FILE, "wb") as f:
        f.write(cal.to_ical())