# copy — Shallow and deep copy operations

**Copy Module**
================

The `copy` module provides functions to create copies of objects.

### Installation

You can install the `copy` module using pip:
```bash
pip install copy
```
### Shallow Copy

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the original elements. This means that if you modify a sub-element of the original object, the same modification will be reflected in the copied object.

#### Example:
```python
import copy

# Original list
original_list = [[1], [2], [3]]

# Create a shallow copy of the list
shallow_copy = copy.copy(original_list)

# Modify an element of the original list
original_list[0][0] = 'X'

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)

# Output:
# Original List: [['X'], [2], [3]]
# Shallow Copy: [['X'], [2], [3]]

# Deep Copy
deep_copy = copy.deepcopy(original_list)

# Modify an element of the original list
original_list[0][0] = 'Y'

print("Original List:", original_list)
print("Deep Copy:", deep_copy)

# Output:
# Original List: [['Y'], [2], [3]]
# Deep Copy: [[1], [2], [3]]
```
As shown above, the shallow copy is affected by the modification of the original list.

### Deep Copy

A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original. This means that if you modify an element of the copied object, it will not affect the original object.

#### Example:
```python
import copy

# Original list
original_list = [[1], [2], [3]]

# Create a deep copy of the list
deep_copy = copy.deepcopy(original_list)

# Modify an element of the copied list
deep_copy[0][0] = 'X'

print("Original List:", original_list)
print("Deep Copy:", deep_copy)

# Output:
# Original List: [[1], [2], [3]]
# Deep Copy: [['X'], [2], [3]]

# Create a dictionary with mutable elements
original_dict = {'a': 1, 'b': [2]}

# Create a copy of the dictionary
dict_copy = copy.copy(original_dict)
deep_dict_copy = copy.deepcopy(original_dict)

# Modify an element of the copied dictionary
dict_copy['a'] = 10

print("Original Dictionary:", original_dict)
print("Copy of Dictionary:", dict_copy)
print("Deep Copy of Dictionary:", deep_dict_copy)

# Output:
# Original Dictionary: {'a': 1, 'b': [2]}
# Copy of Dictionary: {'a': 10, 'b': [2]}
# Deep Copy of Dictionary: {'a': 1, 'b': [2]}
```
As shown above, the deep copy is not affected by the modification of the copied dictionary.
