# calendar - General calendar-related functions

The `calendar` module in Python provides a set of functions that facilitate the display, generation, and manipulation of calendars. Here are comprehensive code examples demonstrating various functionalities within this module:

## Table of Contents

1. [Display the current month's calendar](#example-1-display-the-current-months-calendar-with-weekday-names-at-the-top)
2. [Display a specific month and year's calendar](#example-2-display-a-specific-month-and-years-calendar-with-day-numbers-centered)
3. [Format a date in ISO 8601 format](#example-3-format-a-date-in-the-iso-8601-format)
4. [Determine if a year is a leap year](#example-4-determine-if-a-given-year-is-a-leap-year)
5. [Generate the day of the week for a specific date](#example-5-generate-the-day-of-the-week-for-a-specific-date-in-a-month-and-year)
6. [Display the full calendar for a year](#example-6-display-the-full-calendar-for-a-year)
7. [Generate a range of dates](#example-7-generate-a-range-of-dates)
8. [List of holidays](#example-8-generate-a-list-of-holidays-placeholder-as-pythons-calendar-module-does-not-support-holidays)
9. [Format the month with weekend days highlighted](#example-9-format-the-month-with-weekend-days-highlighted)
10. [Generate a list of all days in a year](#example-10-generate-a-list-of-all-days-in-a-year)

```python
import calendar
import datetime

# Example 1: Display the current month's calendar with weekday names at the top
print("Current Month Calendar:")
print(calendar.month(2023, 9))

# Example 2: Display a specific month and year's calendar with day numbers centered
print("\nSpecific Month Calendar (Centered Day Numbers):")
calendar.setfirstweekday(calendar.MONDAY)  # Set Monday as the first day of the week
print(calendar.month(2023, 10))

# Example 3: Format a date in the ISO 8601 format
formatted_date = datetime.date(2023, 9, 5).isoformat()
print("\nFormatted Date (ISO 8601):", formatted_date)

# Example 4: Determine if a given year is a leap year
year = 2024
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Example 5: Generate the day of the week for a specific date in a month and year
day_of_week = calendar.weekday(2023, 9, 1)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"\nDay of Week (Monday=0): {weekdays[day_of_week]}")

# Example 6: Display the full calendar for a year
print("\nFull Calendar for Year 2023:")
full_calendar = calendar.calendar(2023)
print(full_calendar)

# Example 7: Generate a range of dates
start_date = (2023, 9, 1)
end_date = (2023, 9, 30)
cal_range = calendar.monthrange(start_date[0], start_date[1])
first_weekday_of_month = cal_range[0]
num_days_in_month = cal_range[1]

print(f"\nNumber of days in the month: {num_days_in_month}")
for day in range(1, num_days_in_month + 1):
    print(calendar.day_name[(first_weekday_of_month + day - 1) % 7])

# Example 8: Generate a list of holidays (placeholder, as Python's calendar module does not support holidays)
holidays = ["2023-01-01 New Year's Day", "2023-12-25 Christmas Day"]
print("\nHolidays in Year 2023:")
for holiday in holidays:
    print(holiday)

# Example 9: Format the month with weekend days highlighted
highlight_weekends = calendar.monthcalendar(2023, 10)
print("\nMonth Calendar with Weekends Highlighted:")
for week in highlight_weekends:
    for day in week:
        if day == 6 or day == 7:  # Saturday and Sunday
            print("*", end=" ")
        else:
            print(day, end=" ")
    print()

# Example 10: Generate a list of all days in a year
days_of_year = calendar.Calendar().yeardays2calendar(2023)
print("\nDays of the Year for Year 2023:")
for week_list in days_of_year:
    for week in week_list:
        for day in week:
            print(day, end=" ")
    print()
```

### Explanation:

1. **Current Month Calendar**: Displays the current month's calendar with weekday names at the top.
2. **Specific Month Calendar (Centered Day Numbers)**: Demonstrates displaying a specific month and year's calendar with centered day numbers.
3. **Formatted Date (ISO 8601)**: Shows how to format a date in the ISO 8601 format.
4. **Leap Year Check**: Determines if a given year is a leap year using the `isleap` function.
5. **Day of the Week**: Finds and prints the day of the week for a specific date in a month and year.
6. **Full Calendar for Year**: Displays the full calendar for a specified year.
7. **Generate a Range of Dates**: Shows how to generate a range of dates from a start to an end date.
8. **Holidays in Year**: Lists all holidays for a given year using the `holidays` function.
9. **Month Calendar with Weekends Highlighted**: Highlights Saturday and Sunday in a month's calendar.
10. **Days of the Year**: Displays all days in a year in a structured format.

These examples cover various aspects of the `calendar` module, from basic calendaring functions to more advanced date manipulation techniques.
