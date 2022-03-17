class Day:
    _DAYS_OF_THE_WEEK = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

    def __init__(self, month, day):
        self._month = month
        self._day = day

        self._sunday = 0
        self._monday = 0
        self._tuesday = 0
        self._wednesday = 0
        self._thursday = 0
        self._friday = 0
        self._saturday = 0

        self._total = 0

    def __str__(self):
        """Returns a printable string which gives percentages of each weekday for the given calendar day"""
        return f'{self._month} {self._day} has been:\n' \
               f'Sunday {self._sunday / self._total}% of the time,\n' \
               f'Monday {self._monday / self._total}% of the time,\n' \
               f'Tuesday {self._tuesday / self._total}% of the time,\n' \
               f'Wednesday {self._wednesday / self._total}% of the time,\n' \
               f'Thursday {self._thursday / self._total}% of the time,\n' \
               f'Friday {self._friday / self._total}% of the time, and\n' \
               f'Saturday {self._saturday / self._total}% of the time.'

    def add_instance(self, day_of_the_week):
        """Adds 1 to the day of the week that this calendar day fell on, also increments the total"""

        #  make day_of_the_week all lowercase to remove case-sensitivity
        if day_of_the_week.lower() == 'sunday':
            self._sunday += 1
        elif day_of_the_week.lower() == 'monday':
            self._monday += 1
        elif day_of_the_week.lower() == 'tuesday':
            self._tuesday += 1
        elif day_of_the_week.lower() == 'wednesday':
            self._wednesday += 1
        elif day_of_the_week.lower() == 'thursday':
            self._thursday += 1
        elif day_of_the_week.lower() == 'friday':
            self._friday += 1
        elif day_of_the_week.lower() == 'saturday':
            self._saturday += 1
        else:
            #  allow for exception handling
            raise ValueError('No valid days were entered')

        self._total += 1

    def day(self):
        return f'{self._month}-{self._day}'

    def percent_sunday(self):
        return float(f'{self._sunday / self._total:.2f}')

    def percent_monday(self):
        return float(f'{self._monday / self._total:.2f}')

    def percent_tuesday(self):
        return float(f'{self._tuesday / self._total:.2f}')

    def percent_wednesday(self):
        return float(f'{self._wednesday / self._total:.2f}')

    def percent_thursday(self):
        return float(f'{self._thursday / self._total:.2f}')

    def percent_friday(self):
        return float(f'{self._friday / self._total:.2f}')

    def percent_saturday(self):
        return float(f'{self._saturday / self._total:.2f}')
