# bdb — Debugger framework

**bdb Module Documentation**
==========================

The `bdb` module provides a basic implementation of a debugger framework.

### Importing the Module

```python
import bdb as pdb
```

### Using the Debugger

Here's an example of how to use the `pdb` module:

```python
# Create a simple function to test the debugger
def add(a, b):
    return a + b

try:
    result = add(2, 3)
except Exception as e:
    # Start the debugger when an exception occurs
    pdb.set_trace()
```

In this example, when an exception occurs in the `add` function, the debugger will be triggered.

### Debugger Commands

The following are some common commands that can be used with the debugger:

*   `n(ext)`: Continue execution until the next line.
*   `s(tep)`: Continue execution until the next unhandled exception or until a breakpoint is hit.
*   `c(ontinue)`: Continue execution without hitting any breakpoints.
*   `(break)` : Set a breakpoint at the current location.
*   `l(inepath)`: Display the source code of the current file.
*   `w(here)`: Show the current command history.
*   `p(expression)`: Evaluate an expression and print the result.
*   `q(uit)`: Quit the debugger.

```python
def add(a, b):
    return a + b

try:
    result = add(2, 3)
except Exception as e:
    # Start the debugger when an exception occurs
    pdb.set_trace()

# Set a breakpoint at the start of the function
pdb.set_trace()
```

### Disabling Breakpoints

By default, breakpoints are enabled. To disable them, you can use the `set_trace()` function with the `breakpoint=False` argument:

```python
def add(a, b):
    return a + b

try:
    result = add(2, 3)
except Exception as e:
    # Start the debugger when an exception occurs
    import pdb; pdb.set_trace(breakpoint=False)  # Disable breakpoints
```

### Installing Breakpoints Manually

If you want to install breakpoints manually, you can use the `set_trace()` function with the `breakpoint=True` argument:

```python
def add(a, b):
    return a + b

# Set a breakpoint at the start of the function
import pdb; pdb.set_trace(breakpoint=True)  # Enable breakpoints
```

### Using Breakpoints with Conditional Statements

Breakpoints can also be used with conditional statements. Here's an example:

```python
def add(a, b):
    if a > b:
        return a + b
    else:
        raise ValueError("a is not greater than b")

try:
    result = add(2, 3)
except Exception as e:
    # Start the debugger when an exception occurs
    import pdb; pdb.set_trace(breakpoint=True)  # Enable breakpoints
```

In this example, a breakpoint will be triggered if `a` is not greater than `b`.
