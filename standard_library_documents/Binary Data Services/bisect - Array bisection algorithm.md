# bisect - Array bisection algorithm

The `bisect` module in Python provides a set of functions that perform binary search on sorted arrays. This module is particularly useful when you need to efficiently find the position where an item should be inserted into a list to maintain its sorted order.

Here are comprehensive code examples for each functionality provided by the `bisect` module:

## Table of Contents

1. [Bisection Search](#example-1-bisection-search)
2. [Bisection Search Using `bisect_right` or `bisect`](#example-2-bisection-search-using-bisect_right-or-bisect)
3. [Bisection Search for Insertion](#example-3-bisection-search-for-insertion)
4. [Bisection Search for Deletion](#example-4-bisection-search-for-deletion)
5. [Bisection Search with Key Function](#example-5-bisection-search-with-key-function)
6. [Bisection Search for Rightmost Position](#example-6-bisection-search-for-rightmost-position)

### Example 1: Bisection Search

```python
import bisect

# List of numbers
numbers = [1, 3, 5, 7, 9]

# Element to search for
search_value = 6

# Find the position where the element should be inserted to maintain sorted order
insert_position = bisect.bisect_left(numbers, search_value)

print(f"The element {search_value} can be inserted at index {insert_position} to maintain the list in sorted order.")
```

### Example 2: Bisection Search Using `bisect_right` or `bisect`

The `bisect_right` function is similar to `bisect_left`, but it returns the insertion point where the element should be inserted to maintain sorted order, ensuring that duplicates are added at the rightmost position.

```python
import bisect

# List of numbers with duplicates
numbers = [1, 2, 2, 3, 4, 5]

# Element to search for
search_value = 2

# Find the position where the element should be inserted
insert_position_right = bisect.bisect(numbers, search_value)

print(f"The element {search_value} can be inserted at index {insert_position_right} to maintain the list in sorted order.")
```

### Example 3: Bisection Search for Insertion

```python
import bisect

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Element to insert
insert_value = 7

# Find the position where the element should be inserted to maintain sorted order
insert_position_insert = bisect.bisect_left(numbers, insert_value)

# Insert the element at the found position
numbers.insert(insert_position_insert, insert_value)

print(f"List after inserting {insert_value}: {numbers}")
```

### Example 4: Bisection Search for Deletion

```python
import bisect

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Element to delete
delete_value = 3

# Find the position where the element should be deleted
insert_position_delete = bisect.bisect_left(numbers, delete_value)

# Delete the element if it exists
if insert_position_delete < len(numbers) and numbers[insert_position_delete] == delete_value:
    del numbers[insert_position_delete]

print(f"List after deleting {delete_value}: {numbers}")
```

### Example 5: Bisection Search with Key Function

You can also use a key function to perform the bisect operation on custom keys.

```python
import bisect

# List of tuples where each tuple is (value, index)
tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

# Element and its corresponding key for search
search_value = 3
key_func = lambda x: x[0]

# Find the position where the element should be inserted based on the key function
insert_position_key = bisect.bisect_left(tuples, (search_value, ''), key=key_func)

print(f"The element {search_value} can be inserted at index {insert_position_key} based on the key function.")
```

### Example 6: Bisection Search for Rightmost Position

The `bisect_right` function is useful when you need to find the rightmost position where an element should be inserted to maintain sorted order.

```python
import bisect

# List of numbers with duplicates
numbers = [1, 2, 2, 3, 4, 5]

# Element to search for
search_value = 2

# Find the position where the element should be inserted
insert_position_right = bisect.bisect_right(numbers, search_value)

print(f"The rightmost occurrence of {search_value} is at index {insert_position_right}.")
```

These examples cover various use cases of the `bisect` module, demonstrating its versatility in maintaining sorted lists and performing efficient binary searches.
