# zoneinfo - IANA time zone support

The `zoneinfo` module in Python is part of the standard library and provides classes for representing and manipulating timezone information according to the International Organization for Standardization (ISO) 8601 standard. This module allows you to work with time zones in a way that's both efficient and flexible.

Here are comprehensive examples demonstrating various functionalities of the `zoneinfo` module:

### Example 1: Getting Time Zone Information

```python
import zoneinfo

# Get a specific timezone
timezone = zoneinfo.ZoneInfo("America/New_York")

# Print the time zone name
print(timezone)  # Output: America/New_York

# Convert a naive datetime to a localized datetime
from datetime import datetime, timedelta

naive_datetime = datetime.now()
localized_datetime = naive_datetime.astimezone(timezone)
print(localized_datetime)  # Output: datetime.datetime(2023, 10, 15, 14, 30, tzinfo=zoneinfo.ZoneInfo('America/New_York'))

# Get the offset from UTC
offset = timezone.utcoffset(localized_datetime)
print(offset)  # Output: timedelta(hours=-4)

# Get the daylight saving time status
daylight_savings_time = timezone.dst(localized_datetime)
print(daylight_savings_time)  # Output: None
```

### Example 2: Iterating Over Time Zones

```python
import zoneinfo

# Iterate over all available time zones
for tz in zoneinfo.available_timezones():
    print(tz)  # Print the name of each timezone

# Get a specific time zone by its ID and use it to localize a datetime
timezone = zoneinfo.ZoneInfo("Asia/Tokyo")
localized_datetime = datetime.now(timezone)
print(localized_datetime)  # Output: datetime.datetime(2023, 10, 15, 14, 30, tzinfo=zoneinfo.ZoneInfo('Asia/Tokyo'))
```

### Example 3: Handling Time Zone Differences

```python
import zoneinfo

# Define two time zones
timezone_utc = zoneinfo.ZoneInfo("UTC")
timezone_eastern = zoneinfo.ZoneInfo("America/New_York")

# Create a datetime object for a specific date and time in UTC
utc_datetime = timezone_utc.localize(datetime(2023, 10, 15))

# Convert the UTC datetime to Eastern Standard Time
eastern_datetime = utc_datetime.astimezone(timezone_eastern)
print(eastern_datetime)  # Output: datetime.datetime(2023, 10, 14, 17, 30, tzinfo=zoneinfo.ZoneInfo('America/New_York'))

# Calculate the difference between two datetimes in different time zones
difference = eastern_datetime - utc_datetime
print(difference)  # Output: timedelta(days=-1, hours=2)
```

### Example 4: Using Zone Info Objects

```python
import zoneinfo

# Create a ZoneInfo object directly from a string
tz = zoneinfo.ZoneInfo("Europe/London")

# Check if the created time zone is valid
print(tz)  # Output: Europe/London

# Get a list of all available time zones in a specific country
countries_timezones = zoneinfo.available_timezones_by_country_code("GB")
print(countries_timezones)  # Output: ['Europe/London', 'Europe/Guernsey']

# Use the ZoneInfo object to localize and convert datetimes
utc_datetime = datetime(2023, 10, 15).replace(tzinfo=zoneinfo.utc)
localized_datetime = utc_datetime.astimezone(tz)
print(localized_datetime)  # Output: datetime.datetime(2023, 10, 15, 12, 0, tzinfo=zoneinfo.ZoneInfo('Europe/London'))
```

### Example 5: Handling Time Zones in a Web Application

```python
import zoneinfo
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    # Get the timezone from query parameters or default to UTC
    tz_str = request.args.get('timezone', 'UTC')
    
    # Create a ZoneInfo object for the specified timezone
    try:
        tz = zoneinfo.ZoneInfo(tz_str)
    except ValueError as e:
        return jsonify({"error": f"Invalid timezone: {tz_str}"}), 400
    
    # Get the current local datetime
    now = datetime.now(tz)
    
    # Return the formatted datetime
    response = {
        "datetime": now.isoformat(),
        "timezone": tz_str
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

### Example 6: Using Zone Info in a Command Line Tool

```python
import zoneinfo
from datetime import datetime, timedelta

def main():
    # Get the current time in a specified timezone
    tz_str = input("Enter the timezone (e.g., America/New_York): ")
    tz = zoneinfo.ZoneInfo(tz_str)
    
    # Get the current local datetime
    now = datetime.now(tz)
    
    # Display the current local datetime in the specified timezone
    print(f"Current time in {tz_str}: {now}")

if __name__ == "__main__":
    main()
```

### Example 7: Handling Time Zones with `pytz` for Compatibility

```python
from zoneinfo import ZoneInfo
import pytz
from datetime import datetime, timedelta

# Create a ZoneInfo object using pytz compatibility
timezone = ZoneInfo(pytz.timezone("America/New_York"))

# Get the current local datetime
now = datetime.now(timezone)
print(now)  # Output: datetime.datetime(2023, 10, 15, 14, 30, tzinfo=zoneinfo.ZoneInfo('America/New_York'))

# Convert the datetime to UTC
utc_datetime = now.astimezone(pytz.utc)
print(utc_datetime)  # Output: datetime.datetime(2023, 10, 15, 14, 30, tzinfo=pytz.utc)
```

These examples demonstrate various ways to use the `zoneinfo` module to handle time zones in Python. Each example covers different aspects of working with time zones, from simple conversions and localizations to more complex applications like web development or command-line tools.
