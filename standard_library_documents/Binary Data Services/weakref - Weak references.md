# weakref — Weak references

**WeakReferences Module**
==========================

The `weakref` module provides a way to create weak references to objects, which can be useful for memory management and caching.

### Example Usage
```python
import weakref

# Create a strong reference to an object
obj = object()

# Create a weak reference to the same object
weak_ref = weakref.ref(obj)

print(weak_ref())  # prints the original obj
```

### Creating Weak References

There are three types of weak references:

1. **WeakKeyDictionary**:
   ```python
import weakref

class Object:
    def __init__(self):
        self.name = "Object"

obj = Object()
dictionary = weakref.WeakKeyDictionary({obj: None})
```

2. **WeakValueDictionary**:
   ```python
import weakref

class Object:
    def __init__(self):
        self.name = "Object"

obj = Object()
dictionary = weakref.WeakValueDictionary({None: obj})
```

3. **ReferenceType**:
   ```python
import weakref

def create_object():
    return object()

reference = weakref.ReferenceType(obj)

# Create a new reference with the same object
new_reference = reference()

print(new_reference)  # prints the original obj
```

### Checking for Existence

To check if a weak reference is still valid, use the `isAlive()` method:
```python
import weakref

obj = object()
weak_ref = weakref.ref(obj)

if weak_ref() is None:  # checks if the object has been garbage collected
    print("Object no longer exists")
else:
    print("Object still exists")
```

### Using WeakReferences with Closures

Weak references can be used in closures to ensure that they don't prevent objects from being garbage collected:
```python
import weakref

def create_closure(obj):
    def inner():
        return obj

    # Create a weak reference to the object, which will decay and make the closure invalid
    weak_ref = weakref.ref(obj)

    return weak_ref

obj = object()
weak_ref = create_closure(obj)

# The weak reference has decayed, so we can't use it anymore
print(weak_ref())  # prints None
```

### WeakReferences with Context Managers

Weak references can be used in context managers to ensure that resources are properly cleaned up when they're no longer needed:
```python
import weakref

class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")

# Create a context manager with a weak reference to the resource
with weakref.ref(Resource()) as resource:
    # Use the resource
    pass  # prints "Acquiring resource"

# The weak reference has decayed, so we can't access it anymore
print(resource)  # prints None
```
