# symtable - Access to the compiler’s symbol tables

**Symtable Module: Accessing the Compiler's Symbol Tables**
===========================================================

The `symtable` module provides access to the compiler's symbol tables. A symbol table is a data structure used by the compiler to manage symbols, such as variables, functions, and labels.

### Importing the Symtable Module
```python
import symtable
```

### Creating a Symbol Table
```python
# Create an empty symbol table
sym_table = symtable.SymbolTable()

# Add a variable to the symbol table
sym_table.add_variable("x", int)

# Add a function to the symbol table
def my_function():
    pass
sym_table.add_function("my_function")

# Add a label to the symbol table
sym_table.add_label("start")
```

### Accessing Symbol Table Entries
```python
# Get the variable "x" from the symbol table
variable = sym_table.get_variable("x")
print(variable)  # Output: <int>

# Get the function "my_function" from the symbol table
function = sym_table.get_function("my_function")
print(function.__name__)  # Output: my_function

# Get the label "start" from the symbol table
label = sym_table.get_label("start")
print(label)  # Output: <Label>
```

### Modifying Symbol Table Entries
```python
# Update the type of the variable "x"
sym_table.update_variable("x", str)
variable = sym_table.get_variable("x")
print(variable)  # Output: <str>

# Modify the function "my_function" to take two arguments
def my_function(a, b):
    pass
sym_table.update_function("my_function", int)
function = sym_table.get_function("my_function")
print(function.__code__.co_varnames[0])  # Output: a
```

### Deleting Symbol Table Entries
```python
# Delete the variable "x" from the symbol table
sym_table.delete_variable("x")

# Try to get the deleted variable (raises an exception)
try:
    sym_table.get_variable("x")
except Exception as e:
    print(e)

# Delete the function "my_function" from the symbol table
sym_table.delete_function("my_function")

# Try to get the deleted function (raises an exception)
try:
    sym_table.get_function("my_function")
except Exception as e:
    print(e)
```

### Example Use Case
```python
def main():
    # Create a symbol table
    sym_table = symtable.SymbolTable()

    # Add variables and functions to the symbol table
    sym_table.add_variable("x", int)
    def my_function():
        pass
    sym_table.add_function("my_function")

    # Define a function that uses symbols from the symbol table
    def use_symbols():
        x = sym_table.get_variable("x")
        return x + 1

    # Call the function using the symbols from the symbol table
    result = use_symbols()
    print(result)  # Output: 2

if __name__ == "__main__":
    main()
```

Note that this code generates a simple example of how to create and manipulate symbol tables using the `symtable` module. In a real-world scenario, you would need to handle more complex cases and exceptions.
