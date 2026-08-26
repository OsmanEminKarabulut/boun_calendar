from datetime import datetime

class EventModel:
    def __init__(self, id, adi, start_date, end_date, is_all_day, kategori_adi, link, kulup):
        self.id = id
        self.adi = adi
        self.start_date = start_date
        self.end_date = end_date
        self.is_all_day = is_all_day
        self.kategori_adi = kategori_adi
        self.link = link
        self.kulup = kulup


def jsonToEventModel(json):
    return EventModel(
        json["id"],
        json["adi"],
        datetime.strptime(json["start_date"], "%Y-%m-%d %H:%M:%S"),
        datetime.strptime(json["end_date"], "%Y-%m-%d %H:%M:%S"),
        not json["saat"],
        json["kategoriadi"],
        json["link"],
        json["kulup"],
    )