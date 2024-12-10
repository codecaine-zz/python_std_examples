# enum - Support for enumerations

The `enum` module in Python provides a way to define a set of symbolic names bound to unique values. This is particularly useful for creating clear, readable code that avoids magic numbers and makes it easier to maintain.

Below are some comprehensive examples demonstrating various functionalities of the `enum` module:

```python
# Importing the enum module
from enum import Enum

# Example 1: Basic usage of Enum with auto-incremental values
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing an enum member by its name or value
print(Color.RED)  # Output: Color.RED
print(Color(2))     # Output: Color.GREEN

# Iterating over all members of the Enum
for color in Color:
    print(color)

# Example 2: Using auto-incremental values with a starting point
class Day(Enum):
    MONDAY = 1
    TUESDAY
    WEDNESDAY
    THURSDAY
    FRIDAY
    SATURDAY
    SUNDAY

print(Day.MONDAY)  # Output: Day.MONDAY
print(Day.TUESDAY)  # Output: Day.TUESDAY
# Note: The next value is automatically determined based on the previous one

# Example 3: Using automatic enumeration values with a custom step
class Step(Enum):
    FIRST = 0
    SECOND = -1
    THIRD = None

print(Step.FIRST)   # Output: Step.FIRST
print(Step.SECOND)  # Output: Step.SECOND
print(Step.THIRD)  # Output: Step.THIRD

# Example 4: Using flags to combine multiple enum members
class Flags(Enum):
    READ = 1
    WRITE = 2
    EXECUTE = 4

combined_flags = Flags.READ | Flags.WRITE | Flags.EXECUTE
print(combined_flags)  # Output: Flags(7)

# Checking if a member is in an enum
if Flags.WRITE in combined_flags:
    print("WRITE flag is set")

# Example 5: Using auto-incremental values with a custom step and starting point
class AutoIncrement(Enum):
    ONE = 1
    TWO
    THREE
    FOUR

print(AutoIncrement.ONE)  # Output: AutoIncrement.ONE
print(AutoIncrement.THREE)  # Output: AutoIncrement.THREE
```

The `enum` module provides a powerful way to define enumerations in Python, making code more readable and maintainable. It also offers additional functionalities like combining enum members using flags and customizing the enumeration values. By using enums, you can create clear, self-documenting code that is easier to understand and work with.
```
