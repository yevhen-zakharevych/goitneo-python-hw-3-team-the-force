from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users_list):
    birthdays_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users_list:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        day = birthday_this_year.weekday()

        if day == 5:
            birthday_this_year = birthday_this_year + timedelta(days=2)
        elif day == 6:
            birthday_this_year = birthday_this_year + timedelta(days=1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.strftime('%A')
            birthdays_dict[weekday].append(name)

    result = ""

    for day, names in birthdays_dict.items():
        result += f"{day}: {', '.join(names)}\n"

    if result == "":
        return None

    return result
