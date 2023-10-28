from input_error import input_error
from address_book import AddressBook
from exceptions import BirthdayArgsException

ADDRESS_BOOK_FILE_NAME = 'address_book.bin'


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, book):
    name, *phones = args

    book.add_record(name, phones)

    return "Contact has been added."


@input_error
def add_birthday(args, book):
    try:
        name, birthday = args
    except ValueError:
        raise BirthdayArgsException

    book.add_birthday(name, birthday)

    return "Birthday has been added."


@input_error
def show_birthday(args, book):
    name, = args

    return book.show_birthday(name)


def birthdays(book):
    return book.birthdays()


@input_error
def get_contact(args, book):
    name = args[0]

    return str(book.find(name))


@input_error
def find_phone(args, book):
    name, phone = args

    return book.find_phone(name, phone)


def get_all_contacts(book):
    return str(book)


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args

    book.edit_record(name, old_phone, new_phone)

    return "Contact changed."


@input_error
def delete_contact(args, book):
    name, = args

    book.delete(name)

    return "Contact has been deleted."


def save_to_file(book):
    book.save_to_file(ADDRESS_BOOK_FILE_NAME)

    return "Address book has been saved."


@input_error
def read_from_file(book):
    book.read_from_file(ADDRESS_BOOK_FILE_NAME)

    return "Address book has been loaded."


def main():
    print("Welcome to the assistant bot!")
    book = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_contact(args, book))
        elif command == "find":
            print(find_phone(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "delete":
            print(delete_contact(args, book))
        elif command == "save":
            print(save_to_file(book))
        elif command == "load":
            print(read_from_file(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
