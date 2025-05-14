# Here we just set date, time, year.
# Using python in-build library "datetime".
import datetime

print(datetime.datetime.now())
print(datetime.date.today())

now = datetime.datetime.now()
print(now.strftime("%d/%m/%y"))

# By this way we can set a new date or past or future date.
x = datetime.datetime(2022, 8, 5)
print(x)

# By this way we can check difference.
a = datetime.datetime(2021, 2, 12)
b = datetime.datetime(2021, 2, 10)

difference = a-b
print(difference)



