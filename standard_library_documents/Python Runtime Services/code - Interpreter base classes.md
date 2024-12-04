# code — Interpreter base classes

**Interpreter Base Classes**
=====================================

The `abc` (Abstract Base Classes) module in Python provides a way to define abstract base classes, which are classes that cannot be instantiated and must be subclassed by concrete classes.

Here's an example of how you can use the `abc` module:

```python
# Import the ABC class from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class called 'Shape'
class Shape(ABC):
    """
    Abstract base class for shapes.
    
    This class cannot be instantiated directly and must be subclassed by concrete classes.
    """

    # The __abstractmethods__ attribute is automatically set to a list of methods
    # that are declared but not implemented in the abstract base class.
    @property
    def __abstractmethods__(self):
        return []

    # Declare an abstract method called 'area' that must be implemented by subclasses.
    @abstractmethod
    def area(self):
        """
        Calculate the area of this shape.

        This method must be implemented by concrete subclasses of Shape.
        """

    # Define a method called 'perimeter' that can be overridden by subclasses.
    def perimeter(self):
        """
        Calculate the perimeter of this shape.

        The default implementation returns 0, but concrete subclasses
        can override this to provide their own implementation.
        """

# Create a concrete subclass of Shape called 'Circle'
class Circle(Shape):
    """
    Concrete subclass of Shape for circles.
    """

    # Initialize the circle with its radius
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method by calculating the area using the formula πr^2
    def area(self):
        import math
        return math.pi * (self.radius ** 2)

# Create a concrete subclass of Shape called 'Rectangle'
class Rectangle(Shape):
    """
    Concrete subclass of Shape for rectangles.
    """

    # Initialize the rectangle with its width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method by calculating the area using the formula w*h
    def area(self):
        return self.width * self.height

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the areas of the shapes
print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")

# Attempt to instantiate Shape directly (this will raise an error)
try:
    shape = Shape()
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Shape with abstract methods area
```

This code demonstrates how you can define and use abstract base classes, including using the `@abstractmethod` decorator to declare abstract methods and implementing those methods in concrete subclasses.
