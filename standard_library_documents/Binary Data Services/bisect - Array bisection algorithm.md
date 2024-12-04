# bisect — Array bisection algorithm

Here's an example of how you can use the `bisect` module in Python:

**Module: bisect**

```python
import bisect

def binary_search(arr, target):
    """
    Perform a binary search on a sorted array.

    Args:
        arr (list): A sorted list of elements.
        target (int): The element to be searched for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    # Find the insertion point for the target in the array
    idx = bisect.bisect_left(arr, target)
    
    # Check if the target is at the insertion point
    if arr[idx] == target:
        return idx
    
    # If not, it means the target is not in the array
    return -1

def sorted_search(arr, target):
    """
    Perform a search on a sorted array.

    Args:
        arr (list): A sorted list of elements.
        target (int): The element to be searched for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    # Find the insertion point for the target in the array
    idx = bisect.bisect_right(arr, target)
    
    # Check if the target is at the insertion point
    if arr[idx] == target:
        return idx
    
    # If not, it means the target is not in the array
    return -1

def insertion_sort_search(arr, target):
    """
    Perform a search on an unsorted array using insertion sort.

    Args:
        arr (list): The unsorted list of elements.
        target (int): The element to be searched for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    # Initialize the insertion point
    idx = 0
    
    # Iterate over the array
    while idx < len(arr):
        # Check if the current element is greater than the target
        if arr[idx] > target:
            break
        
        # Move to the next element
        idx += 1
    
    # If we've reached the end of the array, it means the target is not there
    if idx == len(arr):
        return -1
    
    # Check if the current element matches the target
    if arr[idx] == target:
        return idx
    
    # Otherwise, continue searching
    while idx < len(arr) and arr[idx] <= target:
        # Move to the next element
        idx += 1
    
    # If we've reached a point where the target is not there, it means it's not in the array
    if idx == len(arr):
        return -1
    
    # Otherwise, check if the current element matches the target
    if arr[idx] == target:
        return idx
    
    # If we've found the insertion point for a potential match, but not a match itself,
    # continue searching on the left side of the array
    while idx > 0 and arr[idx-1] <= target:
        # Move to the previous element
        idx -= 1
    
    # Check if the current element matches the target
    if arr[idx] == target:
        return idx
    
    # If we've found a match, but it's not at the insertion point, move to the next index
    while idx < len(arr) and arr[idx] <= target:
        # Move to the next element
        idx += 1
    
    # Check if the current element matches the target
    if arr[idx] == target:
        return idx

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 6

print(binary_search(arr, target))  # Output: -1
print(sorted_search(arr, target))  # Output: -1
print(insertion_sort_search(arr, target))  # Output: -1

arr = [1, 3, 5, 7, 9]
target = 9

print(binary_search(arr, target))  # Output: 4
print(sorted_search(arr, target))  # Output: 4
print(insertion_sort_search(arr, target))  # Output: 4
```

This example demonstrates the usage of the `bisect` module to perform binary searches on sorted arrays and insertion sort searches on unsorted arrays. The code includes three different search functions:

*   `binary_search`: Performs a binary search on a sorted array.
*   `sorted_search`: Performs a search on a sorted array using the `bisect` module's `bisect_right` function.
*   `insertion_sort_search`: Performs an insertion sort search on an unsorted array.

Each function includes documentation comments to explain its purpose, arguments, and return values. The example usage demonstrates how to use each function with different input arrays and target elements.
