from day_class import Day
import csv


def make_list_of_days():
    """Places creation of an array of days as a function so a new array can be created if need be"""

    #  iterable dictionary array for creating an object for each day
    calendar_year = {
        'January': 31,
        'February': 29,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }

    #  standard list array for storage because no insertion has to occur
    all_days = []

    #  initialize a class object for every day in the year, stored in the list all_days
    for month, days_in_month in calendar_year:
        for day in range(1, days_in_month + 1):
            all_days.append(Day(month, day))

    return all_days


def is_leap_year(year):
    """Returns whether a given year was a leap year"""

    #  "There is a leap year every year whose number is perfectly divisible by four -
    #  except for years which are both divisible by 100 and not divisible by 400."
    #  quoted from Western Washington University
    #  https://www.wwu.edu/astro101/a101_leapyear.shtml

    if year % 100 == 0:  # if year is a century year, an additional check is required (see above)
        if year % 400 == 0:  # centuries must also be divisible by 400
            return True
        return False
    if year % 4 == 0:
        return True
    return False


def change_week_day(current_day):
    """Changes current_day to the next day n the 7-day cycle"""

    if current_day == 'Sunday':
        return 'Monday'
    elif current_day == 'Monday':
        return 'Tuesday'
    elif current_day == 'Tuesday':
        return 'Wednesday'
    elif current_day == 'Wednesday':
        return 'Thursday'
    elif current_day == 'Thursday':
        return 'Friday'
    elif current_day == 'Friday':
        return 'Saturday'
    elif current_day == 'Saturday':
        return 'Sunday'
    else:
        raise ValueError('No valid day was entered')


def main():
    """Starting from 1800, finds the distribution of weekdays for every calendar day until Dec 31, 2021"""

    #  Jan 1st, 1800 was a Wednesday
    current_week_day = 'Wednesday'
    current_year = 1800

    while current_year != 2022:
        for day in days_of_the_year:
            if day.day() == 'February-29' and is_leap_year(current_year):  # special case
                day.add_instance(current_week_day)
                continue
            elif day.day() == 'February-29':  # skip Feb 29 if not a leap year
                continue

            day.add_instance(current_week_day)
            current_week_day = change_week_day(current_week_day)

        current_year += 1


#  global variable to avoid unnecessary argument passing
days_of_the_year = make_list_of_days()
if __name__ == '__main__':
    main()
