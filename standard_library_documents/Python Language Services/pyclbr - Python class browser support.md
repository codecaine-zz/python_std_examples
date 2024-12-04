# pyclbr - Python class browser support

The `pyclbr` module is a built-in Python module that provides a simple way to browse the directory of classes, functions, and methods defined by the Python compiler. It can be used to extract information about modules and objects within those modules.

Here are comprehensive code examples for the `pyclbr` module:

```python
import pyclbr

# Load a module
module = pyclbr.readmodule('os')

# Print all classes in the loaded module
print("Classes in os:")
for cls in module.classes():
    print(f"  - {cls.name}")

# Print all functions in the loaded module
print("\nFunctions in os:")
for func in module.functions():
    print(f"  - {func.name}")

# Print details of a specific class
class_name = 'os.path'
if class_name in module.classes():
    cls_details = module.classes()[class_name]
    print(f"\nDetails of {class_name}:")
    for attr in cls_details.attributes:
        print(f"  - {attr.name} ({attr.type})")

# Print details of a specific function
function_name = 'os.path.join'
if function_name in module.functions():
    func_details = module.functions()[function_name]
    print(f"\nDetails of {function_name}:")
    for arg in func_details.arguments:
        print(f"  - {arg.name} ({arg.type})")

# Print all methods in a specific class
class_name = 'os.path'
if class_name in module.classes():
    cls_details = module.classes()[class_name]
    print("\nMethods in os.path:")
    for method in cls_details.methods:
        print(f"  - {method.name} ({method.type})")
```

### Explanation:

1. **Loading a Module**: 
   - `pyclbr.readmodule('os')` loads the contents of the `os` module and returns a dictionary-like object containing information about all classes, functions, and methods defined in the module.

2. **Printing All Classes**:
   - Iterates over the classes and prints their names.

3. **Printing All Functions**:
   - Iterates over the functions and prints their names.

4. **Details of a Specific Class**:
   - Checks if a specific class exists and retrieves its details.
   - Prints all attributes, arguments, and methods for that class.

5. **Details of a Specific Function**:
   - Checks if a specific function exists and retrieves its details.
   - Prints all arguments and their types for that function.

6. **Methods in a Specific Class**:
   - Retrieves the methods of a specific class and prints them.

These examples demonstrate how to use `pyclbr` to extract and display information about classes, functions, and methods within Python modules. The code is structured to be clear and easy to understand, making it suitable for inclusion in official documentation or educational purposes.
