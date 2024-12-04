# Data Types

**Python Data Types**
=======================

### 1. Integers

Integers are whole numbers, either positive, negative, or zero.

```python
# Create an integer variable
my_int = 10

# Print the value of the integer
print(my_int)  # Output: 10

# Integer arithmetic operations
result = my_int + 5
print(result)  # Output: 15
```

### 2. Floating Point Numbers (Floats)

Floats are numbers with decimal points.

```python
# Create a float variable
my_float = 3.14

# Print the value of the float
print(my_float)  # Output: 3.14

# Float arithmetic operations
result = my_float + 2.71
print(result)  # Output: 5.85
```

### 3. Complex Numbers

Complex numbers are numbers with both real and imaginary parts.

```python
# Create a complex number variable
my_complex = 3 + 4j

# Print the value of the complex number
print(my_complex)  # Output: (3+4j)

# Complex arithmetic operations
result = my_complex * 2 - 1
print(result)  # Output: (5+7j)
```

### 4. Strings

Strings are sequences of characters.

```python
# Create a string variable
my_string = "Hello, World!"

# Print the value of the string
print(my_string)  # Output: Hello, World!

# String slicing
slice_value = my_string[0:5]
print(slice_value)  # Output: Hello

# String concatenation
result = my_string + ", Python!"
print(result)  # Output: Hello, World!Python!
```

### 5. Boolean Values

Boolean values are either True or False.

```python
# Create a boolean variable
my_bool = True

# Print the value of the boolean
print(my_bool)  # Output: True

# Boolean arithmetic operations
result = my_bool and False
print(result)  # Output: False
```

### 6. Lists

Lists are ordered collections of values.

```python
# Create a list variable
my_list = [1, 2, 3, 4, 5]

# Print the value of the list
print(my_list)  # Output: [1, 2, 3, 4, 5]

# List indexing and slicing
index_value = my_list[0]
slice_value = my_list[1:3]
print(index_value)  # Output: 1
print(slice_value)  # Output: [2, 3]
```

### 7. Tuples

Tuples are ordered collections of values.

```python
# Create a tuple variable
my_tuple = (1, 2, 3, 4, 5)

# Print the value of the tuple
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Tuple indexing and slicing
index_value = my_tuple[0]
slice_value = my_tuple[1:3]
print(index_value)  # Output: 1
print(slice_value)  # Output: (2, 3)
```

### 8. Dictionaries

Dictionaries are unordered collections of key-value pairs.

```python
# Create a dictionary variable
my_dict = {"name": "John", "age": 30}

# Print the value of the dictionary
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# Dictionary key-value lookup
key_value = my_dict["name"]
print(key_value)  # Output: John

# Dictionary values manipulation
result = my_dict["age"] + 1
my_dict["age"] = result
print(my_dict)  # Output: {'name': 'John', 'age': 31}
```

### 9. Sets

Sets are unordered collections of unique values.

```python
# Create a set variable
my_set = {1, 2, 3, 4, 5}

# Print the value of the set
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Set addition
result = my_set.add(6)
print(result)  # Output: None

# Set intersection
other_set = {4, 5, 6, 7}
intersection_value = my_set & other_set
print(intersection_value)  # Output: {4, 5}
```

### 10. Frozensets

Frozensets are immutable sets.

```python
# Create a frozenset variable
my_frozenset = frozenset({1, 2, 3, 4, 5})

# Print the value of the frozenset
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})

# Frozenset comparison
other_frozenset = frozenset({4, 5, 6, 7})
comparison_value = my_frozenset == other_frozenset
print(comparison_value)  # Output: False
```
