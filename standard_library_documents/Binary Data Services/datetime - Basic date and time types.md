# datetime — Basic date and time types

**datetime Module**
====================

The `datetime` module provides classes for manipulating dates and times.

**Importing Modules**
---------------------

```python
import datetime
```

**Basic Classes**
-----------------

### 1. `date` Class

Represents a specific point in time, without any time information.

```python
# Create a date object
date_obj = datetime.date(2022, 7, 25)

print(date_obj)  # Output: 2022-07-25
```

### 2. `time` Class

Represents a specific point in time, with no date information.

```python
# Create a time object
time_obj = datetime.time(14, 30, 0)

print(time_obj)  # Output: 14:30:00
```

### 3. `datetime` Class

Combines both date and time information.

```python
# Create a datetime object
datetime_obj = datetime.datetime(2022, 7, 25, 14, 30, 0)

print(datetime_obj)  # Output: 2022-07-25 14:30:00
```

### 4. `timedelta` Class

Represents a duration of time.

```python
# Create a timedelta object representing 3 days
timedelta = datetime.timedelta(days=3)

print(timedelta)  # Output: 0 days, 0:00:00
```

**Arithmetic Operations**
-------------------------

You can use the `timedelta` class to perform arithmetic operations on dates and times.

```python
# Add 2 days to a date object
date_obj = datetime.date(2022, 7, 25)
new_date_obj = date_obj + datetime.timedelta(days=2)

print(new_date_obj)  # Output: 2022-07-27

# Subtract 1 day from a time object
time_obj = datetime.time(14, 30, 0)
new_time_obj = time_obj - datetime.timedelta(days=1)

print(new_time_obj)  # Output: 13:30:00
```

**Formatting**
--------------

You can use the `strftime` and `strptime` methods to format dates and times.

```python
# Format a date object as 'YYYY-MM-DD'
date_obj = datetime.date(2022, 7, 25)
formatted_date = date_obj.strftime('%Y-%m-%d')

print(formatted_date)  # Output: 2022-07-25

# Parse a string into a date object
date_str = '2022-07-25'
date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

print(date_obj)  # Output: 2022-07-25
```

**Zones**
---------

You can use the `tzinfo` class to represent time zones.

```python
# Create a timezone object for UTC
from datetime import timezone

utc_tz = timezone(timedelta(hours=0))

print(utc_tz)  # Output: UTC
```

Note: This is not an exhaustive list of all possible classes and methods in the `datetime` module.
