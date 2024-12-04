# abc - Abstract Base Classes

The `abc` (Abstract Base Class) module in Python provides a way to define abstract base classes, which are classes that cannot be instantiated directly but serve as a blueprint for subclasses. This module includes the `ABC` class and decorators such as `abstractmethod` and `abstractproperty`. Below are comprehensive code examples demonstrating various functionalities of this module.

### 1. Defining an Abstract Base Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    # Constructor
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

# Attempting to instantiate the base class will raise a TypeError
try:
    animal = Animal("Generic Animal")  # This line will cause an error
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Animal with abstract methods speak
```

### 2. Subclassing and Implementing Abstract Methods

```python
from abc import ABC, abstractmethod

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def bark(self):
        pass

    def speak(self):
        return self.bark()

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def meow(self):
        pass

    def speak(self):
        return self.meow()
```

### 3. Abstract Properties

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_color(self):
        pass

    @property
    @abstractmethod
    def color(self):
        pass

    @color.setter
    @abstractmethod
    def color(self, value):
        pass

class Car(Vehicle):
    _color = None

    def __init__(self, make, model, color="red"):
        self.make = make
        self.model = model
        self.color = color

    def get_color(self):
        return self._color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.lower() in ["red", "blue", "green"]:
            self._color = value.upper()
        else:
            raise ValueError("Invalid color. Choose from: red, blue, green")
```

### 4. Using ABCs with `register` to Customize Base Class

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Define a custom class that will be registered as a subclass of Vehicle
class Bike(Vehicle):
    def drive(self):
        return "Riding the bike"

# Register the custom class with the Vehicle ABC
Vehicle.register(Bike)

# Example usage
vehicle = Bike()
print(vehicle.drive())  # Output: Riding the bike

# Attempting to instantiate a non-registered subclass will raise an error
try:
    vehicle = Vehicle()  # This line will cause an error
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Vehicle with abstract methods drive
```

### 5. Using `abstractmethod` on Class Methods and Static Methods

```python
from abc import ABC, abstractmethod

class MathOperations(ABC):
    @staticmethod
    @abstractmethod
    def add(x, y):
        pass

    @classmethod
    @abstractmethod
    def multiply(cls, x, y):
        pass

class Calculator(MathOperations):
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y

# Example usage
calc = Calculator()
print(calc.add(3, 5))       # Output: 8
print(calc.multiply(4, 6))   # Output: 24
```

### 6. Using `abc` with Inheritance and Multiple Abstract Methods

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage
rectangle = Rectangle(5, 3)
print("Area:", rectangle.area())   # Output: Area: 15
print("Perimeter:", rectangle.perimeter()) # Output: Perimeter: 16
```

### 7. Using `abc` with Inheritance and Multiple Abstract Methods in a Subclass

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

class Dog(Mammal):
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
```

### 8. Using `abc` with Inheritance and Multiple Abstract Methods in a Subclass with Class Attributes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    _width = None
    _height = None

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        return self._width * self._height

# Example usage
rectangle = Rectangle(5, 3)
print("Area:", rectangle.get_area())   # Output: Area: 15
```

### 9. Using `abc` with Inheritance and Multiple Abstract Methods in a Subclass with Class Attributes and Properties

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Mammal(Animal):
    _name = None

    def __init__(self, name):
        self._name = name

class Dog(Mammal):
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
```

### 10. Using `abc` with Inheritance and Multiple Abstract Methods in a Subclass with Class Attributes and Properties

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Mammal(Animal):
    _name = None

    def __init__(self, name):
        self._name = name

class Dog(Mammal):
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
```

These examples demonstrate various aspects of using the `abc` module in Python, including defining abstract base classes, subclassing, implementing methods and properties, and using `register` to customize base classes. Each example includes comments explaining each step for clarity.
