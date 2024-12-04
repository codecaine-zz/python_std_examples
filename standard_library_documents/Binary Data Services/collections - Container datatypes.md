# collections — Container datatypes

Here's an example of how you can use the various container datatypes available in Python's `collections` module.

```python
from collections import *
import time
import random

# 1. List
print("List")
# Create a list
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Append an element to the end of the list
numbers.append(6)
print(numbers)

# Insert an element at a specific position
numbers.insert(2, 10)
print(numbers)

# Remove the first occurrence of an element
numbers.remove(4)
print(numbers)

# Pop an element from the end of the list
last_element = numbers.pop()
print(f"Removed last element: {last_element}")
print(numbers)

# Create a new list with the same elements as another list
list1 = [1, 2, 3]
list2 = numbers[:]
print(list1 is list2)  # This will be False

numbers.extend([7, 8])
print(numbers)

# Sort the list in-place
numbers.sort()
print(numbers)

# Reverse the list in-place
numbers.reverse()
print(numbers)

# Indexing and slicing
print("Indexing and Slicing")
index = numbers.index(10)
print(f"Index of 10: {index}")

sub_list = numbers[1:3]
print(sub_list)

numbers.clear()
print(numbers)  # This will be []

# 2. Tuple
print("\nTuple")
# Create a tuple
tup = (1, 2, 3)
print(tup)

# Unpack the tuple into separate variables
a, b, c = tup
print(f"a: {a}, b: {b}, c: {c}")

# Use the `in` operator to check if an element is in the tuple
if 2 in tup:
    print("2 is in the tuple")

tup += (4,)
print(tup)

tup = tup[:2] + (6,)  # Slice the tuple
print(tup)

# 3. Set
print("\nSet")
# Create a set
numbers_set = {1, 2, 3}
print(numbers_set)

# Add an element to the set
numbers_set.add(4)
print(numbers_set)

# Remove an element from the set
numbers_set.remove(2)
print(numbers_set)

# Use the `difference` method to remove elements that are in another set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))

# Find the intersection of two sets using the `intersection` method
print(set1.intersection(set2))

# Use the `symmetric_difference` method to find elements that are in exactly one set
print(set1.symmetric_difference(set2))

numbers_set.clear()
print(numbers_set)  # This will be []

# 4. Dict
print("\nDict")
# Create a dictionary
person = {"name": "John", "age": 30}
print(person)

# Add a new key-value pair to the dictionary
person["city"] = "New York"
print(person)

# Update the value of an existing key
person["age"] = 31
print(person)

# Remove a key-value pair from the dictionary using the `del` statement
del person["name"]
print(person)

# Use the `.keys()` method to get a view object that displays a list of all keys in the dictionary
print(person.keys())

# Use the `.values()` method to get a view object that displays a list of all values in the dictionary
print(person.values())

# Use the `.items()` method to get a view object that displays a list of all key-value pairs in the dictionary
for key, value in person.items():
    print(f"{key}: {value}")

person.clear()
print(person)  # This will be {}

# 5. Frozenset (unmodifiable set)
print("\nFrozenset")
# Create a frozenset from a list
numbers_frozenset = frozenset([1, 2, 3])
print(numbers_frozenset)

# Use the `in` operator to check if an element is in the frozenset
if 2 in numbers_frozenset:
    print("2 is in the frozenset")

try:
    # Attempt to add an element to the frozenset (this will raise a `TypeError`)
    numbers_frozenset.add(4)
except TypeError as e:
    print(f"Error: {e}")

numbers_frozenset = frozenset([1, 2, 3]) | frozenset([4, 5, 6])
print(numbers_frozenset)

try:
    # Attempt to modify the frozenset by adding or removing elements (this will raise a `TypeError`)
    numbers_frozenset.add(7)
except TypeError as e:
    print(f"Error: {e}")
```

This example demonstrates how you can create, manipulate, and iterate over various container datatypes in Python using the `collections` module. It covers list, tuple, set, dictionary, and frozenset examples, including indexing, slicing, addition, removal, updating, and modification of elements.
