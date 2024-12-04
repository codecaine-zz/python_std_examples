# zoneinfo — IANA time zone support

**Zoneinfo Module**
=====================

The `zoneinfo` module provides access to the International Atomic Time (IAT) time zones, also known as Zulu time zones.

### Installation

To use the `zoneinfo` module, you need to install the `pytz` library. You can do this using pip:
```bash
pip install pytz
```
Alternatively, if you are using Python 3.9 or later, you can use the built-in `zoneinfo` module without installing any additional libraries.

### Code Examples
-----------------

#### Time Zone Objects

You can create a time zone object using the `TimeZone` class:
```python
import zoneinfo

# Create a time zone object for UTC
utc_tz = zoneinfo.TimeZone('UTC')

print(utc_tz.name)  # Output: UTC
```
Similarly, you can create time zone objects for other time zones, such as:

```python
new_york_tz = zoneinfo.TimeZone('America/New_York')
london_tz = zoneinfo.TimeZone('Europe/London')
tokyo_tz = zoneinfo.TimeZone('Asia/Tokyo')

print(new_york_tz.name)  # Output: America/New_York
print(london_tz.name)   # Output: Europe/London
print(tokyo_tz.name)    # Output: Asia/Tokyo
```
#### Time Zone Names

You can use time zone names to access the corresponding time zone object:
```python
print(zoneinfo.ZoneInfo('UTC').name)  # Output: UTC
```
Alternatively, you can use the `zoneinfo.TimeZone` class to create a time zone object from its name:
```python
print(zoneinfo.TimeZone('America/New_York'))  # Output: <zoneinfo.ZoneInfo 'America/New_York'>
```
#### Time Zone Information

You can retrieve information about a time zone using its object:
```python
import zoneinfo

# Create a time zone object for UTC
utc_tz = zoneinfo.TimeZone('UTC')

print(utc_tz.utc_offset)  # Output: -720  # UTC offset in minutes
print(utc_tz.tzname(None))  # Output: UTC
```
Similarly, you can retrieve information about other time zones:
```python
new_york_tz = zoneinfo.TimeZone('America/New_York')
london_tz = zoneinfo.TimeZone('Europe/London')

print(new_york_tz.utc_offset)   # Output: 1440  # UTC offset in minutes
print(london_tz.tzname(None))  # Output: GMT

# Get the time zone information for a specific date and time
from datetime import datetime, timedelta

dt = datetime(2022, 1, 1, tzinfo=new_york_tz)

print(new_york_tz.localize(dt).astimezone().tzname())  # Output: EST
```
#### Time Zone Conversions

You can convert a date and time object from one time zone to another using its `astimezone` method:
```python
import zoneinfo
from datetime import datetime, timedelta

# Create two time zones
new_york_tz = zoneinfo.TimeZone('America/New_York')
london_tz = zoneinfo.TimeZone('Europe/London')

# Create a date and time object in the New York time zone
dt_ny = datetime(2022, 1, 1, tzinfo=new_york_tz)

# Convert it to the London time zone
dt_london = dt_ny.astimezone(london_tz)

print(dt_london.tzname())  # Output: GMT

# Get the UTC offset of the converted date and time object
print(dt_london.utc_offset)   # Output: -7200  # UTC offset in seconds
```
Note that you can also use the `pytz` library to perform these conversions, but this example uses only the built-in `zoneinfo` module.
