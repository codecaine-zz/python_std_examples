# copy - Shallow and deep copy operations

The `copy` module in Python provides a variety of functions to perform shallow and deep copies on objects, which are essential for managing complex data structures. Here are comprehensive examples demonstrating how to use these functionalities:

### Shallow Copy

A shallow copy creates a new object that is a copy of the original object but references the same objects as the originals. This means that changes to sub-objects in the copied object will affect the original object.

```python
# Import the necessary module
import copy

def demonstrate_shallow_copy():
    # Example: Shallow copying a list
    original_list = [1, 2, [3, 4]]
    shallow_copied_list = copy.copy(original_list)
    
    print("Original List:", original_list)  # Output: Original List: [1, 2, [3, 4]]
    print("Shallow Copied List:", shallow_copied_list)  # Output: Shallow Copied List: [1, 2, [3, 4]]

    # Modifying the sub-list in the copied list
    shallow_copied_list[2][0] = 'a'
    
    print("Modified Original List:", original_list)  # Output: Modified Original List: [1, 2, ['a', 4]]
    print("Shallow Copied List After Modification:", shallow_copied_list)  # Output: Shallow Copied List After Modification: [1, 2, ['a', 4]]

# Call the function to demonstrate
demonstrate_shallow_copy()
```

### Deep Copy

A deep copy creates a new object and recursively copies all sub-objects into it. This means that changes to sub-objects in the copied object will not affect the original object.

```python
def demonstrate_deep_copy():
    # Example: Deep copying a dictionary with nested lists
    original_dict = {
        'a': 1,
        'b': [2, 3],
        'c': {'d': 4}
    }
    
    deep_copied_dict = copy.deepcopy(original_dict)
    
    print("Original Dictionary:", original_dict)  # Output: Original Dictionary: {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    print("Deep Copied Dictionary:", deep_copied_dict)  # Output: Deep Copied Dictionary: {'a': 1, 'b': [2, 3], 'c': {'d': 4}}

    # Modifying the nested list in the copied dictionary
    deep_copied_dict['b'][0] = 'x'
    
    print("Modified Original Dictionary:", original_dict)  # Output: Modified Original Dictionary: {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    print("Deep Copied Dictionary After Modification:", deep_copied_dict)  # Output: Deep Copied Dictionary After Modification: {'a': 1, 'b': ['x', 3], 'c': {'d': 4}}

# Call the function to demonstrate
demonstrate_deep_copy()
```

### Explanation

- **Shallow Copy**: This is useful when you want to create a copy of an object where sub-objects are shared. It is often used in cases where performance is critical.
  
- **Deep Copy**: This is recommended when you need a completely independent copy of the object and its sub-objects, ensuring that changes to one do not affect the other.

These examples demonstrate how to use the `copy` module to perform both shallow and deep copies, highlighting their respective use cases.
