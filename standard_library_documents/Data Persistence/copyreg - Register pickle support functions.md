# copyreg — Register pickle support functions

**Module: copyreg**

The `copyreg` module provides a way to register custom pickle support, which allows you to customize how Python serializes and deserializes objects.

### Installing the Module
You don't need to install any external libraries to use this module. It's part of the standard library in Python.

### Importing the Module

```python
import copyreg
```

### Registering Custom Pickle Support Functions

You can register custom pickle support functions using the `register` function from the `copyreg` module.

```python
# Define a custom pickle support function for integers
def int_support():
    """Register support for pickling and unpickling integers"""
    return (int, lambda c: int.from_bytes(c, 'big'))

# Register the custom pickle support function
copyreg.register(int_support)
```

### Unpickling Custom Objects

To use a registered custom pickle support function to unpickle an object, you can use the `unpickle` function from the `copyreg` module.

```python
import pickle

# Pickle some data using the custom support function
data = b'\x80\x03]q\x00(X\x01\x02)'
pkl_data = pickle.loads(data)

print(pkl_data)  # Output: (1, 2)
```

### Deregistering Custom Pickle Support Functions

To deregister a custom pickle support function, you can use the `deregister` function from the `copyreg` module.

```python
# Deregister the custom pickle support function
copyreg.deregister(int_support)
```

Note: After deregistering a custom pickle support function, you won't be able to unpickle objects that were previously pickled using that function.

### Example Use Cases

*   Serializing and deserializing custom object types with `pickle` module.
*   Registering custom serialization formats (e.g., binary data) for specific object types.

**Full Code**

```python
import copyreg
import pickle

def int_support():
    """Register support for pickling and unpickling integers"""
    return (int, lambda c: int.from_bytes(c, 'big'))

# Register the custom pickle support function
copyreg.register(int_support)

try:
    # Pickle some data using the custom support function
    data = b'\x80\x03]q\x00(X\x01\x02)'
    pkl_data = pickle.loads(data)
    print(pkl_data)  # Output: (1, 2)
except TypeError as e:
    print(e)

# Deregister the custom pickle support function
copyreg.deregister(int_support)

try:
    # Attempt to unpickle data using the deregistered custom support function
    data = b'\x80\x03]q\x00(X\x01\x02)'
    pkl_data = pickle.loads(data)
    print(pkl_data)  # Raises TypeError
except TypeError as e:
    print(e)

# Register a new custom pickle support function
def float_support():
    """Register support for pickling and unpickling floats"""
    return (float, lambda c: float.from_bytes(c, 'big'))

copyreg.register(float_support)
```
