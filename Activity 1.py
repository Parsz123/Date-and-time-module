from datetime import date, time, datetime

now = datetime.now()
day = date.today()

print("Today is", day)
print("The current time is", now)
print("The components are", day.year, day.month, day.day)