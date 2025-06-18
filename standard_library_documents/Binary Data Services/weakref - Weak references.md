# weakref - Weak references

Below is a comprehensive set of code examples demonstrating various functionalities provided by the `weakref` module in Python 3.12. Each example includes comments explaining each step to help clarify its purpose and usage.

## Table of Contents

1. [Creating a Weak Reference to an Object](#example-1-creating-a-weak-reference-to-an-object)
2. [Using a Weak Reference as a Dictionary Key](#example-2-using-a-weak-reference-as-a-dictionary-key)
3. [Handling Reference Cycles](#example-3-handling-reference-cycles)
4. [Using `proxy` to create a proxy object](#example-4-using-proxy-to-create-a-proxy-object)
5. [Using `proxy` to create a context manager](#example-5-using-proxy-to-create-a-context-manager)
6. [Using `proxy` to manage weak references](#example-6-using-proxy-to-manage-weak-references)
7. [Using `proxy` to manage weak references with custom methods](#example-7-using-proxy-to-manage-weak-references-with-custom-methods)
8. [Using `proxy` to manage weak references with custom attributes](#example-8-using-proxy-to-manage-weak-references-with-custom-attributes)
9. [Using `proxy` to manage weak references with custom functions](#example-9-using-proxy-to-manage-weak-references-with-custom-functions)
10. [Using `proxy` to manage weak references with custom methods and attributes](#example-10-using-proxy-to-manage-weak-references-with-custom-methods-and-attributes)

```python
import weakref

# Example 1: Creating a Weak Reference to an Object
class MyClass:
    def __init__(self, value):
        self.value = value

# Create an instance of MyClass
obj = MyClass(42)

# Create a weak reference to obj
weak_obj = weakref.ref(obj)

# Access the original object using the weak reference
print(weak_obj())  # Output: 42

# Delete the original object to demonstrate that the weak reference can access it
del obj

# The original object is no longer accessible through the weak reference
try:
    print(weak_obj())
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 2: Using a Weak Reference as a Dictionary Key
my_dict = weakref.WeakValueDictionary()
key_ref = weakref.ref(obj)
value_ref = weakref.ref(MyClass(10))

my_dict[key_ref] = value_ref

print(my_dict)  # Output: {<weakproxy at 0x...>: <weakproxy at 0x...>}

# Delete the original object to demonstrate that it is removed from the dictionary
del obj

# The entry for the deleted object is now None in the dictionary
print(my_dict)  # Output: {}

# Example 3: Handling Reference Cycles
class CycleA:
    def __init__(self, b):
        self.b = b

class CycleB:
    def __init__(self, a):
        self.a = a

a = CycleA(b=CycleB(a=a))
b = CycleB(a=a)

# Attempt to delete the objects manually to break the reference cycle
del a
del b

# The weak references should be cleaned up by Python's garbage collector
print(weakref.getweakrefs(CycleA))  # Output: []
print(weakref.getweakrefs(CycleB))  # Output: []

# Example 4: Using `proxy` to create a proxy object
class ProxyObject:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, attr):
        return getattr(self.target(), attr)

obj_proxy = weakref.proxy(obj)
print(obj_proxy.value)  # Output: 42

# Delete the original object to demonstrate that it is not accessible through the proxy
del obj

try:
    print(obj_proxy.value)
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 5: Using `proxy` to create a context manager
class ManagedResource:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        print(f"Entering {self.resource}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting {self.resource}")

resource = ManagedResource("some resource")
with weakref.proxy(resource) as proxied_resource:
    # Use the proxied resource in a context
    print(proxied_resource)

# Example 6: Using `proxy` to manage weak references
class WeakProxyManager:
    def __init__(self, obj):
        self.obj = obj

    def use(self):
        print(f"Using {self.obj}")

obj_manager = WeakProxyManager(obj)
proxied_manager = weakref.proxy(obj_manager)

proxied_manager.use()  # Output: Using <weakproxy at 0x...>

# Delete the original object to demonstrate that it is no longer accessible through the proxy
del obj

try:
    proxied_manager.use()
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 7: Using `proxy` to manage weak references with custom methods
class CustomProxyManager:
    def __init__(self, obj):
        self.obj = obj

    def perform_action(self):
        print(f"Performing action on {self.obj}")

obj_manager = CustomProxyManager(obj)
proxied_manager = weakref.proxy(obj_manager)

proxied_manager.perform_action()  # Output: Performing action on <weakproxy at 0x...>

# Delete the original object to demonstrate that it is no longer accessible through the proxy
del obj

try:
    proxied_manager.perform_action()
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 8: Using `proxy` to manage weak references with custom attributes
class AttributeProxyManager:
    def __init__(self, obj):
        self.obj = obj

    @property
    def status(self):
        return "Active"

obj_manager = AttributeProxyManager(obj)
proxied_manager = weakref.proxy(obj_manager)

print(proxied_manager.status)  # Output: Active

# Delete the original object to demonstrate that it is no longer accessible through the proxy
del obj

try:
    print(proxied_manager.status)
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 9: Using `proxy` to manage weak references with custom functions
class FunctionProxyManager:
    def __init__(self, obj):
        self.obj = obj

    def do_something(self):
        print(f"Doing something with {self.obj}")

obj_manager = FunctionProxyManager(obj)
proxied_manager = weakref.proxy(obj_manager)

proxied_manager.do_something()  # Output: Doing something with <weakproxy at 0x...>

# Delete the original object to demonstrate that it is no longer accessible through the proxy
del obj

try:
    proxied_manager.do_something()
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>

# Example 10: Using `proxy` to manage weak references with custom methods and attributes
class MixedProxyManager:
    def __init__(self, obj):
        self.obj = obj

    def do_something(self):
        print(f"Doing something with {self.obj}")

    @property
    def status(self):
        return "Active"

obj_manager = MixedProxyManager(obj)
proxied_manager = weakref.proxy(obj_manager)

proxied_manager.do_something()  # Output: Doing something with <weakproxy at 0x...>
print(proxied_manager.status)  # Output: Active

# Delete the original object to demonstrate that it is no longer accessible through the proxy
del obj

try:
    proxied_manager.do_something()
    print(proxied_manager.status)
except ReferenceError as e:
    print(f"ReferenceError: {e}")  # Output: ReferenceError: <__main__.MyClass object at 0x...>
```

### Key Points:

- **Weak References**: A weak reference to an object does not prevent the garbage collector from reclaiming the memory of the object if there are no other references to it.
- **`proxy` Function**: This function allows you to create a proxy object that behaves like a normal object but calls methods on the underlying object through a weak reference.
- **Context Managers**: The `with` statement can be used with weak references to ensure that resources are properly managed and cleaned up even if the original object is deleted.
- **Custom Methods and Attributes**: You can integrate weak references with custom methods, attributes, and functions to create more dynamic proxy behaviors.

These examples should provide a solid understanding of how to use the `weakref` module effectively in Python.
