from collections import UserDict
import pickle
from record import Record
from get_users_per_week import get_birthdays_per_week


class AddressBook(UserDict):
    def __str__(self):
        res = ""

        for name, record in self.data.items():
            res += f"{str(record)}\n"

        if res == "":
            return "Address book is empty."

        return res

    def add_record(self, name, phones):
        if len(phones) == 0:
            raise ValueError

        record = Record(name)

        for phone in phones:
            record.add_phone(phone)

        self.data[record.name.value] = record

    def add_birthday(self, name, birthday):
        record = self.find(name)
        record.add_birthday(birthday)

    def show_birthday(self, name):
        record = self.find(name)

        return record.show_birthday()

    def birthdays(self):
        users = []

        for name, record in self.data.items():
            if record.birthday.value:
                user = {
                    "name": record.name.value,
                    "birthday": record.birthday.value
                }

                users.append(user)

        return get_birthdays_per_week(users)

    def edit_record(self, name, old_phone, new_phone):
        record = self.find(name)
        record.edit_phone(old_phone, new_phone)

    def find(self, name):
        return self.data[name]

    def find_phone(self, name, phone):
        record = self.find(name)

        return record.find_phone(phone)

    def delete(self, name):
        del self.data[name]

    def save_to_file(self, filename):
        with open(filename, "wb") as fh:
            pickle.dump(self, fh)

    def read_from_file(self, filename):
        with open(filename, "rb") as fh:
            address_book = pickle.load(fh)

            if address_book:
                self.data = address_book

