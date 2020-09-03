from datetime import date, time, datetime, timedelta
import os

#  Python datetime or date object
#  Unix epoch time   (#seconds since 1/1/70)
#  Time tuple  (9 values -- Y M D H M S JDATE DSFLAG ISLEAP

today = date.today()
print(today)
print(today.year, today.day, today.month)

james_bd = date(2014, 8, 1)
print(james_bd)

elapsed = today - james_bd
print(elapsed)

james_age = elapsed.days / 365

print(f"james is {james_age:.2f} years old")

file_path = os.path.join("DATA", "alice.txt")

raw_timestamp = os.path.getmtime(file_path)  # .getatime()  last time read or accessed
print(raw_timestamp)

timestamp = datetime.fromtimestamp(raw_timestamp)
print(timestamp)

from dateutil import parser
date_strings = [  # <1>
    'April 1, 2015',
    '4/1/2015',
    'Apr 1, 2015',
    'Apr 1 2015',
    '04/01/2015',
    '1 Apr 2015',
    'April 1st, 2015',
    'April 1, 2015 8:09',
    '4/1/2015 8:09 PM',
    'Apr 1, 2015 5 AM',
    'Apricot 4, 341',
    'Apr 31, 2020 22:55'
]

for date_string in date_strings:
    try:
        dt = parser.parse(date_string)  # <2>
        print(f"{date_string:25s} {dt}")
    except ValueError as err:
        print("Can't parse", date_string)



