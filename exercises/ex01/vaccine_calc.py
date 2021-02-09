"""A vaccination calculator."""

__author__ = "730407523"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
initial_people: int = round(int(input("Doses administered: ")) / 2)
daily_people: int = round(int(input("Doses per day: ")) / 2)
target: int = int(input("Target percent vaccinated: "))

target_people: int = round(population * (target / 100))

# to-do: condense above to simple instead of storing extra values

people_delta: int = target_people - initial_people

# setup time objs

today: datetime = datetime.today()
time: int = round(people_delta / daily_people)
time_elapsed: timedelta = timedelta(round(people_delta / daily_people))

print(time_elapsed)

triumph_day: datetime = today + time_elapsed
print(f'We will reach {target}% vaccination in {time_elapsed.days} days, which falls on {(today + time_elapsed).strftime("%B %d, %Y")}.')