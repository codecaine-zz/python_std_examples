# math — Mathematical functions

**Math Module Code Examples**
=====================================

The math module provides access to mathematical functions.

### Importing the Math Module
```python
# Import the math module
import math

# Print the version of the math module
print(math.version)

# Alternatively, you can also import the math module using 'from math import *'
# from math import *

# Access a specific function from the math module
# print(math.sin(30))  # Calculate sine of 30 degrees
```

### Basic Math Functions
```python
# Trigonometric functions
print(math.sin(0))  # Sine of 0 degrees
print(math.cos(0))  # Cosine of 0 degrees
print(math.tan(0))  # Tangent of 0 degrees

print(math.sin(math.pi/2))  # Sine of pi/2 radians (90 degrees)

# Exponential and logarithmic functions
import math
x = 10
exp_x = math.exp(x)  # Calculate exponential of x
log_x = math.log(x)   # Calculate natural logarithm of x

# Power function
print(math.pow(2, 3))  # Square the number 2

# Absolute value
print(abs(-5))  # Calculate absolute value of -5

# Round a number to a specific decimal place
print(round(10.1234, 2))  # Round 10.1234 to 2 decimal places
```

### Hyperbolic Functions
```python
import math

# Hyperbolic sine (hyperbolic arc sine)
y = math.sinh(1)  # Calculate hyperbolic sine of 1

# Hyperbolic cosine (hyperbolic arc cosine)
z = math.cosh(0)  # Calculate hyperbolic cosine of 0

# Hyperbolic tangent (hyperbolic arc tangent)
t = math.tanh(0.5)  # Calculate hyperbolic tangent of 0.5
```

### Rounding and Remainder Functions
```python
import math

# Round a number to the nearest integer
print(math.ceil(10.1234))  # Round 10.1234 to the nearest integer
print(math.floor(10.1234))  # Round 10.1234 to the nearest lower integer

# Calculate remainder of division
a = 17
b = 5
remainder = a % b  # Calculate remainder of 17 divided by 5
```

### Math Constants
```python
import math

print(math.pi)  # Pi constant
print(math.e)   # Euler's number (approximately 2.71828)
```

### Math Degrees to Radians Conversion Function
```python
import math

def deg_to_rad(degrees):
    """
    Convert degrees to radians.
    
    Parameters:
    degrees (float): Angle in degrees
    
    Returns:
    float: Angle in radians
    """
    return degrees * math.pi / 180

# Test the function
print(deg_to_rad(30))  # Output: pi/6
```
