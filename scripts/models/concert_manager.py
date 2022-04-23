import datetime

class ConcertManager():
    def __init__(self):
        self.concerts = []

    def sorted_concerts(self):
        return sorted(self.concerts, key=lambda x: x.date_obj)

    def get_next_concert(self):
        for concert in self.sorted_concerts():
            if concert.date_obj > datetime.datetime.now():
                return concert

    def get_future_concerts(self):
        return [concert for concert in self.sorted_concerts()
                    if concert.date_obj > datetime.datetime.now() and concert != self.get_next_concert()]

    def get_past_concerts(self):
        return [concert for concert in self.sorted_concerts()
                    if concert.date_obj < datetime.datetime.now()][::-1]
