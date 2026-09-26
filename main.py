import src.fetcher as fetcher
import src.cal_generator as cal_generator


#Runs only when the calendar has changed
if fetcher.is_tr_cal_changed():
    tr_events = fetcher.get_tr_events()
    cal_generator.generate_tr_cal(tr_events)

if fetcher.is_en_cal_changed():
    en_events = fetcher.get_en_events()
    cal_generator.generate_en_cal(en_events)
