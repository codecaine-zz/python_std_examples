# bdb - Debugger framework

The `bdb` module in Python is a debugging framework that allows you to debug programs interactively at the source code level. Below are comprehensive examples of how to use each of the main functions and classes provided by this module. These examples cover basic usage, common debugging scenarios, and best practices for integrating bdb into your applications.

### 1. Basic Usage

First, ensure you have a script or function that you want to debug. For simplicity, let's create a simple script:

```python
# example_script.py
def add(a, b):
    result = a + b
    return result

result = add(5, 3)
print("Result:", result)
```

To use `bdb` for debugging this script, you can start by setting up the debugger and stepping through the code:

```python
import bdb
import sys

# Define a custom exception to handle the breakpoint
class BreakpointException(Exception):
    pass

def break_here():
    raise BreakpointException("Break here!")

if __name__ == "__main__":
    try:
        exec(open('example_script.py').read())
    except BreakpointException as e:
        bdb.set_trace()
        print(e)
```

### 2. Customizing the Debugger

You can customize the behavior of `bdb` by subclassing the `Bdb` class and overriding methods to add custom functionality:

```python
class MyBdb(bdb.Bdb):
    def post_mortem(self, frame):
        # Override post-mortem to show a custom message
        print("Post-mortem debugging started.")
        bdb.Bdb.post_mortem(self, frame)

def my_main():
    try:
        exec(open('example_script.py').read())
    except Exception as e:
        my_bdb = MyBdb()
        my_bdb.set_trace()
        print(f"Error: {e}")

if __name__ == "__main__":
    my_main()
```

### 3. Debugging Interactive Input

`bdb` can also be used to debug interactive input:

```python
import bdb
import sys

def prompt_for_input(prompt):
    return input(prompt)

def process_input(input_value):
    result = prompt_for_input("Enter a number: ")
    try:
        num = float(result)
        print(f"The processed number is: {num}")
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    try:
        process_input(input())
    except bdb.Breakpoint as e:
        print(e)
```

### 4. Using `bdb.set_trace()` in an Interactive Session

You can use `bdb.set_trace()` directly in an interactive session to start debugging a script:

```python
import bdb

def add(a, b):
    result = a + b
    return result

# Start the debugger at this point
result = add(5, 3)
print("Result:", result)

try:
    exec(open('example_script.py').read())
except Exception as e:
    bdb.set_trace()
    print(f"Error: {e}")
```

### 5. Debugging Nested Functions

When dealing with nested functions, you can use `bdb` to step into them:

```python
import bdb
import sys

def outer_function():
    def inner_function(a):
        return a * 2

    result = inner_function(3)
    print("Result:", result)

# Start the debugger at this point
outer_function()

try:
    exec(open('example_script.py').read())
except Exception as e:
    bdb.set_trace()
    print(f"Error: {e}")
```

### 6. Customizing Output

You can customize the output of `bdb` by overriding methods in your custom subclass:

```python
class MyBdb(bdb.Bdb):
    def do_print(self, arg):
        # Override print to show a custom message
        print("Custom print statement:", arg)

def my_main():
    try:
        exec(open('example_script.py').read())
    except Exception as e:
        my_bdb = MyBdb()
        my_bdb.set_trace()
        print(f"Error: {e}")

if __name__ == "__main__":
    my_main()
```

### 7. Debugging with a Custom Breakpoint

You can define a custom breakpoint by subclassing `bdb.Breakpoint`:

```python
class CustomBreakpoint(bdb.Breakpoint):
    def __init__(self, frame, code):
        super().__init__(frame, code)
        self.message = "Custom breakpoint triggered."

def my_main():
    try:
        exec(open('example_script.py').read())
    except Exception as e:
        custom_bp = CustomBreakpoint(None, None)
        custom_bp.__call__()
        print(f"Error: {e}")

if __name__ == "__main__":
    my_main()
```

### 8. Debugging with Logging

You can use `bdb` to log debugging information:

```python
import bdb
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG)

def add(a, b):
    result = a + b
    logging.debug(f"Adding {a} and {b}, got {result}")
    return result

if __name__ == "__main__":
    try:
        exec(open('example_script.py').read())
    except Exception as e:
        bdb.set_trace()
        print(f"Error: {e}")
```

These examples demonstrate various aspects of using the `bdb` module, from basic debugging to more advanced customization options. By integrating these techniques into your development workflow, you can effectively debug complex programs and scripts in Python.
