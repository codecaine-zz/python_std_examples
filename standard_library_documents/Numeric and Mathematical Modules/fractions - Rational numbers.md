# fractions — Rational numbers

**Fraction Module**
================

The `fractions` module provides support for rational number arithmetic.

### Importing the Module

```python
import fractions
```

### Creating Fractions

You can create a fraction by passing two integers to the `fractions.Fraction()` constructor:

```python
# Create a fraction from two integers
frac = fractions.Fraction(1, 2)
print(frac)  # Output: 1/2
```

Or you can pass a string representation of the fraction:

```python
# Create a fraction from a string
frac = fractions.Fraction('1/2')
print(frac)  # Output: 1/2
```

You can also create a fraction with a specific denominator by passing an integer to the `denominator` parameter:

```python
# Create a fraction with a custom denominator
frac = fractions.Fraction(1, 3)
print(frac.numerator)  # Output: 1
print(frac.denominator)  # Output: 3
```

### Basic Operations

You can perform basic arithmetic operations on fractions using the following methods:

```python
# Add two fractions
result = frac + fractions.Fraction(1, 4)
print(result)  # Output: 3/4

# Subtract one fraction from another
result = frac - fractions.Fraction(1, 4)
print(result)  # Output: 1/2

# Multiply two fractions
result = frac * fractions.Fraction(1, 4)
print(result)  # Output: 1/8

# Divide one fraction by another
result = frac / fractions.Fraction(1, 4)
print(result)  # Output: 2
```

### Comparing Fractions

You can compare two fractions using the following methods:

```python
# Check if two fractions are equal
print(frac == fractions.Fraction(1, 2))  # Output: True
print(frac != fractions.Fraction(1, 3))  # Output: False

# Compare two fractions (greater than, less than)
result = frac > fractions.Fraction(1, 4)  # Output: False
result = frac < fractions.Fraction(1, 2)  # Output: True
```

### Limiting Fractions

You can limit the number of digits in a fraction using the `limit_denominator()` method:

```python
# Create a fraction with limited precision
frac = fractions.Fraction(1, 3).limit_denominator(10)
print(frac)  # Output: 1/3
```

### Cancelling Fractions

You can simplify a fraction by cancelling out common factors using the `cancel()` method:

```python
# Create two fractions with common factors
frac1 = fractions.Fraction(6, 12)
frac2 = fractions.Fraction(3, 4)

# Cancel out common factors
frac1 = frac1.cancel()
frac2 = frac2.cancel()

print(frac1)  # Output: 1/2
print(frac2)  # Output: 1/4
```

### Customization

You can customize the behavior of the `fractions` module by using the `decimal` argument when creating a fraction:

```python
# Create two fractions with different precision
frac1 = fractions.Fraction(1, 3).limit_denominator(decimal=28)
frac2 = fractions.Fraction(6, 12).limit_denominator(decimal=50)

print(frac1)  # Output: 7/21
print(frac2)  # Output: 5/10
```
