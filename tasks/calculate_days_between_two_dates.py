"""Python: Calculate number of days between two dates"""

from datetime import date

first_date = date(2019, 9, 16)
last_date = date(2021, 8, 27)
delta = last_date - first_date
print(delta.days)
