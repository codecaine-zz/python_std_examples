# calendar — General calendar-related functions

Here's an example of how you can use some general calendar-related functions from the `calendar` module:
```python
import calendar

# Print the current month and year
def print_current_month():
    """Prints the current month and year."""
    year = 2024  # Replace with the desired year
    month = 12  # Replace with the desired month (1-12)
    print(calendar.month(year, month))

print_current_month()

# Get the number of days in a month
def get_days_in_month():
    """Gets the number of days in a given month."""
    month = 2  # February, which has 28 days
    year = 2024  # Replace with the desired year
    print(calendar.monthrange(year, month)[1])  # [1] returns the number of days

get_days_in_month()

# Get the first day of a week (0 for Monday, 6 for Sunday)
def get_first_day_of_week():
    """Gets the first day of a given week."""
    year = 2024  # Replace with the desired year
    month = 12  # Replace with the desired month (1-12)
    print(calendar.weekday(year, month, 1))  # [1] returns the day of the week (0-6)

get_first_day_of_week()

# Get the number of weeks in a given month
def get_weeks_in_month():
    """Gets the number of weeks in a given month."""
    year = 2024  # Replace with the desired year
    month = 12  # Replace with the desired month (1-12)
    print(calendar.monthcalendar(year, month))  # Returns a matrix representing a month’s calendar
    # The index [i][j] represents the day of the week (0-6) and date (1-31)
    # We need to subtract 1 from the index because Python uses zero-based indexing

get_weeks_in_month()

# Print all holidays in a given year
def print_holidays():
    """Prints all holidays in a given year."""
    year = 2024  # Replace with the desired year
    print(calendar.monthcalendar(year, 12))  # Returns a matrix representing the month’s calendar
    for week in calendar.monthcalendar(year, 12):
        for day in week:
            if day != 0:  # Non-zero values represent days in the month
                print(f"{day}: Holiday")

print_holidays()
```
This example includes functions to:

1. Print the current month and year.
2. Get the number of days in a given month.
3. Get the first day of a week (0 for Monday, 6 for Sunday).
4. Get the number of weeks in a given month.
5. Print all holidays in a given year.

These functions are part of the `calendar` module's standard library function set and can be used to interact with dates in Python.
