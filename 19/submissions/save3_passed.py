from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime) -> object:
        self.name = name
        self.expires = expires
    def __get__(self):
        return self.expires < NOW
    expired = property(fget=__get__)