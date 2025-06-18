# math - Mathematical functions
## Table of Contents

1. [1. **Trigonometric Functions**](#1-trigonometric-functions)
2. [2. **Logarithmic Functions**](#2-logarithmic-functions)
3. [3. **Exponential and Power Functions**](#3-exponential-and-power-functions)
4. [4. **Square Root and Floor/Ceiling Functions**](#4-square-root-and-floorceiling-functions)
5. [5. **Constants**](#5-constants)
6. [6. **Rounding Functions**](#6-rounding-functions)
7. [7. **Factorial and Gamma Function**](#7-factorial-and-gamma-function)
8. [8. **Modular Arithmetic Functions**](#8-modular-arithmetic-functions)
9. [9. **Hyperbolic Functions**](#9-hyperbolic-functions)
10. [10. **Error Functions and Complementary Error Function**](#10-error-functions-and-complementary-error-function)



The `math` module is a fundamental part of Python's standard library, providing a wide range of mathematical functions and constants. Below are comprehensive code examples for each functionality within the `math` module. These examples are designed to be clear, concise, and suitable for inclusion in official documentation.

### 1. **Trigonometric Functions**

```python
import math

# Calculate the sine of an angle (in radians)
angle = math.pi / 4
sine_value = math.sin(angle)
print(f"Sine of {angle} radians: {sine_value}")

# Calculate the cosine of an angle (in radians)
cosine_value = math.cos(angle)
print(f"Cosine of {angle} radians: {cosine_value}")

# Calculate the tangent of an angle (in radians)
tangent_value = math.tan(angle)
print(f"Tangent of {angle} radians: {tangent_value}")
```

### 2. **Logarithmic Functions**

```python
import math

# Calculate the natural logarithm of a number
x = 10
natural_log = math.log(x)
print(f"Natural logarithm of {x}: {natural_log}")

# Calculate the base-10 logarithm of a number
base_10_log = math.log10(x)
print(f"Base-10 logarithm of {x}: {base_10_log}")
```

### 3. **Exponential and Power Functions**

```python
import math

# Calculate e raised to the power of x
e_x = math.exp(1)  # This is equivalent to math.e ** x
print(f"e^1: {e_x}")

# Raise a number to the power of another number
base = 2
exponent = 3
result = base ** exponent
print(f"{base} raised to the power of {exponent}: {result}")
```

### 4. **Square Root and Floor/Ceiling Functions**

```python
import math

# Calculate the square root of a number
number = 16
sqrt_value = math.sqrt(number)
print(f"Square root of {number}: {sqrt_value}")

# Calculate the floor of a number (rounds down to the nearest integer)
x = 4.7
floor_value = math.floor(x)
print(f"Floor of {x}: {floor_value}")

# Calculate the ceiling of a number (rounds up to the nearest integer)
y = 4.2
ceiling_value = math.ceil(y)
print(f"Ceiling of {y}: {ceiling_value}")
```

### 5. **Constants**

```python
import math

# Access mathematical constants
pi = math.pi
e = math.e
inf = math.inf
nan = math.nan

print(f"Value of π: {pi}")
print(f"Value of e: {e}")
print(f"Infinity: {inf}")
print(f"Not a Number (NaN): {nan}")
```

### 6. **Rounding Functions**

```python
import math

# Round a number to the nearest integer
x = 4.75
rounded_value = round(x)
print(f"Rounded value of {x}: {rounded_value}")

# Round a number up to the nearest even integer (bankers' rounding)
y = 3.5
round_up_even = math.floor(y + 0.5) if y % 1 == 0.5 else math.ceil(y - 0.5)
print(f"Rounded up to nearest even integer of {y}: {round_up_even}")
```

### 7. **Factorial and Gamma Function**

```python
import math

# Calculate the factorial of a number
factorial_5 = math.factorial(5)
print(f"Factorial of 5: {factorial_5}")

# Calculate the gamma function (which is related to factorials for positive integers)
gamma_3 = math.gamma(3)
print(f"Gamma function of 3: {gamma_3}")
```

### 8. **Modular Arithmetic Functions**

```python
import math

# Calculate the greatest common divisor using Euclid's algorithm
a, b = 48, 18
gcd_value = math.gcd(a, b)
print(f"GCD of {a} and {b}: {gcd_value}")

# Calculate the least common multiple (LCM) using the formula LCM(x, y) = |x * y| / GCD(x, y)
lcm_value = abs(a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b}: {lcm_value}")
```

### 9. **Hyperbolic Functions**

```python
import math

# Calculate the hyperbolic sine of an angle (in radians)
hyperbolic_sine = math.sinh(1)
print(f"Hyperbolic sine of 1 radian: {hyperbolic_sine}")

# Calculate the hyperbolic cosine of an angle (in radians)
hyperbolic_cosine = math.cosh(1)
print(f"Hyperbolic cosine of 1 radian: {hyperbolic_cosine}")

# Calculate the hyperbolic tangent of an angle (in radians)
hyperbolic_tangent = math.tanh(1)
print(f"Hyperbolic tangent of 1 radian: {hyperbolic_tangent}")
```

### 10. **Error Functions and Complementary Error Function**

```python
import math

# Calculate the error function (erf) for a real argument x
x = 0.5
error_function_value = math.erf(x)
print(f"Error function of {x}: {error_function_value}")

# Calculate the complementary error function (erfc) for a real argument x
complementary_error_function_value = math.erfc(x)
print(f"Complementary error function of {x}: {complementary_error_function_value}")
```

### 11. **Constants and Special Values**

```python
import math

# Access special values defined in the math module
pi_over_4 = math.pi / 4
negative_zero = -0.0
inf_pos = math.inf
inf_neg = -math.inf
nan_val = math.nan

print(f"π/4: {pi_over_4}")
print(f"Negative zero: {negative_zero}")
print(f"Infinity (positive): {inf_pos}")
print(f"Infinity (negative): {inf_neg}")
print(f"Not a Number (NaN): {nan_val}")
```

### 12. **Pi and E Constants**

```python
import math

# Access the mathematical constants π and e
pi_value = math.pi
e_value = math.e

print(f"Value of π: {pi_value}")
print(f"Value of e: {e_value}")
```

These examples cover a wide range of functionalities provided by the `math` module, demonstrating how to use various mathematical operations effectively in Python. Each example includes comments explaining the purpose and usage of each function or constant, ensuring clarity for beginners and advanced users alike.
