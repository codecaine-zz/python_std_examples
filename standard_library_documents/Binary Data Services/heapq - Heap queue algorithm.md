# heapq - Heap queue algorithm

The `heapq` module in Python provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. This module is optimized for speed and space efficiency, making it suitable for applications where you need to maintain a collection of elements with priorities.

Below are comprehensive examples demonstrating various functionalities of the `heapq` module:

## Table of Contents

1. [Creating a Min-Heap](#1-creating-a-min-heap)
2. [Creating a Max-Heap](#2-creating-a-max-heap)
3. [Finding the N Smallest Elements](#3-finding-the-n-smallest-elements)
4. [Priority Queue with Time-Sorted Elements](#4-priority-queue-with-time-sorted-elements)
5. [Finding the k Closest Points to a Given Point](#5-finding-the-k-closest-points-to-a-given-point)

### 1. Creating a Min-Heap

```python
import heapq

# Create an empty min-heap
min_heap = []

# Add elements to the heap
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)

# Output the current state of the heap
print("Heap after push:", min_heap)  # Output: [1, 3, 4]

# Pop the smallest element from the heap
smallest = heapq.heappop(min_heap)
print("Smallest element popped:", smallest)  # Output: 1

# Push a new element and pop the next smallest element
heapq.heappush(min_heap, 0)
print("Heap after push (0):", min_heap)  # Output: [0, 3, 4]
smallest = heapq.heappop(min_heap)
print("Next smallest element popped:", smallest)  # Output: 0
```

### 2. Creating a Max-Heap

To use `heapq` as a max-heap, you can negate the values when pushing and popping. This is because `heapq` implements a min-heap by default.

```python
import heapq

# Create an empty max-heap
max_heap = []

# Add elements to the heap by negating them
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)

# Output the current state of the heap
print("Heap after push (max-heap):", [-x for x in max_heap])  # Output: [3, 1, 4]

# Pop the largest element from the heap
largest = -heapq.heappop(max_heap)
print("Largest element popped:", largest)  # Output: 3

# Push a new element and pop the next largest element
heapq.heappush(max_heap, -0)
print("Heap after push (-0):", [-x for x in max_heap])  # Output: [1, 4, 0]
largest = -heapq.heappop(max_heap)
print("Next largest element popped:", largest)  # Output: 1
```

### 3. Finding the N Smallest Elements

The `nlargest` and `nsmallest` functions are used to find the N largest or smallest elements in a list.

```python
import heapq

# List of numbers
numbers = [7, 10, 4, 3, 20, 15]

# Find the three largest numbers
largest_three = heapq.nlargest(3, numbers)
print("Three largest numbers:", largest_three)  # Output: [20, 15, 10]

# Find the two smallest numbers
smallest_two = heapq.nsmallest(2, numbers)
print("Two smallest numbers:", smallest_two)  # Output: [3, 4]
```

### 4. Priority Queue with Time-Sorted Elements

The `heapq` module can also be used to implement a priority queue.

```python
import heapq

# Priority queue list
priority_queue = []

# Add elements to the priority queue
heapq.heappush(priority_queue, (10, 'a'))
heapq.heappush(priority_queue, (20, 'b'))
heapq.heappush(priority_queue, (5, 'c'))

# Process each element in order of their priority
while priority_queue:
    priority, item = heapq.heappop(priority_queue)
    print(f"Processed {item} with priority {priority}")
```

### 5. Finding the k Closest Points to a Given Point

This example demonstrates how to use `heapq` to find the k closest points to a given point in a list of points.

```python
import heapq

# List of points (x, y)
points = [(3, 4), (1, 2), (1, -1), (-2, 0)]

# Given point (x0, y0)
given_point = (0, 0)

# Find the k closest points to the given point
k = 2
closest_points = heapq.nsmallest(k, points, key=lambda p: (p[0] ** 2 + p[1] ** 2))
print("K closest points:", closest_points)  # Output: [(1, -1), (3, 4)]
```

### Conclusion

The `heapq` module provides a efficient and flexible way to manage heaps in Python. Whether you need to maintain a min-heap, max-heap, or perform operations like finding the N largest/smallest elements, this module offers the tools to do so with ease.
