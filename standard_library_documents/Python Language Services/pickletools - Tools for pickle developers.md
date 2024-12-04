# pickletools - Tools for pickle developers

The `pickletools` module in Python provides tools for examining and debugging pickled data, which is used to serialize and deserialize objects. Below are comprehensive code examples for each functionality provided by `pickletools`, including comments explaining each step.

```python
# Example 1: Inspecting a Pickle File

import pickletools

def inspect_pickle_file(filename):
    # Open the pickle file in binary read mode
    with open(filename, 'rb') as f:
        # Load and parse the pickle data
        parsed_data = pickletools.dis(f)
        
        # Print the disassembly of the pickled data
        for line in parsed_data.splitlines():
            print(line)

# Example usage
inspect_pickle_file('example.pkl')
```

### Explanation:
- **Function Definition**: The function `inspect_pickle_file` takes a filename as an argument.
- **File Opening**: The file is opened in binary read mode (`'rb'`) to handle the serialized data.
- **Loading and Parsing**: The `pickletools.dis()` function is used to parse the pickle data, which disassembles it into human-readable form.
- **Output**: Each line of disassembly is printed to the console.

### Example 2: Extracting Source Code from a Pickled Object

```python
import pickletools

def extract_source_code(obj):
    # Create an in-memory buffer and write the object to it
    import io
    buf = io.BytesIO()
    pickle.dump(obj, buf)
    
    # Get the bytecode of the pickled data
    bytecodes = buf.getvalue()
    
    # Disassemble the bytecodes
    parsed_data = pickletools.dis(bytecodes)
    
    # Print the disassembly
    for line in parsed_data.splitlines():
        print(line)

# Example usage
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
extract_source_code(obj)
```

### Explanation:
- **Object Creation**: A simple class `MyClass` is defined with an initializer.
- **Buffer and Serialization**: The object is serialized into a memory buffer using `pickle.dump()`.
- **Bytecode Retrieval**: The bytecodes are extracted from the buffer.
- **Disassembly**: The `pickletools.dis()` function disassembles the bytecodes, providing insights into the serialization process.

### Example 3: Generating Python Source Code for a Pickled Object

```python
import pickletools
import ast

def generate_python_source_code(obj):
    # Create an in-memory buffer and write the object to it
    import io
    buf = io.BytesIO()
    pickle.dump(obj, buf)
    
    # Get the bytecodes of the pickled data
    bytecodes = buf.getvalue()
    
    # Disassemble the bytecodes
    parsed_data = pickletools.dis(bytecodes)
    
    # Parse the disassembly into Python source code
    ast_code = ast.parse(parsed_data)
    
    # Print the generated source code
    import pprint
    pprint.pprint(ast_code)

# Example usage
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
generate_python_source_code(obj)
```

### Explanation:
- **Buffer and Serialization**: Similar to example 2, the object is serialized into a buffer.
- **Disassembly**: The bytecodes are disassembled to understand the serialization process.
- **Parsing**: The `ast.parse()` function converts the disassembly into Python source code.
- **Output**: The parsed source code is printed using `pprint.pprint()`, which provides a readable representation of the AST.

These examples demonstrate how to use `pickletools` for various purposes, from inspecting pickled data to generating Python source code that reconstructs it.
