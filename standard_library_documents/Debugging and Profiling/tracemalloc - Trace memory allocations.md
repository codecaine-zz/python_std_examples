# tracemalloc — Trace memory allocations

**Tracemalloc Example**
=====================

The `tracemalloc` module provides an interface for tracking object allocations and deallocations.

### Installing Tracemalloc

You can install the `tracemalloc` module using pip:

```bash
pip install py-trace
```

### Basic Usage

Here is a basic example of how to use `tracemalloc`:

```python
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# Example usage: create a list and append elements to it
numbers = []
for i in range(1000):
    numbers.append(i)

# Stop tracing memory allocations
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory allocation: {current / 1024:.2f} KB")
print(f"Peak memory allocation: {peak / 1024:.2f} KB")

# Get a snapshot of the current memory allocations
snapshot = tracemalloc.take_snapshot()

# Print the top 10 objects in the snapshot
for stat in snapshot.statistics('lineno'):
    print(stat)

# Stop tracing memory allocations
tracemalloc.stop()
```

This will start tracking memory allocations, create a list and append elements to it, stop tracking memory allocations, and then print out the current and peak memory allocations. It also prints out the top 10 objects in the snapshot.

### Tracking Memory Allocations by Frame

You can use `tracemalloc.take_snapshot()` with a frame argument to get a more detailed view of memory allocations:

```python
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

try:
    # Example usage: create a list and append elements to it
    numbers = []
    for i in range(1000):
        numbers.append(i)
except Exception as e:
    print(e)

# Stop tracing memory allocations
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory allocation: {current / 1024:.2f} KB")
print(f"Peak memory allocation: {peak / 1024:.2f} KB")

# Get a snapshot of the current memory allocations
snapshot = tracemalloc.take_snapshot()

# Print the top 10 objects in the snapshot, grouped by frame
for stat in snapshot.statistics('lineno'):
    print(stat)

# Stop tracing memory allocations
tracemalloc.stop()
```

In this example, `tracemalloc.take_snapshot()` is called with a frame argument to get a more detailed view of memory allocations.

### Filtering Memory Allocations

You can use the `snapshot.filter` method to filter memory allocations by type:

```python
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

try:
    # Example usage: create a list and append elements to it
    numbers = []
    for i in range(1000):
        numbers.append(i)
except Exception as e:
    print(e)

# Stop tracing memory allocations
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory allocation: {current / 1024:.2f} KB")
print(f"Peak memory allocation: {peak / 1024:.2f} KB")

# Get a snapshot of the current memory allocations
snapshot = tracemalloc.take_snapshot()

# Filter the snapshot to only show allocations for the 'numbers' list
snapshot.filter('frames')

# Print the top 10 objects in the filtered snapshot, grouped by frame
for stat in snapshot.statistics('lineno'):
    print(stat)

# Stop tracing memory allocations
tracemalloc.stop()
```

In this example, `snapshot.filter('frames')` is called to filter the snapshot to only show allocations for the `'numbers'` list.

### Capturing Memory Allocations

You can use `snapshot.capture()` to capture a snapshot of the current memory allocations:

```python
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

try:
    # Example usage: create a list and append elements to it
    numbers = []
    for i in range(1000):
        numbers.append(i)
except Exception as e:
    print(e)

# Capture a snapshot of the current memory allocations
snapshot = tracemalloc.take_snapshot()
capture = snapshot.capture()

print(capture.top(10))
```

In this example, `snapshot.capture()` is called to capture a snapshot of the current memory allocations. The resulting dictionary can be printed using `print(capture.top(10))`.
