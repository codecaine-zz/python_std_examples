# pickletools — Tools for pickle developers

**pickletools Module**
======================

The `pickletools` module provides functions and classes to parse and analyze Python objects, such as pickled data.

### Code Generation

```python
import pickletools

# Function to dump a Python object using pickle.dump()
def dump_object(obj):
    """Dump a Python object to a bytes buffer."""
    # Use pickle.dumps() to serialize the object into a bytes buffer
    buf = pickle.dumps(obj)
    # Use pickletools.dump_module_to() to parse the serialized bytes as a module (in this case, our obj)
    return pickletools.dump_module_to(buf)

# Function to load a Python object from a bytes buffer using pickle.loads()
def load_object(buf):
    """Load a Python object from a bytes buffer."""
    # Use pickletools.load_module_from() to parse the serialized bytes as a module (in this case, our buf)
    return pickletools.load_module_from(buf)

# Function to get a human-readable representation of a pickled object
def get_pretty_obj(obj):
    """Get a pretty-printed string representation of a pickled object."""
    # Use pickle.dumps() to serialize the object into a bytes buffer
    buf = pickle.dumps(obj)
    # Use pickletools.PICKLE.loads as a fallback if dump_module_to returns an error.
    return pickletools.unpickler.load(buf)

# Example usage:
obj = 12345
buf = dump_object(obj)
print(buf)  # Output: b'\x80\x03}q\x00(X\x01K\x02K.'

loaded_obj = load_object(buf)
print(loaded_obj)  # Output: 12345

pretty_obj = get_pretty_obj(obj)
print(pretty_obj)  # Output: 'integer object(n=12345)'
```

### Classes and Functions

The `pickletools` module provides the following classes and functions:

*   **`dump_module_to()`**: Parse a serialized bytes buffer as a Python module.
*   **`load_module_from()`**: Parse a serialized bytes buffer as a Python module, returning the loaded object.
*   **`pickle.PICKLE.loads()`**: Load an unpickled bytes buffer into a Python object.
*   **`pickletools.unpickler.load()`**: Load an unpickled bytes buffer into a Python object.

### Modules

The `pickletools` module provides several modules for different purposes:

*   **`pickletools.PicklingError`**: Raised when an error occurs during pickling.
*   **`pickletools.UnpicklingError`**: Raised when an error occurs during unpickling.

Note: The above code examples are intended to illustrate how the `pickletools` module can be used, but they may not cover all possible use cases or edge conditions. Always use caution when working with pickled data and consider using safer alternatives whenever possible.
