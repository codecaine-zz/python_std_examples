# types - Dynamic type creation and names for built-in types

The `types` module in Python provides a way to create new types dynamically using the `types.ModuleType`, `types.FunctionType`, `types.BuiltinFunctionType`, and other classes. This is useful for extending the language or creating custom data structures with specific behaviors.

Below are comprehensive code examples for various functionalities provided by the `types` module:

### 1. Creating a Custom Module

```python
import types

# Create a new module dynamically
new_module = types.ModuleType("my_custom_module")

# Add attributes to the module
new_module.my_variable = "Hello, World!"
new_module.my_function = lambda x: f"Value is {x}"

# Accessing module attributes
print(new_module.my_variable)  # Output: Hello, World!
print(new_module.my_function(42))  # Output: Value is 42

# You can also import the module as if it were a regular Python file
import my_custom_module
print(my_custom_module.my_variable)  # Output: Hello, World!
print(my_custom_module.my_function(42))  # Output: Value is 42
```

### 2. Creating a Custom Function

```python
import types

# Define a custom function using the FunctionType
def custom_function(x):
    return x * 2

# Create an instance of FunctionType with specified arguments and defaults
custom_func_instance = types.FunctionType(
    func=custom_function,
    args=("x",),
    dargs=(10,),
    kwonlydargs=tuple(),
    kws=("y",),
    defaults=(5,),
    closure=None
)

# Call the custom function
print(custom_func_instance(3))  # Output: 20 (10 * 3)
print(custom_func_instance(y=6, x=7))  # Output: 49 (7 * 6 + 5)
```

### 3. Creating a Custom Builtin Function

```python
import types

# Define a custom built-in function using the BuiltinFunctionType
def custom_builtin_function(x):
    return x ** 2

# Create an instance of BuiltinFunctionType with specified arguments and defaults
custom_builtin_func_instance = types.BuiltinFunctionType(
    func=custom_builtin_function,
    args=("x",),
    dargs=(5,),
    kwonlydargs=tuple(),
    kws=("y",),
    defaults=(3,),
    closure=None
)

# Call the custom built-in function
print(custom_builtin_func_instance(2))  # Output: 4 (2 ** 2)
print(custom_builtin_func_instance(y=3, x=4))  # Output: 16 (4 ** 3 + 3)
```

### 4. Creating a Custom Class

```python
import types

# Define a custom class using the type() function
class MyCustomClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyCustomClass
my_instance = MyCustomClass(10)

# Accessing the attribute of the custom class
print(my_instance.value)  # Output: 10

# You can also define methods for the class dynamically
MyCustomClass.my_method = types.MethodType(lambda self: f"My value is {self.value}", MyCustomClass)

print(my_instance.my_method())  # Output: My value is 10
```

### 5. Creating a Custom Exception

```python
import types

# Define a custom exception using the type() function
class MyCustomError(Exception):
    pass

# Create an instance of MyCustomError
try:
    raise MyCustomError("This is a custom error")
except MyCustomError as e:
    print(e)  # Output: This is a custom error
```

### 6. Creating a Custom Method Type

```python
import types

# Define a custom method using the MethodType function
def my_method(self):
    return f"Hello from {self.__class__.__name__}"

# Create an instance of MethodType for MyCustomClass
MyCustomClass.my_method = types.MethodType(my_method, MyCustomClass)

my_instance = MyCustomClass()
print(my_instance.my_method())  # Output: Hello from MyCustomClass
```

### 7. Creating a Custom Type with Slots

```python
import types

# Define a custom type with slots using the type() function
MyCustomType = types.new_class(
    "MyCustomType",
    bases=(object,),
    exec_body=lambda cls, locals: locals.update({
        "__slots__": ("value",)
    })
)

# Create an instance of MyCustomType
my_instance = MyCustomType()
my_instance.value = 20

print(my_instance.value)  # Output: 20

# Accessing the attribute directly without slots is not allowed
try:
    my_instance.non_slot_attribute = 30
except AttributeError as e:
    print(e)  # Output: 'MyCustomType' object has no attribute 'non_slot_attribute'
```

### 8. Creating a Custom Type with New

```python
import types

# Define a custom type using the new() function
class MyCustomClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyCustomClass
my_instance = MyCustomClass(10)

# Accessing the attribute of the custom class
print(my_instance.value)  # Output: 10

# You can also define methods for the class dynamically
MyCustomClass.my_method = types.MethodType(lambda self: f"My value is {self.value}", MyCustomClass)

print(my_instance.my_method())  # Output: My value is 10
```

These examples demonstrate how to use various classes and functions in the `types` module to create dynamic types, functions, methods, classes, exceptions, and more. Each example includes comments explaining the purpose of each step and the expected output.
