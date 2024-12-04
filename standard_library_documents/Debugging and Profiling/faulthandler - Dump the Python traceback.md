# faulthandler — Dump the Python traceback

Here's an example of how you can use `functools` and `traceback` modules to dump the Python traceback.

```python
# Import necessary modules
import functools
import traceback

def exception_handler(exctype, value, tb):
    """
    Custom exception handler to print the entire traceback.
    """
    # Print the exception type and value
    print(f"Exception Type: {exctype.__name__}")
    print(f"Value: {value}")

    # Get the entire traceback
    tb = traceback.format_tb(tb)

    # Combine the exception type, value, and traceback into a single string
    tb_str = exctype.__name__ + ":\n" + str(value) + "\n" + "".join(tb)

    print(tb_str)


# Create a custom exception handler
exception_handler_func = functools.partial(exception_handler, None, None, sys.exc_info()[2])

def main():
    try:
        # Code that might raise an exception
        x = 1 / 0

    except Exception as e:
        # Use the custom exception handler
        print("An error occurred:")
        exception_handler_func(e)

if __name__ == "__main__":
    main()
```

However, in Python 3.12 and later versions, you can use `functools.set_trace()` to set a breakpoint that will dump the traceback.

```python
# Import necessary modules
import functools

def main():
    try:
        # Code that might raise an exception
        x = 1 / 0
    except Exception as e:
        print("An error occurred:")
        print(functools.format_traceback(e))

if __name__ == "__main__":
    main()
```

In this example, when the exception occurs, `functools.format_traceback()` will dump the traceback.
