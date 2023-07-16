#bài tập 1
from datetime import datetime
time_now = datetime.now()
current_day = time_now.day
current_month = time_now.month
current_year = time_now.year
current_hour = time_now.hour
current_minute = time_now.minute
timestamp = time_now.timestamp()

#bai tập 2
t1 = time_now.strftime("%m/%d/%Y")
print(t1)
t2 = time_now.strftime("%H:%M:%S")
print(t2)

#bai tập 3
to_day_str = "5 December, 2019"
str_to_time = datetime.strptime(to_day_str, "%d %B, %Y")
print(str_to_time)

#bai tập 4
from datetime import *
time_now = date(year=2023, month=7, day=16)
new_year = date(year=2024, month=1, day=1)
print(new_year - time_now)

#bai tập 5
day_now = date(year=2023, month=7, day=16)
past = date(year=1970, month=1, day=1)
print(day_now - past)

