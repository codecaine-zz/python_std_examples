# trace — Trace or track Python statement execution

Here's an example of how you can use the `trace` function from the `traceback` module in Python:

```python
import traceback

# Function to be traced
def add(a, b):
    """
    Adds two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    print(f"Inside add function with args {a} and {b}")
    return a + b

# Traceback an exception
try:
    # Simulate a division by zero error
    result = 1 / 0
except Exception as e:
    # Get the traceback of the current exception
    tb = traceback.format_exc()
    print("Traceback:")
    print(tb)

# Use trace to trace function execution
def traced_add(a, b):
    return add(a, b)

traced_result = traced_add(1, 2)
print(f"Traced result: {traced_result}")

# Tracing a specific point in the call stack
import sys

def outer_function():
    try:
        # Simulate an exception
        raise Exception("Outer function raised")
    except Exception as e:
        print("Caught exception:", str(e))
        tb = traceback.extract_stack()
        print("Call stack:")
        for i, frame in enumerate(tb):
            print(f"{i}: {frame.function} at line {frame.lineno}")

outer_function()

# Tracing the entire call stack
tb = traceback.extract_stack()
print("Call stack:")
for i, frame in enumerate(tb):
    print(f"{i}: {frame.function} at line {frame.lineno}")
```

Here are some key points about `traceback`:

- **`format_exc()` function:** This function returns a string containing the formatted traceback of the current exception.
- **`extract_stack()` function:** This function returns a list of frames in the call stack. Each frame is a dictionary with keys like 'function', 'filename', and 'lineno'.
- **`traceback.print_tb()` function:** This function prints the entire traceback directly to the output stream.

Here are some key points about tracing:

- **Tracing exceptions:** You can use `trace` to catch exceptions, log their type, value, and location in your program.
- **Tracing function calls:** You can use `trace` to track what's happening inside your functions, like which arguments they're using or where the function call came from.
- **Tracing entire call stack:** You can use `extract_stack()` to get the full history of function calls up to the current point in your program.

You can also use `traceback` with other modules such as `inspect`, `sys`, and `contextlib`. 

For instance:

```python
import inspect

def traced_function():
    result = func_to_trace(1, 2)
    print(f"Result: {result}")
    return result

def func_to_trace(a, b):
    # Do something with the function arguments here...
    pass
```

Note that this example will run into a recursion error if `func_to_trace` calls itself directly.
