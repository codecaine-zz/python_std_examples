# cmath — Mathematical functions for complex numbers

**cmath Module Documentation**
================================

The `cmath` module provides functions to handle complex numbers.

### Importing the Module

```python
import cmath
```

### Functions

#### 1. `cmath.exp(x)`

Computes the exponential function of a complex number.

```python
# Example usage:
result = cmath.exp(2 + 3j)
print(result)
```

#### 2. `cmath.log(x)`

Computes the natural logarithm of a positive real number or the complex logarithm of a complex number.

```python
# Example usage:
result = cmath.log(10)
print(result)

# Complex logarithm example:
complex_result = cmath.log(16 + 8j)
print(complex_result)
```

#### 3. `cmath.sqrt(x)`

Computes the square root of a positive real number or the complex square root of a complex number.

```python
# Example usage:
real_sqrt = cmath.sqrt(9)
complex_sqrt = cmath.sqrt(16 + 8j)
print(real_sqrt, complex_sqrt)
```

#### 4. `cmath.polar(x)`

Returns the polar form of a complex number.

```python
import math

# Example usage:
result = cmath.polar(10 + 2j)
r, phi = result
print(f'r = {r}, phi = {phi}')

# Convert back to rectangular form:
rectangular_form = cmath.rect(r, phi)
print(rectangular_form)
```

#### 5. `cmath.phase(x)`

Returns the phase of a complex number.

```python
# Example usage:
result = cmath.phase(10 + 2j)
print(result)

# Note: This function is not always defined for all real numbers.
# It raises a ValueError if the input is zero or negative.
```

#### 6. `cmath.rect(r, phi)`

Returns the rectangular form of a complex number.

```python
import math

# Example usage:
result = cmath.rect(10, math.pi / 2)
print(result)

# Note: This function is not always defined for all real numbers.
# It raises a ValueError if r <= 0 or pi/2 < phi + 2*pi*n < 3*pi/2.
```

#### 7. `cmath.isclose(x, y)` and `cmath.isfinite(x)`, etc.

These functions check whether two numbers are close to each other or finite, respectively.

```python
# Example usage:
import math

x = cmath.sqrt(-4)
print(cmath.isclose(x, -2))  # Returns True due to floating-point errors.
print(math.isfinite(x))      # Returns False.
```

### Constants

#### `cmath.pi` and `cmath.e`

Constants for pi and e.

```python
import math

# Example usage:
result = cmath.pi / (1 + cmath.sqrt(-3))
print(result)

result = cmath.e ** 2
print(result)
```
