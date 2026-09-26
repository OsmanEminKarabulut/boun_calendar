from icalendar import Calendar, Event
from datetime import datetime, timedelta
import os

#paths
OUTPUT_DIR = "dist/calendars"
TR_ICS_FILE = os.path.join(OUTPUT_DIR, "boun_calendar.ics")
EN_ICS_FILE = os.path.join(OUTPUT_DIR, "boun_en_calendar.ics")

TR_YADYOK_ICS_FILE = os.path.join(OUTPUT_DIR, "boun_tr_yadyok_calendar.ics")
EN_YADYOK_ICS_FILE = os.path.join(OUTPUT_DIR, "boun_en_yadyok_calendar.ics")

def generate_tr_cal(events):

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
            event.add("dtend", e.end_date.date()  + timedelta(days=1))

        else:
            event.add('dtstart', e.start_date)
            event.add('dtend', e.end_date)

        aciklama_metni = f"Kategori: {e.kategori_adi}\n"
        

        if e.kulup:
            aciklama_metni += f"Kulüp: {e.kulup}\n"
        if e.link:
            aciklama_metni += f"Detaylar: {e.link}"
            event.add('url', e.link)
        event.add("description", aciklama_metni)
        cal.add_component(event)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(TR_ICS_FILE, "wb") as f:
        f.write(cal.to_ical())


def generate_tr_yadyok_cal(events):

    #Calendar configuration
    cal = Calendar()
    cal.add('prodid', '-//Bogazici Calendar//bogazici.edu.tr//')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'Boğaziçi Üniversitesi YADYOK Akademik Takvimi')
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
            event.add("dtend", e.end_date.date()  + timedelta(days=1))

        else:
            event.add('dtstart', e.start_date)
            event.add('dtend', e.end_date)

        aciklama_metni = f"Kategori: {e.kategori_adi}\n"
        

        if e.kulup:
            aciklama_metni += f"Kulüp: {e.kulup}\n"
        if e.link:
            aciklama_metni += f"Detaylar: {e.link}"
            event.add('url', e.link)
        event.add("description", aciklama_metni)
        cal.add_component(event)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(TR_YADYOK_ICS_FILE, "wb") as f:
        f.write(cal.to_ical())





def generate_en_cal(events):

    #Calendar configuration
    cal = Calendar()
    cal.add('prodid', '-//Bogazici Calendar//bogazici.edu.tr//')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'Boğaziçi University Academic Calendar')
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
            event.add("dtend", e.end_date.date()  + timedelta(days=1))

        else:
            event.add('dtstart', e.start_date)
            event.add('dtend', e.end_date)

        aciklama_metni = f"Category: {e.kategori_adi}\n"
        

        if e.kulup:
            aciklama_metni += f"Club: {e.kulup}\n"
        if e.link:
            aciklama_metni += f"Details: {e.link}"
            event.add('url', e.link)
        event.add("description", aciklama_metni)
        cal.add_component(event)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(EN_ICS_FILE, "wb") as f:
        f.write(cal.to_ical())


def generate_en_yadyok_cal(events):

    #Calendar configuration
    cal = Calendar()
    cal.add('prodid', '-//Bogazici Calendar//bogazici.edu.tr//')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', 'Boğaziçi University SFL Academic Calendar')
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
            event.add("dtend", e.end_date.date()  + timedelta(days=1))

        else:
            event.add('dtstart', e.start_date)
            event.add('dtend', e.end_date)

        aciklama_metni = f"Category: {e.kategori_adi}\n"
        

        if e.kulup:
            aciklama_metni += f"Club: {e.kulup}\n"
        if e.link:
            aciklama_metni += f"Details: {e.link}"
            event.add('url', e.link)
        event.add("description", aciklama_metni)
        cal.add_component(event)

    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(EN_YADYOK_ICS_FILE, "wb") as f:
        f.write(cal.to_ical())