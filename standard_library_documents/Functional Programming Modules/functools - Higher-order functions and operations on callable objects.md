# functools — Higher-order functions and operations on callable objects

Here's an example of how you can use the `functools` module from Python's standard library.

```python
import functools

# 1. Partial Application
def add(a, b):
    return a + b

partial_add_5 = functools.partial(add, 5)
print(partial_add_5(3))  # Outputs: 8

# 2. Higher-Order Functions (Functions as Arguments)
def multiply_by_2(f):
    return lambda x: f(x) * 2

double_values = multiply_by_2
print(double_values(4))  # Outputs: 8

# 3. Closures
def outer():
    x = 10
    def inner():
        y = 20
        print("Value of x:", x)
        print("Value of y:", y)
    return inner

func = outer()
func()

# 4. Reduce (Aggregate Function)
from functools import reduce

numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, numbers))  # Outputs: 15

# 5. Total Order Reducer
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1 < p2)  # Outputs: True
print(p1 == p2)  # Outputs: False

# 6. Singleton Function
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Outputs: True

# 7. LruCache (Cache for Function Results)
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Outputs: 55

# 8. singledispatch (Multi-Dispatch for Functions)
from functools import singledispatch

@singledispatch
def handle_event(event_type):
    print("Default event handled")

@handle_event.register
def _(event_type="button_click"):
    print("Button click event handled")

handle_event("button_click")  # Outputs: Button click event handled
handle_event("unknown_event")  # Outputs: Default event handled

# 9. cmp_to_key (Key Function from Comparison Functions)
from functools import cmp_to_key

def compare_strings(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return 0

sorted_list = sorted(["hello", "world"], key=cmp_to_key(compare_strings))
print(sorted_list)  # Outputs: ['world', 'hello']

# 10. update_wrapper (Update the wrapper function's docstring and __name__)
from functools import update_wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorated function")
        return func(*args, **kwargs)
    update_wrapper(wrapper, func)  # Update the wrapper function's docstring
    return wrapper

@my_decorator
def add(a, b):
    """Add two numbers"""
    return a + b

print(add.__name__)  # Outputs: decorated_add
print(add.__doc__)   # Outputs: Add two numbers
```

These examples demonstrate how you can use various functions from the `functools` module to create higher-order functions, work with closures, and perform operations such as partial application, caching, and multi-dispatch.
