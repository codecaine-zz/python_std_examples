# numbers - Numeric abstract base classes

The `numbers` module in Python provides an abstract base class hierarchy for numeric types, which can serve as a foundation for creating custom numeric types. Here are comprehensive examples demonstrating various functionalities provided by this module:

```python
from abc import ABCMeta, abstractmethod

# Define the Number class
class Number(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __floordiv__(self, other):
        pass

    @abstractmethod
    def __mod__(self, other):
        pass

    @abstractmethod
    def __pow__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __ne__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @abstractmethod
    def __neg__(self):
        pass

    @abstractmethod
    def __abs__(self):
        pass

# Define the Real class, which is a subclass of Number
class Real(Number):
    @abstractmethod
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Real(self.value + other)

    def __sub__(self, other):
        return Real(self.value - other)

    def __mul__(self, other):
        return Real(self.value * other)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Real(self.value / other)

    def __floordiv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        return Real(self.value // other)

    def __mod__(self, other):
        if other == 0:
            raise ZeroDivisionError("modulo by zero")
        return Real(self.value % other)

    def __pow__(self, other):
        return Real(pow(self.value, other))

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __neg__(self):
        return Real(-self.value)

    def __abs__(self):
        return Real(abs(self.value))

# Define the Complex class, which is a subclass of Number
class Complex(Number):
    @abstractmethod
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Real):
            return Complex(self.real + other.value, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("unsupported operand type(s) for +: 'Complex' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Real):
            return Complex(self.real - other.value, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("unsupported operand type(s) for -: 'Complex' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Real):
            return Complex(self.real * other.value, self.imag * other.value)
        elif isinstance(other, Complex):
            r = self.real * other.real - self.imag * other.imag
            i = self.real * other.imag + self.imag * other.real
            return Complex(r, i)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Complex' and '{}'".format(type(other).__name__))

    def __truediv__(self, other):
        if isinstance(other, Real):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            r = self.real / other
            i = self.imag / other
            return Complex(r, i)
        elif isinstance(other, Complex):
            denom = pow(other.real, 2) + pow(other.imag, 2)
            r = (self.real * other.real + self.imag * other.imag) / denom
            i = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(r, i)
        else:
            raise TypeError("unsupported operand type(s) for /: 'Complex' and '{}'".format(type(other).__name__))

    def __floordiv__(self, other):
        if isinstance(other, Real):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            r = self.real // other
            i = self.imag // other
            return Complex(r, i)
        elif isinstance(other, Complex):
            denom = pow(other.real, 2) + pow(other.imag, 2)
            r = (self.real * other.real + self.imag * other.imag) // denom
            i = (self.imag * other.real - self.real * other.imag) // denom
            return Complex(r, i)
        else:
            raise TypeError("unsupported operand type(s) for //: 'Complex' and '{}'".format(type(other).__name__))

    def __mod__(self, other):
        if isinstance(other, Real):
            if other == 0:
                raise ZeroDivisionError("modulo by zero")
            return Complex(self.real % other)
        elif isinstance(other, Complex):
            raise TypeError("unsupported operand type(s) for %: 'Complex' and '{}'".format(type(other).__name__))
        else:
            raise TypeError("unsupported operand type(s) for %: 'Complex' and '{}'".format(type(other).__name__))

    def __pow__(self, other):
        if isinstance(other, Real):
            return Complex(pow(self.real, other), pow(self.imag, other))
        elif isinstance(other, Complex):
            r = pow(pow(self.real, 2) + pow(self.imag, 2), other.real)
            i = (other.real * log(pow(self.real, 2) + pow(self.imag, 2))) * exp(log(abs(self)) * other.imag / 2)
            return Complex(r, i)
        else:
            raise TypeError("unsupported operand type(s) for **: 'Complex' and '{}'".format(type(other).__name__))

    def __lt__(self, other):
        if isinstance(other, Real):
            return abs(self) < abs(other)
        elif isinstance(other, Complex):
            return abs(self) < abs(other)
        else:
            raise TypeError("unsupported operand type(s) for <: 'Complex' and '{}'".format(type(other).__name__))

    def __le__(self, other):
        if isinstance(other, Real):
            return abs(self) <= abs(other)
        elif isinstance(other, Complex):
            return abs(self) <= abs(other)
        else:
            raise TypeError("unsupported operand type(s) for <=: 'Complex' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Real):
            return self.real == other.value and self.imag == 0
        elif isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        else:
            raise TypeError("unsupported operand type(s) for ==: 'Complex' and '{}'".format(type(other).__name__))

    def __ne__(self, other):
        if isinstance(other, Real):
            return self.real != other.value or self.imag != 0
        elif isinstance(other, Complex):
            return self.real != other.real or self.imag != other.imag
        else:
            raise TypeError("unsupported operand type(s) for !=: 'Complex' and '{}'".format(type(other).__name__))

    def __gt__(self, other):
        if isinstance(other, Real):
            return abs(self) > abs(other)
        elif isinstance(other, Complex):
            return abs(self) > abs(other)
        else:
            raise TypeError("unsupported operand type(s) for >: 'Complex' and '{}'".format(type(other).__name__))

    def __ge__(self, other):
        if isinstance(other, Real):
            return abs(self) >= abs(other)
        elif isinstance(other, Complex):
            return abs(self) >= abs(other)
        else:
            raise TypeError("unsupported operand type(s) for >=: 'Complex' and '{}'".format(type(other).__name__))

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __abs__(self):
        return sqrt(pow(self.real, 2) + pow(self.imag, 2))

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
c1 = Complex(3, 4)
c2 = Complex(1, 2)

print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 14i
```

This implementation provides basic complex number operations such as addition, multiplication, and comparison. Note that this is a simple example and does not include all the methods required by the `complex` class in Python. You might want to extend it to handle more features or optimizations depending on your needs. In real-world applications, you would typically use Python's built-in `complex` class for complex number operations.
