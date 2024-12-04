# dis - Disassembler for Python bytecode

The `dis` module is a part of the Python standard library that provides a way to examine Python bytecode. It can help you understand how Python programs are executed and debug them. Below are several comprehensive examples demonstrating various functionalities of the `dis` module.

### 1. Basic Disassembly

```python
import dis

# Example function to demonstrate basic disassembly
def example_function(x):
    return x * 2 + 3

# Get bytecode for the function
bytecode = example_function.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 2. Disassembling a Built-in Function

```python
import dis

# Disassemble the built-in sum function
dis.dis(sum)
```

### 3. Iterating Over Instructions

```python
import dis

def print_instructions(func):
    # Get bytecode for the function
    bytecode = func.__code__.co_code
    
    # Iterate over instructions and print them
    for offset, instruction in enumerate(dis.get_instructions(bytecode)):
        print(f"{offset:04d}: {instruction.opname} {instruction.argval}")

# Example function to demonstrate iterating over instructions
def example_function(x):
    return x * 2 + 3

print_instructions(example_function)
```

### 4. Disassembling a Module

```python
import dis
import inspect

# Get bytecode for the current module
module = inspect.currentframe().f_code.co_filename
with open(module, 'rb') as f:
    bytecode = f.read()

# Disassemble the bytecode of the entire module
dis.dis(bytecode)
```

### 5. Disassembling a Class Method

```python
import dis

class MyClass:
    @staticmethod
    def my_method(x):
        return x * 2 + 3

# Get bytecode for the class method
bytecode = MyClass.my_method.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 6. Disassembling a Module with Decorators

```python
import dis
import inspect

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator called")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function(x):
    return x * 2 + 3

# Get bytecode for the decorated function
bytecode = example_function.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 7. Disassembling a Generator Function

```python
import dis

def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Get bytecode for the generator function
bytecode = count_up_to.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 8. Disassembling a List Comprehension

```python
import dis

def list_comprehension_example():
    return [x * 2 + 3 for x in range(5)]

# Get bytecode for the list comprehension
bytecode = list_comprehension_example.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 9. Disassembling a Nested Function

```python
import dis

def outer_function(x):
    def inner_function(y):
        return x * y + 3
    
    return inner_function(2)

# Get bytecode for the nested function
bytecode = outer_function.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 10. Disassembling a Function with Keyword Arguments

```python
import dis

def example_function_with_kwargs(x, y=3):
    return x * y + 2

# Get bytecode for the function with keyword arguments
bytecode = example_function_with_kwargs.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

### 11. Disassembling a Function with Default Values

```python
import dis

def example_function_with_defaults(x, y=3):
    return x * y + 2

# Get bytecode for the function with default values
bytecode = example_function_with_defaults.__code__.co_code

# Disassemble the bytecode
dis.dis(bytecode)
```

These examples cover a range of functionalities within the `dis` module, from basic disassembly to more complex scenarios involving decorators and nested functions. Each example is thoroughly documented to help understand how to use each feature effectively.
