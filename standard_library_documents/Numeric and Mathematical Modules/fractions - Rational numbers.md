# fractions - Rational numbers

The `fractions` module in Python provides support for rational number arithmetic. Here are comprehensive and well-documented code examples that cover various functionalities within this module:

```python
import fractions

# Creating Rational Numbers

# Using constructor
num1 = fractions.Fraction(3, 4)  # Represents the fraction 3/4
num2 = fractions.Fraction(5, 6)  # Represents the fraction 5/6

print(num1)        # Output: 3/4
print(num2)        # Output: 5/6

# From integers
num3 = fractions.Fraction(7)   # Equivalent to Fraction(7, 1)
print(num3)        # Output: 7/1

# Using string input
num4 = fractions.Fraction('3/4')  # Represents the fraction 3/4
print(num4)        # Output: 3/4

# Converting a float to a Fraction
num5 = fractions.Fraction(0.75)
print(num5)        # Output: 3/4

# Using mixed numbers
mixed_num = fractions.Fraction(3, 2)  # Represents the fraction 3/2
print(mixed_num)     # Output: 3/2

# Arithmetic Operations

# Addition
result_add = num1 + num2
print(result_add)   # Output: 17/12

# Subtraction
result_subtract = num1 - num2
print(result_subtract) # Output: -1/12

# Multiplication
result_multiply = num1 * num2
print(result_multiply) # Output: 5/24

# Division
result_divide = num1 / num2
print(result_divide)   # Output: 3/10

# Exponentiation
result_power = num1 ** 2
print(result_power)    # Output: 9/16

# Comparison Operators

# Equality
if num1 == num3:
    print("num1 is equal to num3")
else:
    print("num1 is not equal to num3")

# Inequality
if num1 != num4:
    print("num1 is not equal to num4")
else:
    print("num1 is equal to num4")

# Less than
if num1 < num2:
    print("num1 is less than num2")
else:
    print("num1 is not less than num2")

# Greater than
if num1 > num3:
    print("num1 is greater than num3")
else:
    print("num1 is not greater than num3")

# Less than or equal to
if num1 <= num2:
    print("num1 is less than or equal to num2")
else:
    print("num1 is not less than or equal to num2")

# Greater than or equal to
if num1 >= num4:
    print("num1 is greater than or equal to num4")
else:
    print("num1 is not greater than or equal to num4")

# Converting to float and int

float_num = float(num5)
print(float_num)      # Output: 0.75

int_num = int(num3)
print(int_num)       # Output: 7

# Absolute value
abs_value = abs(fractions.Fraction(-2, 3))
print(abs_value)     # Output: 2/3

# Converting to string
str_num = str(num1)
print(str_num)      # Output: '3/4'

# Fraction representation in decimal format
decimal_repr = num1.limit_denominator()
print(decimal_repr)   # Output: 0.75

# Numerator and Denominator
numerator = fractions.Fraction(8, 6).numerator
denominator = fractions.Fraction(8, 6).denominator
print(numerator)    # Output: 4
print(denominator)   # Output: 3

# Simplifying a fraction
simplified_num = fractions.Fraction(10, 25)
simplified_num = simplified_num.limit_denominator()
print(simplified_num)   # Output: 2/5

# Operations with Infinite Fractions
inf_frac = float('inf')  # Represents Infinity
zero_frac = fractions.Fraction(0)  # Represents Zero

print(inf_frac + inf_frac)      # Output: Infinity
print(zero_frac - inf_frac)    # Output: -Infinity
```

### Explanation:

1. **Creating Rational Numbers**: The `Fraction` class is used to create rational numbers from integers, floats, strings, or mixed number representations.

2. **Arithmetic Operations**: Basic arithmetic operations like addition, subtraction, multiplication, and division are supported, along with exponentiation.

3. **Comparison Operators**: Functions like `==`, `!=`, `<`, `>`, `<=`, and `>=` are used to compare fractions.

4. **Conversions**:
   - To float: Use the `float()` function.
   - To integer: Use the `int()` function.
   - To string: Use the `str()` function.

5. **Absolute Value**: The `abs()` function returns the absolute value of a fraction.

6. **Fraction Representation in Decimal Format**: The `limit_denominator()` method is used to simplify the fraction and convert it to a float, which represents the decimal equivalent.

7. **Numerator and Denominator**: Use the `numerator` and `denominator` attributes to access these properties of a fraction.

8. **Simplifying Fractions**: Use the `limit_denominator()` method to reduce fractions to their simplest form.

9. **Operations with Infinite Fractions**: Special representations like 'Infinity' and 'Zero' are supported for operations involving infinite or zero values.

These examples provide a comprehensive overview of how to use the `fractions` module in Python, covering various aspects of rational number arithmetic.
