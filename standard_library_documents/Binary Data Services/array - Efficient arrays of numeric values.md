# array - Efficient arrays of numeric values

The `array` module in Python provides a way to handle homogeneous sequences of numbers efficiently. This is particularly useful when you need to work with large collections of numerical data and need to perform fast operations on them.

Here are comprehensive code examples for various functionalities provided by the `array` module:

### 1. Creating Arrays

#### Example: Create an array of integers
```python
import array as arr

# Create an array of integers
int_array = arr.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)
```

#### Example: Create an array of floats
```python
import array as arr

# Create an array of floats
float_array = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print("Float Array:", float_array)
```

### 2. Accessing Elements

#### Example: Accessing elements by index
```python
import array as arr

# Access an element from the array
int_array = arr.array('i', [10, 20, 30, 40, 50])
print("Element at index 2:", int_array[2])  # Output: 30
```

#### Example: Accessing elements with out of bounds
```python
import array as arr

try:
    int_array = arr.array('i', [10, 20, 30])
    print("Element at index -1:", int_array[-1])  # Output: 30
    print("Element at index 5:", int_array[5])   # Raises IndexError
except IndexError as e:
    print(e)
```

### 3. Modifying Elements

#### Example: Modifying an element by index
```python
import array as arr

# Modify an element in the array
int_array = arr.array('i', [1, 2, 3, 4, 5])
int_array[2] = 10
print("Modified Integer Array:", int_array)
```

### 4. Appending Elements

#### Example: Appending a single element
```python
import array as arr

# Append a single element to the array
int_array = arr.array('i', [1, 2, 3])
int_array.append(4)
print("Array after appending 4:", int_array)
```

#### Example: Extending with multiple elements
```python
import array as arr

# Extend the array with another array
int_array = arr.array('i', [1, 2, 3])
other_int_array = arr.array('i', [4, 5, 6])
int_array.extend(other_int_array)
print("Array after extending:", int_array)
```

### 5. Operations on Arrays

#### Example: Adding elements using a loop
```python
import array as arr

# Create an empty integer array and add elements
int_array = arr.array('i')
for i in range(10):
    int_array.append(i * 2)
print("Array after adding elements with a loop:", int_array)
```

#### Example: Sorting the array
```python
import array as arr

# Sort an array
int_array = arr.array('i', [5, 3, 9, 1, 6])
int_array.sort()
print("Sorted Integer Array:", int_array)
```

### 6. Converting Arrays to Lists

#### Example: Convert array to a list
```python
import array as arr

# Convert an array to a list
int_array = arr.array('i', [1, 2, 3])
list_array = int_array.tolist()
print("Array converted to list:", list_array)
```

### 7. Concatenating Arrays

#### Example: Concatenating two arrays
```python
import array as arr

# Concatenate two integer arrays
int_array1 = arr.array('i', [1, 2, 3])
int_array2 = arr.array('i', [4, 5, 6])
concatenated_array = int_array1 + int_array2
print("Concatenated Integer Array:", concatenated_array)
```

### 8. Reversing an Array

#### Example: Reversing the array
```python
import array as arr

# Reverse an integer array
int_array = arr.array('i', [7, 8, 9])
reversed_array = int_array[::-1]
print("Reversed Integer Array:", reversed_array)
```

### 9. Indexing with Negative Numbers

#### Example: Accessing elements using negative indices
```python
import array as arr

# Access elements using negative indices
int_array = arr.array('i', [10, 20, 30])
print("Element at index -1:", int_array[-1])  # Output: 30
print("Element at index -2:", int_array[-2])  # Output: 20
```

### 10. Iterating Over Arrays

#### Example: Iterating over an array using a for loop
```python
import array as arr

# Iterate over an integer array
int_array = arr.array('i', [4, 8, 12])
for element in int_array:
    print(element)  # Output: 4, 8, 12
```

### 11. Comparing Arrays

#### Example: Comparing two arrays for equality
```python
import array as arr

# Compare two integer arrays for equality
int_array1 = arr.array('i', [1, 2, 3])
int_array2 = arr.array('i', [1, 2, 3])
print("Arrays are equal:", int_array1 == int_array2)  # Output: True
```

### 12. Arithmetic Operations

#### Example: Adding two arrays element-wise (supported for integer and float arrays)
```python
import array as arr

# Add two integer arrays element-wise
int_array1 = arr.array('i', [1, 2, 3])
int_array2 = arr.array('i', [4, 5, 6])
result_array = int_array1 + int_array2
print("Resulting Array after addition:", result_array)
```

### 13. String Formatting

#### Example: Formatting an array as a string (supported for integer and float arrays)
```python
import array as arr

# Format an array as a string
int_array = arr.array('i', [7, 8, 9])
formatted_string = str(int_array)
print("Array formatted as string:", formatted_string)  # Output: array('i', [7, 8, 9])
```

These examples cover the most common functionalities of the `array` module. Each example is well-documented to help you understand how to use each method effectively in your Python programs.
