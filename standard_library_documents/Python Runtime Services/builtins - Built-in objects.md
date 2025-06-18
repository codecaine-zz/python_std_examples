# builtins - Built-in objects
## Table of Contents

1. [1. Accessing Built-in Functions](#1-accessing-built-in-functions)
2. [2. Accessing Built-in Types](#2-accessing-built-in-types)
3. [3. Accessing Built-in Exceptions](#3-accessing-built-in-exceptions)
4. [4. Accessing Built-in Constants](#4-accessing-built-in-constants)
5. [5. Accessing Built-in Modules](#5-accessing-built-in-modules)
6. [6. Accessing Built-in Classes](#6-accessing-built-in-classes)
7. [7. Accessing Built-in Methods](#7-accessing-built-in-methods)
8. [8. Accessing Built-in Modules and Functions](#8-accessing-built-in-modules-and-functions)
9. [9. Accessing Built-in Constants and Functions](#9-accessing-built-in-constants-and-functions)
10. [10. Accessing Built-in Operators](#10-accessing-built-in-operators)



The `builtins` module in Python is a special module that contains all the built-in names available in every interactive session and in all modules. It provides access to the most commonly used functions, types, and exceptions.

Here are some comprehensive code examples for each functionality in the `builtins` module:

### 1. Accessing Built-in Functions

```python
# Example: Using abs() function
number = -42
absolute_value = abs(number)
print(f"The absolute value of {number} is {absolute_value}")

# Example: Using max() function
list_of_numbers = [3, 5, 7, 1, 9]
maximum_number = max(list_of_numbers)
print(f"The maximum number in the list is {maximum_number}")

# Example: Using min() function
minimum_number = min(list_of_numbers)
print(f"The minimum number in the list is {minimum_number}")
```

### 2. Accessing Built-in Types

```python
# Example: Creating a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Example: Creating a tuple
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)

# Example: Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30}
print("Dictionary:", my_dict)
```

### 3. Accessing Built-in Exceptions

```python
# Example: Using ValueError exception to catch invalid input
try:
    value = int('abc')
except ValueError as e:
    print(f"ValueError caught: {e}")

# Example: Using FileNotFoundError exception to handle missing files
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError caught: {e}")
```

### 4. Accessing Built-in Constants

```python
# Example: Using True, False, and None constants
print("True:", True)
print("False:", False)
print("None:", None)

# Example: Accessing the maximum value an int can hold in Python
max_int = sys.maxsize
print(f"The maximum value an int can hold is {max_int}")

# Example: Using pi from math module (accessed through builtins)
import math
pi_value = math.pi
print(f"Value of pi: {pi_value}")
```

### 5. Accessing Built-in Modules

```python
# Example: Importing the math module
import math

# Using a function from the math module
result = math.sqrt(25)
print(f"The square root of 25 is {result}")

# Accessing an attribute from the math module
e_value = math.e
print(f"Value of e (Euler's number): {e_value}")
```

### 6. Accessing Built-in Classes

```python
# Example: Using the complex class to create a complex number
complex_number = complex(3, 4)
print("Complex Number:", complex_number)

# Example: Using the list class to create a mutable list
mutable_list = [1, 2, 3]
print("Mutable List:", mutable_list)

# Accessing an attribute from a class in builtins
list_len = len(mutable_list)
print(f"Length of the list: {list_len}")
```

### 7. Accessing Built-in Methods

```python
# Example: Using the upper() method on a string
text = "hello"
uppercase_text = text.upper()
print(f"Uppercase text: '{uppercase_text}'")

# Example: Using the append() method on a list
mutable_list.append(6)
print("Updated List:", mutable_list)

# Accessing an attribute of a class instance in builtins
list_count = len(mutable_list)
print(f"Length of the list after appending: {list_count}")
```

### 8. Accessing Built-in Modules and Functions

```python
# Example: Using the time module to get current time
import time

current_time = time.localtime()
print("Current Time:", current_time)

# Example: Using the random module to generate a random number
import random

random_number = random.randint(1, 10)
print(f"Random Number between 1 and 10: {random_number}")
```

### 9. Accessing Built-in Constants and Functions

```python
# Example: Using the math constants pi and e
import math

pi_value = math.pi
e_value = math.e

print(f"Value of pi: {pi_value}")
print(f"Value of e (Euler's number): {e_value}")

# Example: Using the math functions sin() and cos()
sin_value = math.sin(math.pi / 2)
cos_value = math.cos(0)

print(f"Sine of pi/2: {sin_value}")
print(f"Cosine of 0: {cos_value}")
```

### 10. Accessing Built-in Operators

```python
# Example: Using the addition operator (+) with numbers
num1 = 5
num2 = 3
sum_result = num1 + num2
print(f"Sum of {num1} and {num2} is {sum_result}")

# Example: Using the multiplication operator (*) with strings
string1 = "Hello"
string2 = "World"
product_string = string1 * 3
print(f"Product of '{string1}' repeated 3 times: '{product_string}'")
```

These examples demonstrate various aspects of using the `builtins` module, including accessing built-in functions, types, exceptions, constants, modules, classes, methods, and operators. Each example is clear, concise, and includes comments to explain each step.
