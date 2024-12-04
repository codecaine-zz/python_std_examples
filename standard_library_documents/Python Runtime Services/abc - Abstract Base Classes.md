# abc — Abstract Base Classes

**Abstract Base Classes (ABC) Module**
=====================================

The `abc` module provides support for defining abstract base classes, which are classes that cannot be instantiated and must be subclassed by other classes.

### Importing the ABC Module
```python
import abc
```

### Defining an Abstract Class
```python
# Define a new class using the abc class
class Shape(abc.ABC):
    # The __abstractmethods__ attribute will be populated with abstract methods
    @property
    @abc.abstractmethod
    def area(self):
        """Return the area of the shape"""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape"""
        pass
```

### Implementing an Abstract Method
```python
# Define a concrete class that implements the abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * 3.14 * self.radius
```

### Checking for Abstract Methods
```python
try:
    # Attempt to instantiate the abstract class
    obj = Shape()
except TypeError as e:
    print(e)
# Output: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Attempt to get the abstract method without subclassing it
print(Shape.area)  # Output: <class 'abc.abstractmethod'>
```

### Registering Abstract Base Classes
```python
import abc

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    pass
```

### Checking for Singleton Classes
```python
print(Logger.__instance_count)  # Output: 1
```

### Creating a Metaclass
```python
import abc

def singleton(cls):
    cls._ instances = {}
    def wrapper(*args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    return wrapper

class Logger(metaclass=singleton):
    pass
```

### Checking for Singleton Classes (again)
```python
print(Logger.__instance_count)  # Output: 1
```

### Using `issubclass`
```python
# Check if Circle is a subclass of Shape
print(issubclass(Circle, Shape))  # Output: True

# Check if int is a subclass of Circle
print(issubclass(int, Circle))  # Output: False
```
