# sys - System-specific parameters and functions

The `sys` module in Python provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. Below are comprehensive and well-documented code examples for each functionality provided by the `sys` module.

### 1. `sys.version`
This function returns a string containing the version number of the Python interpreter as a string in the form 'x.x.y'.

```python
# Example: Retrieve the Python version
import sys

print("Python version:", sys.version)
```

### 2. `sys.executable`
This function returns the full path to the interpreter that started the current program.

```python
# Example: Retrieve the executable file path
import sys

print("Executable path:", sys.executable)
```

### 3. `sys.platform`
This function returns a string identifying the underlying platform on which Python is running.

```python
# Example: Retrieve the platform
import sys

print("Platform:", sys.platform)
```

### 4. `sys.modules`
This variable holds the dictionary of all currently loaded modules, with keys as module names and values as their corresponding module objects.

```python
# Example: Print all imported modules
import sys

for name in sys.modules:
    print(name)
```

### 5. `sys.maxsize`
This constant holds the maximum integer value that can be stored in an integer type on the current platform.

```python
# Example: Retrieve the maximum size of integers
import sys

print("Maximum size of integers:", sys.maxsize)
```

### 6. `sys.argv`
This list contains the command-line arguments passed to the script when it was run. The first element is always a string 'scriptname', and the rest are the remaining arguments.

```python
# Example: Print command-line arguments
import sys

print("Command-line arguments:", sys.argv)
```

### 7. `sys.path`
This list contains the current Python module search path. This is used when importing modules.

```python
# Example: Print current Python path
import sys

print("Current Python path:", sys.path)
```

### 8. `sys.stdin`, `sys.stdout`, and `sys.stderr`
These are file-like objects representing standard input, standard output, and standard error streams, respectively. You can use them to read from or write to these streams.

```python
# Example: Read from stdin and print the result
import sys

user_input = sys.stdin.read()
print("User input:", user_input)

# Example: Write to stdout
import sys

sys.stdout.write("Hello, World!\n")
```

### 9. `sys.exit([status])`
This function exits the script with an optional exit status code. If no argument is given, it defaults to 0.

```python
# Example: Exit the program
import sys

print("Exiting the program...")
sys.exit(0)
```

### 10. `sys.getsizeof(obj[, default])`
This function returns the size of an object in bytes. The `default` parameter is used if `obj` is a type object, not an instance.

```python
# Example: Get the size of an integer
import sys

num = 123456
print("Size of", num, ":", sys.getsizeof(num))

# Example: Get the size of a string
str_obj = "Hello, World!"
print("Size of", str_obj, ":", sys.getsizeof(str_obj))
```

### 11. `sys.settrace(func)`
This function sets a global trace function for all currently running Python programs.

```python
# Example: Set a global trace function
import sys

def my_trace(frame, event, arg):
    print(event, frame.f_lineno)

sys.settrace(my_trace)
```

### 12. `sys.getdefaultencoding()`
This function returns the default encoding used by the interpreter for strings.

```python
# Example: Retrieve the default encoding
import sys

print("Default encoding:", sys.getdefaultencoding())
```

### 13. `sys.setrecursionlimit(limit)`
This function sets the maximum depth of recursion. If a recursive function calls itself too many times, it will raise a `RecursionError`.

```python
# Example: Set the recursion limit
import sys

print("Current recursion limit:", sys.getrecursionlimit())
sys.setrecursionlimit(1000)
print("New recursion limit:", sys.getrecursionlimit())
```

### 14. `sys.exitfunc`
This variable holds a function to be called when the interpreter exits, such as at the end of a program or on an error.

```python
# Example: Set an exit function
import sys

def my_exit_function():
    print("Exiting with custom message...")

sys.exitfunc = my_exit_function
```

### 15. `sys.dont_write_bytecode`
This variable is used to prevent the creation of `.pyc` files.

```python
# Example: Disable bytecode writing
import sys

print("Bytecode writing enabled:", not sys.dont_write_bytecode)
sys.dont_write_bytecode = True
print("Bytecode writing disabled:", not sys.dont_write_bytecode)
```

### 16. `sys.flags`
This dictionary contains various flags that control the behavior of Python.

```python
# Example: Print all flags
import sys

for name, value in vars(sys).items():
    if isinstance(value, bool) and not name.startswith('__'):
        print(name, value)
```

These examples cover a wide range of functionalities provided by the `sys` module. Each example is thoroughly documented to ensure clarity and ease of understanding.
