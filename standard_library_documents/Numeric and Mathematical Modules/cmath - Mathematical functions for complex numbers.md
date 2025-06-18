# cmath - Mathematical functions for complex numbers
## Table of Contents

1. [Explanation:](#explanation)



Below is a comprehensive set of example code snippets demonstrating various functionalities available in the `cmath` module, which provides mathematical functions for complex numbers in Python 3.12.

```python
import cmath

# Example 1: Basic Complex Number Operations
# Create a complex number using the constructor
z = complex(3, 4)
print(f"Complex number z: {z}")

# Convert real and imaginary parts separately
real_part = z.real
imaginary_part = z.imag
print(f"Real part: {real_part}, Imaginary part: {imaginary_part}")

# Add two complex numbers
w = complex(1, 2)
result_addition = z + w
print(f"Addition of z and w: {result_addition}")

# Subtract one complex number from another
result_subtraction = z - w
print(f"Subtraction of w from z: {result_subtraction}")

# Multiply two complex numbers
result_multiplication = z * w
print(f"Multiplication of z and w: {result_multiplication}")

# Divide one complex number by another
result_division = z / w
print(f"Division of z by w: {result_division}")

# Example 2: Absolute Value and Phase of a Complex Number
abs_z = abs(z)
phase_z = cmath.phase(z)
print(f"Absolute value of z: {abs_z}, Phase (angle in radians): {phase_z}")

# Example 3: Polar and Rectangular Representation
polar_representation = cmath.polar(z)
rectangular_representation = cmath.rect(abs_z, phase_z)
print(f"Polar representation (r, theta): {polar_representation}")
print(f"Rectangular representation (x, y): {rectangular_representation}")

# Example 4: Square Root of a Complex Number
sqrt_z = cmath.sqrt(z)
print(f"Square root of z: {sqrt_z}")

# Example 5: Exponential and Logarithmic Functions for Complex Numbers
exp_z = cmath.exp(z)
log_z = cmath.log(z)
print(f"Exponent of z: {exp_z}")
print(f"Natural logarithm of z: {log_z}")

# Example 6: Trigonometric and Hyperbolic Functions for Complex Numbers
sin_z = cmath.sin(z)
cos_z = cmath.cos(z)
tan_z = cmath.tan(z)

asinh_z = cmath.asinh(z)
acosh_z = cmath.acosh(z)
atanh_z = cmath.atanh(z)

print(f"Trigonometric functions: sin({z})={sin_z}, cos({z})={cos_z}, tan({z})={tan_z}")
print(f"Inverse hyperbolic trigonometric functions: asinh({z})={asinh_z}, acosh({z})={acosh_z}, atanh({z})={atanh_z}")

# Example 7: Roots of a Quadratic Equation
a = 1
b = -3
c = 2

roots = cmath.sqrt(b**2 - 4*a*c)
root1 = (-b + roots) / (2 * a)
root2 = (-b - roots) / (2 * a)

print(f"Roots of the quadratic equation ax^2 + bx + c = 0: {root1}, {root2}")

# Example 8: Roots of Unity
n = 5  # Number of roots
roots_of_unity = [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
print(f"Roots of unity (for n={n}): {roots_of_unity}")

# Example 9: Complex Conjugate
conjugate_z = z.conjugate()
print(f"Conjugate of z: {conjugate_z}")

# Example 10: Check if a complex number is real or imaginary
if conjugate_z == z:
    print("z is a real number")
elif z.imag != 0:
    print("z is an imaginary number")
else:
    print("z is zero")

# Example 11: Check if a complex number is purely imaginary
if z.real == 0:
    print("z is purely imaginary")
else:
    print("z is not purely imaginary")

# Example 12: Complex Number Exponentiation with Euler's Formula
euler_formula_result = cmath.exp(z)
print(f"Exponential of z using Euler's formula: {euler_formula_result}")
```

### Explanation:

- **Basic Operations**: Demonstrates addition, subtraction, multiplication, and division of complex numbers.
- **Absolute Value and Phase**: Shows how to compute the magnitude and angle (phase) of a complex number.
- **Polar and Rectangular Representation**: Converts between polar and rectangular coordinates.
- **Square Root**: Computes the square root of a complex number.
- **Exponential and Logarithmic Functions**: Demonstrates exponential and logarithmic operations on complex numbers.
- **Trigonometric and Hyperbolic Functions**: Includes sine, cosine, tangent, and their inverse functions for complex numbers.
- **Quadratic Equation Roots**: Uses the quadratic formula to find roots of a complex equation.
- **Roots of Unity**: Computes all `n`th roots of unity for a given integer `n`.
- **Complex Conjugate**: Shows how to obtain the conjugate of a complex number.
- **Real or Imaginary Check**: Determines if a complex number is real, purely imaginary, or zero.

These examples cover a range of operations and properties available in the `cmath` module, providing comprehensive understanding of its functionalities.
