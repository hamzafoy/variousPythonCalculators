import datetime
import time
start_date = datetime.date(year=2022, month=1, day=1)
current_date = datetime.date.today()

print(start_date)
print(current_date)
print(current_date.strftime('%A %d %B %Y'))
print("The first day of the year is {:%A %d %B %Y}".format(start_date))

# This manner is more powerful and not as affected by underlying modules/frameworks

print("{date:%A} {date.day} {date:%B} {date.year}".format(date=current_date))

lapse_in_days = current_date - start_date
print(lapse_in_days.days)

#Playing with time
current_time = time.localtime()
print(time.strftime("%H:%M:%S", current_time))

#Be aware that running the script in two instances of time will result in a different value
#stored when calling for current time & date.

#Playing with Timezones
gulftime = datetime.timezone(datetime.timedelta(hours=4), "GST")
centraltime = datetime.timezone(datetime.timedelta(hours=-5), "CST")
departure = datetime.datetime(year=2023, month=6, day=1, hour=9, minute=20, tzinfo=centraltime)
arrival = datetime.datetime(year=2023, month=6, day=2, hour=7, minute=55, tzinfo=gulftime)
timelapsed = arrival - departure
print(timelapsed.seconds)
print("The flight from Chicago to Abu Dhabi will take " + str(round(timelapsed.seconds / 60 / 60, 2)) + " hours.")