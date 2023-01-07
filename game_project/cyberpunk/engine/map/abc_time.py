from datetime import datetime


class ITime:
    _datetime: datetime

    @property
    def time(self):
        return self.datetime.time()

    @property
    def date(self):
        return self.datetime.date()

    def get_datetime_readable(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S')
