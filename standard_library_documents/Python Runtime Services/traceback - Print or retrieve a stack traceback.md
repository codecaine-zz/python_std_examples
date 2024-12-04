# traceback — Print or retrieve a stack traceback

**Traceback Module**
====================
```python
import traceback
from traceback import format_exception

# Create a traceback object
tb = traceback.format_exception(*sys.exc_info())

# Print the traceback as a string
print(tb)

# Format the traceback with a custom style
formatted_tb = format_exception(*sys.exc_info(), limit=40)
print(formatted_tb)

# Extract the type, value, and traceback of an exception
exception_type, exception_value, tb = sys.exc_info()
print(f"Exception Type: {exception_type.__name__}")
print(f"Exception Value: {exception_value}")
print(f"Traceback: {tb}")

# Print a formatted traceback with section headers
formatted_tb = traceback.format_exc(limit=20)
print(formatted_tb)

# Use the traceback module to format a custom exception message
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    # Code that may raise an exception
    x = 1 / 0
except CustomError as e:
    print(traceback.format_exc(limit=40))  # Print the formatted traceback with custom error message
```

**Explanation:**

*   The `traceback` module provides functions to extract, format, and print stack traces.
*   The `format_exception` function returns a list of strings representing the formatted exception information. It takes three arguments: `exc_type`, `exc_value`, and `exc_traceback`.
*   The `format_exc` function returns a string representing the formatted traceback. It takes one argument: `limit`, which specifies the maximum number of frames to include in the traceback.
*   The `traceback.format_tb` function returns a list of strings representing the formatted traceback information for an exception object.
*   You can use the `traceback.format_exc` function to format the current exception, and the `traceback.format_exception` function to format any type of exception.

**Use Cases:**

*   Handling exceptions in your code and printing or logging the stack trace.
*   Displaying informative error messages to users with the help of the `traceback` module.
*   Using a custom exception class and formatting its traceback for display.
