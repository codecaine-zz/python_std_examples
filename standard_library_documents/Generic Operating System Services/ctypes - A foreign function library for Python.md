# ctypes - A foreign function library for Python

The `ctypes` module in Python provides C compatible data types, and allows calling functions in DLLs or shared libraries. This is useful for interfacing with native libraries and interacting with hardware.

Below are some comprehensive code examples demonstrating various functionalities of the `ctypes` module:

### Example 1: Loading a Shared Library

```python
import ctypes

# Load a shared library (e.g., libc.so on Linux)
libc = ctypes.CDLL('libc.so.6')

# Define a function from the library using ctypes.CFUNCTYPE
def print_message(message):
    libc.printf(b"%s\n", message.encode())

# Call the function with an argument
print_message("Hello, World!")
```

### Example 2: Passing Arguments and Returning Results

```python
import ctypes

# Load the math library (libm.so on Linux)
math = ctypes.CDLL('libm.so.6')

# Define a function from the library using ctypes.CFUNCTYPE
def sin(x):
    result = ctypes.c_double()
    math.sin(ctypes.byref(result), x)
    return result.value

# Call the function with an argument and print the result
print(f"The sine of 30 degrees (in radians) is: {sin(3.14159 / 6)}")
```

### Example 3: Structures and Pointers

```python
import ctypes

# Define a structure using ctypes.Structure
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

# Create an instance of the structure
p1 = Point(5, 10)

# Print the fields of the structure
print(f"Point p1: ({p1.x}, {p1.y})")

# Define a function that takes a pointer to a struct and modifies it
def modify_point(point):
    point.x += 1
    point.y += 2

# Modify the point object using the function
modify_point(p1)
print(f"Modified Point p1: ({p1.x}, {p1.y})")
```

### Example 4: Callback Functions

```python
import ctypes

# Define a callback function type
def my_callback(arg):
    print("Callback called with argument:", arg)

# Register the callback function using ctypes.CFUNCTYPE
callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int)
my_function_pointer = callback_type(my_callback)

# Call the callback function from another function
def call_my_callback():
    my_function_pointer(42)

# Execute the callback function
call_my_callback()
```

### Example 5: Using Enumerations

```python
import ctypes

# Define an enumeration using ctypes.c_int and an enum class
class Color(ctypes.c_int):
    RED = 1
    GREEN = 2
    BLUE = 3

# Create a variable of the enumeration type
color = Color.RED

# Print the value of the enumeration
print(f"The color is {color}")

# Define a function that takes an enum and returns its name
def get_color_name(color):
    color_names = {
        Color.RED: "Red",
        Color.GREEN: "Green",
        Color.BLUE: "Blue"
    }
    return color_names[color]

# Get the name of the color
print(f"The name of the color is {get_color_name(color)}")
```

### Example 6: Dynamic Library Path

```python
import ctypes

# Load a shared library using an absolute path
lib_path = "/path/to/your/library.so"
my_lib = ctypes.CDLL(lib_path)

# Define a function from the loaded library
def my_lib_function():
    result = ctypes.c_int()
    my_lib.my_lib_function(ctypes.byref(result))
    return result.value

# Call the function and print the result
print(f"The result of my_lib_function is: {my_lib_function()}")
```

### Example 7: Loading a Shared Library with Multiple Symbols

```python
import ctypes

# Load a shared library with multiple symbols
lib = ctypes.CDLL('libexample.so')

# Define functions from the library using ctypes.CFUNCTYPE
def function1(arg):
    result = ctypes.c_int()
    lib.function1(ctypes.byref(result), arg)
    return result.value

def function2(arg):
    result = ctypes.c_double()
    lib.function2.argtypes = [ctypes.c_float]
    lib.function2.restype = ctypes.c_double
    lib.function2(ctypes.c_float(arg))
    return result.value

# Call the functions and print the results
print(f"Result of function1(5): {function1(5)}")
print(f"Result of function2(3.14): {function2(3.14)}")
```

### Example 8: Passing Structures to Functions

```python
import ctypes

# Define a structure using ctypes.Structure
class Rectangle(ctypes.Structure):
    _fields_ = [("width", ctypes.c_int), ("height", ctypes.c_int)]

# Create an instance of the structure
rect = Rectangle(10, 20)

# Define a function from the library that takes a pointer to a struct
def print_rect(rect_ptr):
    rect_obj = ctypes.cast(rect_ptr, ctypes.POINTER(Rectangle)).contents
    print(f"Rectangle: Width={rect_obj.width}, Height={rect_obj.height}")

# Call the function with a pointer to the structure
print_rect(ctypes.byref(rect))
```

These examples demonstrate various ways to use the `ctypes` module for interfacing with native libraries, including loading shared libraries, passing arguments and returning results, using structures and pointers, working with callback functions, enumerations, dynamic library paths, handling multiple symbols in a single load, and passing structures to functions.
