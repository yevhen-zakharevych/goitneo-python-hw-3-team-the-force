from field import Field
from exceptions import PhoneLengthException


class Phone(Field):
    def __init__(self, value):
        if not len(value) == 10:
            raise PhoneLengthException
        super().__init__(value)
