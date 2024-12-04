# inspect — Inspect live objects

**Module: `inspect`**
=====================================

The `inspect` module provides several useful functions to help get information about live objects, such as modules, classes, instances, and frames.

### Module Inspection

#### 1. `inspect.getmodule()`

Returns the module that contains the specified object.

```python
import inspect

def main():
    # Get the current frame
    current_frame = inspect.currentframe()

    # Get the module from the current frame
    current_module = inspect.getmodule(current_frame)

    print("Current Module:", current_module.__name__)

if __name__ == "__main__":
    main()
```

#### 2. `inspect.getmro()`

Returns the method resolution order for a specified object.

```python
import inspect

class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

def main():
    # Get the class hierarchy
    parent_class = ParentClass
    child_class = ChildClass
    mro = inspect.getmro(parent_class)

    print("Method Resolution Order:", mro)

if __name__ == "__main__":
    main()
```

#### 3. `inspect.getmembers()`

Returns a list of tuples containing the names and values of specified object's members.

```python
import inspect

def main():
    # Create an example class
    class ExampleClass:
        def method1(self):
            pass

        def method2(self, param):
            pass

    # Get all methods and attributes
    obj = ExampleClass()
    members = inspect.getmembers(obj)

    print("Members:")
    for name, value in members:
        print(f"- {name}: {value.__self__}")

if __name__ == "__main__":
    main()
```

#### 4. `inspect.getattr()`

Returns the attribute with the specified name.

```python
import inspect

def main():
    # Create an example class
    class ExampleClass:
        def method1(self):
            pass

        def method2(self, param):
            pass

    obj = ExampleClass()
    attr_name = "method1"

    attr_value = inspect.getattr(obj, attr_name)

    print(f"Attribute '{attr_name}': {attr_value}")

if __name__ == "__main__":
    main()
```

#### 5. `inspect.getsource()`

Returns the source code for a specified object.

```python
import inspect

def main():
    # Create an example function
    def example_function():
        pass

    func_name = "example_function"
    source_code = inspect.getsource(func_name)

    print(f"Source Code for '{func_name}':\n{source_code}")

if __name__ == "__main__":
    main()
```

### Class Inspection

#### 1. `inspect.getmembers()`

Returns a list of tuples containing the names and values of specified object's attributes.

```python
import inspect

def main():
    # Create an example class
    class ExampleClass:
        def method1(self):
            pass

        def method2(self, param):
            pass

    obj = ExampleClass()
    members = inspect.getmembers(obj)

    print("Members:")
    for name, value in members:
        print(f"- {name}: {value.__self__}")

if __name__ == "__main__":
    main()
```

#### 2. `inspect.getclass()`

Returns the class of a specified object.

```python
import inspect

def main():
    # Create an example instance
    obj = "hello"

    class_name = type(obj).__name__

    print(f"Class Name: {class_name}")

if __name__ == "__main__":
    main()
```

### Frame Inspection

#### 1. `inspect.currentframe()`

Returns the current frame.

```python
import inspect

def main():
    # Get the current frame
    current_frame = inspect.currentframe()

    print("Current Frame:", current_frame)

if __name__ == "__main__":
    main()
```

#### 2. `inspect.getouterframes()`

Returns a list of frames containing information about the caller's stack.

```python
import inspect

def outer_function():
    inner_function()

def main():
    # Call the outer function
    outer_function()

if __name__ == "__main__":
    main()
```

#### 3. `inspect.getframeinfo()`

Returns a frame object with additional information about a specified frame.

```python
import inspect

def main():
    # Create an example function
    def example_function():
        pass

    func_frame = inspect.getframeinfo(example_function)

    print(f"Function Name: {func_frame.function}")
    print(f"File Name: {func_frame.filename}")

if __name__ == "__main__":
    main()
```

### Other Functions

#### 1. `inspect.isclass()`

Checks if the specified object is a class.

```python
import inspect

def main():
    # Create an example class
    class ExampleClass:
        pass

    obj = ExampleClass()

    is_class = inspect.isclass(obj)

    print(f"Is Class: {is_class}")

if __name__ == "__main__":
    main()
```

#### 2. `inspect.isfunction()`

Checks if the specified object is a function.

```python
import inspect

def main():
    # Create an example function
    def example_function():
        pass

    obj = example_function()

    is_func = inspect.isfunction(obj)

    print(f"Is Function: {is_func}")

if __name__ == "__main__":
    main()
```

#### 3. `inspect.ismethod()`

Checks if the specified object is a method.

```python
import inspect

def main():
    # Create an example class
    class ExampleClass:
        def method(self):
            pass

    obj = ExampleClass()

    is_method = inspect.ismethod(obj)

    print(f"Is Method: {is_method}")

if __name__ == "__main__":
    main()
```

#### 4. `inspect.ismodule()`

Checks if the specified object is a module.

```python
import inspect

def main():
    # Create an example module
    import example_module

    obj = example_module

    is_module = inspect.ismodule(obj)

    print(f"Is Module: {is_module}")

if __name__ == "__main__":
    main()
```

#### 5. `inspect.gettrace()`

Returns the frame of the caller.

```python
import inspect

def main():
    # Create an example function
    def example_function():
        pass

    # Get the trace frame
    trace_frame = inspect.gettrace()

    print(f"Trace Frame: {trace_frame}")

if __name__ == "__main__":
    main()
```

These are some of the most commonly used functions in the `inspect` module. The specific function you need may depend on your use case, but this should provide a good starting point for exploring what the `inspect` module has to offer.
