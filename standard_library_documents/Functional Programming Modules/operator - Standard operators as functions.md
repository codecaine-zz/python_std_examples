# operator — Standard operators as functions

Here's an example of using the `operator` module in Python, which provides a comprehensive set of operators as functions:

```python
# Import the operator module
import operator

# Define variables for demonstration purposes
a = 10
b = 5
c = 20
d = 15

# Arithmetic Operators
print("Arithmetic Operators:")
# Add
add_result = operator.add(a, b)
print(f"add({a}, {b}) = {add_result}")

# Subtract
subtract_result = operator.sub(a, c)
print(f"sub({a}, {c}) = {subtract_result}")

# Multiply
multiply_result = operator.mul(a, d)
print(f"mul({a}, {d}) = {multiply_result}")

# Divide (Note: Division can be both integer and floating-point)
divide_result = operator.truediv(a, c)
print(f"truediv({a}, {c}) = {divide_result}")

# Modular Exponentiation
power_result = operator.pow(2, 3) # Using a constant for demonstration purposes
print(f"pow(2, 3) = {power_result}")
```

This example demonstrates how to use various operators from the `operator` module, including arithmetic and exponentiation operations.

Here's a brief explanation of each function:

- `operator.add(a, b)` - Adds two numbers.
- `operator.sub(a, b)` - Subtracts one number from another.
- `operator.mul(a, b)` - Multiplies two numbers.
- `operator.truediv(a, b)` - Divides one number by another (returns a float).
- `operator.pow(base, exponent)` - Calculates the power of `base` raised to `exponent`.

Here's an example with more operators and their usage:

```python
print("Other Operators:")
# Comparison Operators
is_greater_result = operator.gt(5, 3)
print(f"gt({5}, {3}) = {is_greater_result}")

# Equality Operator (True if both operands are equal)
is_equal_result = operator.eq(10, 10)
print(f"eq({10}, {10}) = {is_equal_result}")

# Inequality Operator
is_not_equal_result = operator.ne(10, 5)
print(f"ne({10}, {5}) = {is_not_equal_result}")

# Membership Operators
is_member_result = 2 in [1, 2, 3]
print(f"in({2}, [1, 2, 3]) = {is_member_result}")

# Bitwise operators

# AND operator
and_result = operator.and_(5, 8)
print(f"and(5, 8) = {and_result}")

# OR operator
or_result = operator.or_(5, 8)
print(f"or(5, 8) = {or_result}")

# XOR operator
xor_result = operator.xor(5, 8)
print(f"xor(5, 8) = {xor_result}")
```

This example demonstrates how to use comparison operators (`gt`, `eq`, `ne`), membership operators (`in`), and bitwise operators (`and_`, `or_`, `xor_`).
