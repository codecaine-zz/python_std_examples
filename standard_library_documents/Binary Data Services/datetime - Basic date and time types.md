# datetime - Basic date and time types

Here are comprehensive and well-documented code examples for the Python standard library module `datetime`, focusing on its basic date and time types.

## Table of Contents

1. [Importing the datetime Module](#1-importing-the-datetime-module)
2. [Creating a Current Date and Time](#2-creating-a-current-date-and-time)
3. [Formatting Dates and Times](#3-formatting-dates-and-times)
4. [Creating a Specific Date](#4-creating-a-specific-date)
5. [Adding and Subtracting Time](#5-adding-and-subtracting-time)
6. [Parsing Strings into Dates](#6-parsing-strings-into-dates)
7. [Working with Time Zones](#7-working-with-time-zones)
8. [Comparing Dates and Times](#8-comparing-dates-and-times)
9. [Working with Time Periods](#9-working-with-time-periods)
10. [Creating Time Objects](#10-creating-time-objects)

### 1. Importing the `datetime` Module

The first step is to import the `datetime` module, which provides classes for manipulating dates and times.

```python
# Import the datetime class from the datetime module
from datetime import datetime
```

### 2. Creating a Current Date and Time

You can create a current date and time using the `now()` method of the `datetime` class.

```python
# Get the current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
```

### 3. Formatting Dates and Times

Dates and times can be formatted using various format codes, which are similar to those used by the C `strftime()` function.

```python
# Format the current date and time
formatted_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date_time)
```

### 4. Creating a Specific Date

You can create a specific date using the `datetime` class with `year`, `month`, and `day` arguments.

```python
# Create a specific date
specific_date = datetime(2023, 10, 5)
print("Specific Date:", specific_date)
```

### 5. Adding and Subtracting Time

You can add or subtract time from a `datetime` object using the `timedelta` class.

```python
# Create a timedelta of one day
one_day = datetime.timedelta(days=1)

# Add one day to the current date
future_date = current_datetime + one_day
print("Future Date:", future_date)
```

### 6. Parsing Strings into Dates

You can parse strings containing dates into `datetime` objects using the `strptime()` method.

```python
# Parse a string into a datetime object
parsed_date_time = datetime.strptime("2023-10-05 14:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_date_time)
```

### 7. Working with Time Zones

The `pytz` library can be used to work with time zones, but for basic usage, you can use the `datetime.timezone()` function.

```python
from datetime import timezone

# Create a timezone object for UTC
utc_timezone = timezone.utc

# Get the current date and time in UTC
utc_datetime = datetime.now(utc_timezone)
print("Current Date and Time in UTC:", utc_datetime)
```

### 8. Comparing Dates and Times

Dates and times can be compared using comparison operators.

```python
# Compare two dates
date1 = datetime(2023, 9, 5)
date2 = datetime(2023, 10, 5)

if date1 < date2:
    print("Date1 is before Date2")
elif date1 > date2:
    print("Date1 is after Date2")
else:
    print("Date1 and Date2 are the same")
```

### 9. Working with Time Periods

Time periods can be represented using `timedelta` objects.

```python
# Create a timedelta of one month
one_month = datetime.timedelta(days=30)

# Add one month to the current date
future_date_with_month = current_datetime + one_month
print("Future Date with Month:", future_date_with_month)
```

### 10. Creating Time Objects

You can create time objects using the `time` module, which is part of the `datetime` module.

```python
from datetime import time

# Create a specific time
specific_time = time(14, 30)
print("Specific Time:", specific_time)
```

### Conclusion

These examples cover the basic functionalities of the `datetime` module in Python. They demonstrate how to create, manipulate, and format dates and times, as well as work with time zones and compare dates and times. These examples are suitable for both beginner and advanced users and can be used in a variety of applications involving date and time handling.
