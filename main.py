import src.fetcher as fetcher
import src.cal_generator as cal_generator


#Runs only when the calendar has changed
if fetcher.is_cal_changed():
    events = fetcher.get_events()
    cal_generator.generate_cal(events)
