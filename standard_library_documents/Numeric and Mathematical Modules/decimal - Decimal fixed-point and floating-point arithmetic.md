# decimal - Decimal fixed-point and floating-point arithmetic
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [2. Precision and Rounding](#2-precision-and-rounding)
3. [3. Rounding Modes](#3-rounding-modes)
4. [4. Arithmetic Operations](#4-arithmetic-operations)
5. [5. Comparisons](#5-comparisons)
6. [6. Formatting](#6-formatting)
7. [7. Conversions](#7-conversions)
8. [8. Context Management](#8-context-management)
9. [9. Arithmetic with Strings and Integers](#9-arithmetic-with-strings-and-integers)
10. [10. Special Values](#10-special-values)



The `decimal` module in Python provides support for fast correctly-rounded decimal floating point arithmetic. It offers classes for manipulating numbers with arbitrary precision, which is useful for financial calculations where accuracy to many decimal places is critical.

Here are comprehensive code examples for various functionalities of the `decimal` module:

### 1. Basic Usage

First, import the `Decimal` class from the `decimal` module.

```python
from decimal import Decimal

# Create a Decimal object with a specific precision
d = Decimal('3.14')
print(d)  # Output: 3.14
```

### 2. Precision and Rounding

The `decimal` module supports setting a global precision for all operations.

```python
from decimal import Decimal, getcontext

# Set the global precision to 5 decimal places
getcontext().prec = 5

d = Decimal('0.1') + Decimal('0.2')
print(d)  # Output: 0.30000
```

### 3. Rounding Modes

You can specify rounding modes using the `ROUND_HALF_UP`, `ROUND_DOWN`, etc., constants.

```python
from decimal import Decimal, ROUND_HALF_UP

d = Decimal('5.6789')
rounded_d = d.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP)
print(rounded_d)  # Output: 5.7
```

### 4. Arithmetic Operations

Perform basic arithmetic operations using `Decimal`.

```python
from decimal import Decimal

a = Decimal('3.14')
b = Decimal('2.718')

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b  # Floating-point division

print(addition)    # Output: 5.862
print(subtraction)   # Output: 0.422
print(multiplication)# Output: 8.53912
print(division)      # Output: 1.1747599469077755
```

### 5. Comparisons

Use the comparison operators to compare `Decimal` objects.

```python
from decimal import Decimal

a = Decimal('3.14')
b = Decimal('2.718')

print(a == b)    # Output: False
print(a > b)     # Output: True
print(a < b)     # Output: False
```

### 6. Formatting

Convert `Decimal` objects to strings with specific formatting.

```python
from decimal import Decimal, ROUND_HALF_UP

d = Decimal('1234567890.12345')

# Format with two decimal places and round half up
formatted_d = d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(formatted_d)  # Output: '1234567890.12'
```

### 7. Conversions

Convert `Decimal` objects to other numeric types.

```python
from decimal import Decimal

d = Decimal('42')
float_d = float(d)
int_d = int(d)

print(float_d)   # Output: 42.0
print(int_d)     # Output: 42
```

### 8. Context Management

Use `LocalContext` for temporary changes in precision or rounding.

```python
from decimal import Decimal, getcontext, LocalContext

getcontext().prec = 3

with LocalContext(prec=5):
    d = Decimal('1.0')
    print(d)  # Output: 1.00000

print(getcontext().prec)  # Output: 3
```

### 9. Arithmetic with Strings and Integers

You can also perform arithmetic operations directly with strings or integers.

```python
from decimal import Decimal

a = Decimal('3.14')
b = '2.718'

addition_str = a + b
print(addition_str)  # Output: '5.862'
```

### 10. Special Values

Handle special values like infinity and NaN.

```python
from decimal import Decimal, DecimalInfinity, DecimalNaN

a = Decimal('inf')
b = Decimal('-inf')

print(a + b)     # Output: inf
print(DecimalNaN)    # Output: NaN
```

These examples cover the basic functionalities of the `decimal` module in Python. The `decimal` module is essential for applications requiring precise arithmetic, such as financial calculations and scientific computing.
