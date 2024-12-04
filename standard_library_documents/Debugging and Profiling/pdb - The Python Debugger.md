# pdb — The Python Debugger

**PDB Module: Python Debugger**
=====================================

The `pdb` module provides an interactive debugger for Python programs.

### Importing the PDB Module

To use the `pdb` module, you need to import it in your Python program.
```python
import pdb
```

### Basic Usage

Here's a simple example of how to use the `pdb` module:
```python
def fibonacci(n):
    """Return the nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    pdb.set_trace()  # Set a breakpoint at this line
    print(fibonacci(10))

if __name__ == "__main__":
    main()
```

When you run this program, it will pause execution at the `pdb.set_trace()` line and present you with a debugger prompt. You can then type various commands to inspect variables, step through code, and continue execution.

### Debugger Commands

Here are some common debugger commands:

*   **b [lineno]**: Set a breakpoint at the specified line number.
*   **c**: Continue execution until the next breakpoint or the program completes.
*   **n**: Step into the current function call.
*   **s**: Step over the current function call and continue execution.
*   **r**: Return from the current function call.
*   **p [expression]**: Print the value of the specified expression.
*   **q**: Quit the debugger.
*   **l**: List the current source code file.
*   **h**: Help display the available commands.

### Example Debugger Session

Here's an example of what you might see when you run the program and set a breakpoint:
```
$ python fibonacci.py
> /path/to/fibonacci.py(9)fibonacci(n=10)
-> return fibonacci(n-1) + fibonacci(n-2)
P < FIBONACCI at 0x7f812c23d440 (main.fibonacci)>
>
```

You can then type various commands to inspect variables and step through code. For example:
```python
(p) print n
10

(s) Step over the current function call and continue execution.
> /path/to/fibonacci.py(9)fibonacci(n=9)
-> return fibonacci(n-1) + fibonacci(n-2)
P < FIBONACCI at 0x7f812c23d440 (main.fibonacci)>
>
```

### Advanced Debugger Features

The `pdb` module also supports advanced features such as:

*   **Frames**: You can switch between frames in the debugger using the `c`, `n`, and `s` commands.
*   **Locals**: You can view the local variables of the current frame using the `p` command.
*   **Threads**: You can inspect threads in the debugger using the `t` command.

### Best Practices

Here are some best practices for using the `pdb` module:

*   Set breakpoints at meaningful locations in your code to debug logic flow and errors.
*   Use the `c` command to continue execution until the next breakpoint or the program completes.
*   Use the `n` command to step into function calls and inspect variable values.
*   Use the `p` command to print variable values and inspect local variables.
