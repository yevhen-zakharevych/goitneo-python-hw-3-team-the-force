from exceptions import BirthdayException,BirthdayArgsException, PhoneException, PhoneLengthException


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact does not exist."
        except PhoneLengthException:
            return "Phone length should be 10."
        except PhoneException:
            return "Phone does not exist."
        except BirthdayException:
            return "Birthday should be format 'DD.MM.YYYY'"
        except BirthdayArgsException:
            return "Give me name and birthday please."
        except FileNotFoundError:
            return "No address book file."

    return inner
