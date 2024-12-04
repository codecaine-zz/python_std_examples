# numbers — Numeric abstract base classes

Here's an example of how you can use the `numbers` module from Python's standard library.

```python
# Importing numbers module
from numbers import *

# Create instances of numeric types
int_instance = 5   # Integer
float_instance = 3.14  # Floating Point Number
complex_instance = 2+7j  # Complex Number

# Printing the values
print("Integer Instance:", int_instance)
print("Floating Point Instance:", float_instance)
print("Complex Instance:", complex_instance)

# Using numeric types in arithmetic operations
result_int_addition = int_instance + 5  # Integer Addition
result_float_multiplication = float_instance * 2.5  # Floating Point Multiplication

# Printing the results
print("Integer Addition Result:", result_int_addition)
print("Floating Point Multiplication Result:", result_float_multiplication)

# Checking if a number is an instance of a specific numeric type
if isinstance(int_instance, int):
    print(f"{int_instance} is an integer")
elif isinstance(float_instance, float):
    print(f"{float_instance} is a floating point number")
elif isinstance(complex_instance, complex):
    print(f"{complex_instance} is a complex number")

# Using numeric types in comparison operations
print("Is int_instance greater than 10?", int_instance > 10)
print("Is float_instance less than 2.5?", float_instance < 2.5)

# Checking the type of a number
if isinstance(int_instance, (int, float)):
    print(f"{int_instance} is either an integer or a floating point number")
elif isinstance(complex_instance, (int, float)):
    print(f"{complex_instance} is either an integer or a floating point number")

# Using numeric types in membership tests
print("Is 5 an instance of the int type?", isinstance(5, int))
print("Is 3.14 an instance of the float type?", isinstance(3.14, float))

# Checking if a number is finite (not infinite)
if complex_instance.imag == 0 and complex_instance.real != 0:
    print(f"{complex_instance} is a real number")
elif float_instance == float_instance:  # Not strictly equal to itself because of floating point precision issues
    print(f"{float_instance} is a non-negative zero value")
else:
    print(f"{float_instance} is a finite number")

# Checking if a number is an integer or a rational (not necessarily an integer)
if isinstance(int_instance, int):
    print(f"{int_instance} is an integer")
elif isinstance(complex_instance, complex) and complex_instance.imag == 0:
    print(f"{complex_instance} is a real rational number")
else:
    print(f"{float_instance} is not an integer or rational")

# Using numeric types in geometric calculations
import math

print("Is the square root of 9 an integer?", isinstance(math.sqrt(9), int))
print("Is the cube root of 27 an integer?", isinstance(round(27 ** (1./3)), int))

```
This example showcases how you can use instances of different numeric types, perform arithmetic operations, and make comparisons with these numbers.
