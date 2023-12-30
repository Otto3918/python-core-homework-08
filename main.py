''' The function gets a list of dictionaries. The dictionary contains:
       - employee name (key)
       - date of birth (value)
    The function returns a dictionary with a list of employees, days
    whose births fall within the next 7 days, including
    the day this script was launched. A dictionary with the following structure:
       - day of the week (key)
       - list of employees who have a birthday
         on this day of the week.
         If your birthday is on Saturday or Sunday, then
         we move it to Monday '''

from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    ''' Let's create a dictionary (dict_search_day_week), where:
        "key" is a tuple (day, month) from a given date range
        "value" is the day of the week '''
    dict_search_day_week = dict()

    ''' And a dictionary (dict_out) where:
        "key" is the name of the day of the week.
        "value" - a currently empty list for recording employees who have a birthday
                     falls on this day of the week. '''
    dict_out = dict()

    date_first = date.today()                    # Interval start date
    date_last = date_first + timedelta(days=6)   # Interval end date
    while date_first <= date_last:
        key = (date_first.day, date_first.month)
        value = date_first.strftime('%A')

        dict_search_day_week[key] = value
        date_first = date_first + timedelta(days=1)
        dict_out[value] = []

    for person in users:
        name_person = person['name']
        birthday_person = person['birthday']  # From the employee's date of birth
        num_day = birthday_person.day         # create a tuple as a search key
        key_search = (num_day, birthday_person.month)
        name_day_week = dict_search_day_week.get(key_search)
        if name_day_week is not None:         # birthday and month of birth are available in the required interval
            ''' Sunday (num_day = 6) will be moved to Monday that is, 1 day in advance
                Saturday (num_day = 5) will be moved to Monday that is, 2 day in advance  '''
            plus_day = 0
            if name_day_week == 'Sunday':
                plus_day = 1
            elif name_day_week == 'Saturday':
                plus_day = 2

            if plus_day != 0:
                ''' Let's check that the days moved to Monday
                    did not leave the specified interval '''
                date_first = birthday_person + timedelta(days=plus_day)
                name_day_week = 'Monday' if date_first <= date_last else ''

            if name_day_week:
                dict_out[name_day_week].append(name_person)

    ''' Let's remove days of the week where there are no birthdays '''
    users = {key: value for key, value in dict_out.items() if len(value) > 0}

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 25).date()},
        {"name": "Jan Koum2", "birthday": datetime(1976, 12, 29).date()},
        {"name": "Jan Koum3", "birthday": datetime(1976, 12, 31).date()},
        {"name": "Jan Koum4", "birthday": datetime(1976, 1, 2).date()},
        {"name": "Jan Koum5", "birthday": datetime(1976, 1, 3).date()}
    ]

    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
