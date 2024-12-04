# time — Time access and conversions

**Time Module Code Generation**
=====================================

The `time` module provides various time-related functions.

### 1. Time Functions

```python
import time

# Get current time in seconds since the epoch (January 1, 1970)
current_time = time.time()
print(f"Current time: {current_time}")

# Get current time as a float in fractional seconds
current_time_float = time.time()
print(f"Current time (float): {current_time_float}")

# Get the number of microseconds since the epoch
microseconds = int(time.time() * 1e6)
print(f"Microseconds: {microseconds}")

# Sleep for 5 seconds
time.sleep(5)

# Get the current date and time
now = time.localtime()
print("Current Date and Time:")
print(f"Year: {now.tm_year}")
print(f"Month: {now.tm_mon}")
print(f"Day: {now.tm_mday}")
print(f"Hour: {now.tm_hour}")
print(f"Minute: {now.tm_min}")
print(f"Second: {now.tm_sec}")

# Convert time to UTC
utc_now = time.gmtime()
print("UTC Current Date and Time:")
print(f"Year: {utc_now.tm_year}")
print(f"Month: {utc_now.tm_mon}")
print(f"Day: {utc_now.tm_mday}")
print(f"Hour: {utc_now.tm_hour}")
print(f"Minute: {utc_now.tm_min}")
print(f"Second: {utc_now.tm_sec}")

# Convert time to local
local_now = time.localtime()
print("Local Current Date and Time:")
print(f"Year: {local_now.tm_year}")
print(f"Month: {local_now.tm_mon}")
print(f"Day: {local_now.tm_mday}")
print(f"Hour: {local_now.tm_hour}")
print(f"Minute: {local_now.tm_min}")
print(f"Second: {local_now.tm_sec}")

# Get the time zone offset in seconds
offset = time.tzname()
print("Time Zone Offset:")
print(offset)

# Convert time to string format (HH:MM)
time_str = time.strftime("%H:%M")
print(f"Time String: {time_str}")
```

### 2. Timezone Functions

```python
import time
import pytz

# Set the timezone to UTC
utc_now = time.tzlocal()
utc_tz = pytz.UTC
utc_now_tz = utc_tz.localize(time.time())
print("UTC Current Date and Time:")
print(f"Year: {utc_now_tz.tm_year}")
print(f"Month: {utc_now_tz.tm_mon}")
print(f"Day: {utc_now_tz.tm_mday}")
print(f"Hour: {utc_now_tz.tm_hour}")
print(f"Minute: {utc_now_tz.tm_min}")
print(f"Second: {utc_now_tz.tm_sec}")

# Set the timezone to local
local_tz = pytz.timezone("US/Pacific")
local_time = time.localtime()
local_time_tz = local_tz.localize(local_time)
print("Local Current Date and Time:")
print(f"Year: {local_time_tz.tm_year}")
print(f"Month: {local_time_tz.tm_mon}")
print(f"Day: {local_time_tz.tm_mday}")
print(f"Hour: {local_time_tz.tm_hour}")
print(f"Minute: {local_time_tz.tm_min}")
print(f"Second: {local_time_tz.tm_sec}")

# Get the timezone offset in seconds
offset = local_time_tz.utcoffset(time.time()).total_seconds()
print("Time Zone Offset:")
print(offset)
```

### 3. Date and Time Functions

```python
import time
from datetime import datetime

# Create a date and time object from the current time
now = datetime.now()
print(f"Current Date and Time: {now}")

# Get the year, month, day, hour, minute, second values from the current date and time
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")

# Create a date and time object from the string format (YYYY-MM-DD HH:MM:SS)
date_time_str = "2022-01-01 12:30:00"
date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
print(f"Date and Time Object: {date_time_obj}")
```

### 4. Calendar Functions

```python
import time
from calendar import monthrange

# Get the number of days in a month
month = 12
days_in_month = monthrange(2022, month)[1]
print(f"Days in {month} 2022: {days_in_month}")

# Get the weekday (0-6) and day (1-31) for a specific date
year = 2022
month = 1
day = 1
weekday = time.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").tm_wday
print(f"Weekday: {weekday}")
day = monthrange(year, month)[1]
print(f"Day: {day}")

# Get the day of the week (Monday=0, Sunday=6) for a specific date
year = 2022
month = 1
day = 1
week_day = time.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").tm_wday
print(f"Day of Week: {week_day}")
```
