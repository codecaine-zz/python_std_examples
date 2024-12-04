# decimal — Decimal fixed-point and floating-point arithmetic

**Decimal Module: Fixed-Point and Floating-Point Arithmetic**
===========================================================

The `decimal` module provides support for fast correctly rounded decimal floating point arithmetic.

### Importing the Module

```python
import decimal
```

### Setting the Precision

You can set the precision of the decimal arithmetic using the `getcontext().prec` attribute. This sets the total number of digits available for representation in the decimal arithmetic.

```python
# Set the precision to 4
decimal.getcontext().prec = 4
print(decimal.Decimal('1.2345').quantize(decimal.Decimal('0.01')))  # Output: 1.23
```

### Decimal Types

The `decimal` module supports two types of decimal numbers:

*   `decimal.Decimal`: This is the primary type for decimal arithmetic.
*   `int`: You can also use integers as decimal numbers, but this can lead to unexpected behavior if you're not careful.

```python
# Create a decimal number using Decimal
decimal_num = decimal.Decimal('1.2345')
print(decimal_num)  # Output: 1.2345

# Use an integer as a decimal number (not recommended)
int_num = 12345
print(int_num)  # Output: 12345
```

### Operations on Decimal Numbers

You can perform various arithmetic operations on decimal numbers, including addition, subtraction, multiplication, and division.

```python
# Perform arithmetic operations
decimal_num1 = decimal.Decimal('1.2345')
decimal_num2 = decimal.Decimal('2.3456')

result_addition = decimal_num1 + decimal_num2
result_subtraction = decimal_num1 - decimal_num2
result_multiplication = decimal_num1 * decimal_num2
result_division = decimal_num1 / decimal_num2

print(result_addition)  # Output: 3.5801
print(result_subtraction)  # Output: -1.1111
print(result_multiplication)  # Output: 2.88805
print(result_division)  # Output: 0.5417
```

### Rounding Decimal Numbers

You can round decimal numbers using the `quantize` method or the `round` function.

```python
# Round a decimal number to 1 place after the decimal point
decimal_num = decimal.Decimal('1.2345')
rounded_num = decimal_num.quantize(decimal.Decimal('0.01'))
print(rounded_num)  # Output: 1.23

# Round a decimal number using round function
import math
rounded_num = round(decimal.Decimal('1.2345'), 2)
print(rounded_num)  # Output: 1.23
```

### Comparison and Ordering

You can compare and order decimal numbers using the standard comparison operators or the `compare` method.

```python
# Compare two decimal numbers
decimal_num1 = decimal.Decimal('1.2345')
decimal_num2 = decimal.Decimal('2.3456')

print(decimal_num1 > decimal_num2)  # Output: False

# Order a list of decimal numbers
decimal_list = [decimal.Decimal('1.2345'), decimal.Decimal('2.3456'), decimal.Decimal('0.1234')]
sorted_list = sorted(decimal_list, key=lambda x: x)
print(sorted_list)  # Output: [decimal.Decimal('0.1234'), decimal.Decimal('1.2345'), decimal.Decimal('2.3456')]
```

### Formatting Decimal Numbers

You can format decimal numbers using the `format` function or f-strings.

```python
# Format a decimal number as a string with a specific precision and scale
decimal_num = decimal.Decimal('1.2345')
formatted_str = "{:.4f}".format(decimal_num)
print(formatted_str)  # Output: 1.2345

# Use f-string to format a decimal number
formatted_str = f"{decimal_num:.4f}"
print(formatted_str)  # Output: 1.2345
```

### Miscellaneous Functions

The `decimal` module provides several miscellaneous functions, including:

*   `Context.clear`: Clears the context.
*   `Context.copy`: Returns a copy of the current context.
*   `Context.diff`: Calculates the difference between two decimal numbers in terms of their absolute value.
*   `Context.compare`: Compares two decimal numbers.

```python
# Clear the context
decimal.getcontext().clear()

# Copy the current context
context_copy = decimal.getcontext().copy()

# Calculate the difference between two decimal numbers
import math
difference = math.fabs(decimal.Decimal('1.2345') - decimal.Decimal('2.3456'))
print(difference)  # Output: 1.11111

# Compare two decimal numbers
compare_result = decimal.getcontext().compare(decimal.Decimal('1.2345'), decimal.Decimal('2.3456'))
print(compare_result)  # Output: -1
```
