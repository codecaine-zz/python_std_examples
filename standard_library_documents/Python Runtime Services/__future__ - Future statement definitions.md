# __future__ — Future statement definitions

Here's an example of how to use the `__future__.nested_scopes` feature, which was added in Python 2.1:

```python
from __future__ import nested_scopes

# Define a function that uses nested scopes
def outer_function():
    """
    This function demonstrates the use of nested scopes with the __future__.nested_scopes feature.
    
    In Python 2.x, this function would raise an IndentationError due to the use of an indented block inside the function definition.
    """
    # Inner function that uses nested scopes
    def inner_function():
        """
        This inner function demonstrates the correct usage of nested scopes in Python 3.x.
        
        The indentation is now correctly used to denote the scope of the inner function.
        """
        print("Inner function called")
    
    # Call the inner function
    inner_function()

# Call the outer function
outer_function()
```

To use the `__future__.annotations` feature, which was added in Python 2.6:

```python
from __future__ import annotations

class Person:
    """
    This class demonstrates the use of type hints and annotations.
    
    In Python 3.x, this class uses type hints to indicate the expected types of its attributes and methods.
    """

    def __init__(self, name: str, age: int):
        """
        Initializes a new instance of the Person class.
        
        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age

    def greet(self) -> None:
        """
        Prints out a greeting message with the person's name.
        
        Returns:
            None
        """
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person = Person("John Doe", 30)

# Call the greet method
person.greet()
```

To use the `__future__.division` feature, which was added in Python 2.6:

```python
from __future__ import division

def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    # Use the / operator for true division
    return 3.14 * radius ** 2 / 4

# Call the calculate_area function
radius = 5.0
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
```

To use the `__future__.generators` feature, which was added in Python 2.3:

```python
from __future__ import generators

# Define a generator function
def fibonacci(n: int) -> int:
    """
    Generates the first n numbers in the Fibonacci sequence.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Yields:
        int: The next number in the Fibonacci sequence.
    """
    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    
    for _ in range(n):
        yield a
        a, b = b, a + b

# Call the fibonacci function
for num in fibonacci(10):
    print(num)
```

To use the `__future__.print_function` feature, which was added in Python 2.6:

```python
from __future__ import print_function

def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    # Use the print function with parentheses
    print("The sum of {} and {} is {}".format(a, b, a + b))

# Call the add function
add(2, 3)
```

To use the `__future__.unicode_literals` feature, which was added in Python 2.1:

```python
from __future__ import unicode_literals

def greet(name: str) -> None:
    """
    Prints out a greeting message with the person's name.
    
    Args:
        name (str): The person's name.
    """
    # Use Unicode literals
    print("Hello, {}".format(name))

# Call the greet function
greet(u"John Doe")
```

To use the `__future__.absolute_import` feature, which was added in Python 2.5:

```python
from __future__ import absolute_import

import math

def calculate_square_root(n: int) -> float:
    """
    Calculates the square root of a number.
    
    Args:
        n (int): The number to find the square root of.
    
    Returns:
        float: The square root of the number.
    """
    # Use absolute imports
    from math import sqrt
    
    return sqrt(n)

# Call the calculate_square_root function
n = 16
result = calculate_square_root(n)
print(f"The square root of {n} is {result:.2f}")
```

To use the `__future__.division` feature (again, because it's different in Python 3.x):

```python
from __future__ import division

def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    # Use the / operator for true division
    return 3.14 * radius ** 2 / 4

# Call the calculate_area function
radius = 5.0
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
```

To use the `__future__.nested_scopes` feature (again, because it's different in Python 3.x):

```python
from __future__ import nested_scopes

def outer_function():
    """
    This function demonstrates the use of nested scopes with the __future__.nested_scopes feature.
    
    In Python 2.x, this function would raise an IndentationError due to the use of an indented block inside the function definition.
    """
    # Inner function that uses nested scopes
    def inner_function():
        """
        This inner function demonstrates the correct usage of nested scopes in Python 3.x.
        
        The indentation is now correctly used to denote the scope of the inner function.
        """
        print("Inner function called")
    
    # Call the inner function
    inner_function()

# Call the outer function
outer_function()
```
