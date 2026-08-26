import src.fetcher as fetcher
import src.cal_generator as cal_generator

if fetcher.is_cal_changed():
    events = fetcher.get_events()
    cal_generator.generate_cal(events)
