from datetime import datetime
from field import Field
from exceptions import BirthdayException


class Birthday(Field):
    def __init__(self, value):
        if not value:
            super().__init__(value)
            return

        try:
            d, m, y = value.split(".")
            birthday = datetime(year=int(y), month=int(m), day=int(d))
            super().__init__(birthday)

        except (ValueError, TypeError):
            raise BirthdayException

    def __str__(self):
        if not self.value:
            return "Birthday hasn't been added."
        return datetime.strftime(self.value, "%-d %b %Y")
