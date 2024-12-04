# timeit — Measure execution time of small code snippets

**Timeit Module**
================

The `timeit` module provides a simple way to measure the execution time of small code snippets.

**Example Use Cases:**

*   Measuring performance of different algorithms
*   Comparing execution times of different code implementations
*   Optimizing code for better performance

**Code Examples:**

### 1. Basic Usage

```python
import timeit

# Define a simple function to measure
def add_numbers(a, b):
    return a + b

# Create a timer object
timer = timeit.Timer(lambda: add_numbers(2, 3))

# Measure the execution time of the function
execution_time = timer.timeit(number=1000000)

print(f"Execution time: {execution_time:.6f} seconds")
```

### 2. Using Setup and Timeit

```python
import timeit

# Define a simple setup for the measurement
def add_numbers(a, b):
    return a + b

# Create a timer object with setup
timer = timeit.Timer('add_numbers(2, 3)', 'a, b')

# Measure the execution time of the function
execution_time = timer.timeit(number=1000000)

print(f"Execution time: {execution_time:.6f} seconds")
```

### 3. Using Loop and Timeit

```python
import timeit

# Define a simple loop for the measurement
def add_numbers(a, b):
    result = 0
    for i in range(1000000):
        result += a + b
    return result

# Create a timer object with setup
timer = timeit.Timer('add_numbers(2, 3)', 'a, b')

# Measure the execution time of the function
execution_time = timer.timeit(number=1)

print(f"Execution time: {execution_time:.6f} seconds")
```

### 4. Using Timer Function

```python
import timeit

# Define a simple function to measure
def add_numbers(a, b):
    return a + b

# Use the timer function to measure execution time
with timeit.timer('add_numbers(2, 3)') as timer:
    for i in range(1000000):
        result = add_numbers(2, 3)

print(f"Execution time: {timer.total_time:.6f} seconds")
```

### 5. Measuring Execution Time with Multiple Runs

```python
import timeit

# Define a simple function to measure
def add_numbers(a, b):
    return a + b

# Create multiple timer objects with setup
timers = [
    timeit.Timer('add_numbers(2, 3)', 'a, b'),
    timeit.Timer('add_numbers(2, 4)', 'a, b'),
    timeit Timer('add_numbers(5, 6)', 'a, b')
]

# Measure the execution time of each function
execution_times = [timer.timeit(number=1000000) for timer in timers]

print(f"Execution times: {execution_times}")
```

### 6. Using Setup and Timeit with Loop

```python
import timeit

# Define a simple setup for the measurement
def add_numbers(a, b):
    result = 0
    for i in range(1000000):
        result += a + b
    return result

# Create multiple timer objects with setup
timers = [
    timeit.Timer('add_numbers(2, 3)', 'a, b'),
    timeit.Timer('add_numbers(4, 5)', 'a, b')
]

# Measure the execution time of each function
execution_times = [timer.timeit(number=1) for timer in timers]

print(f"Execution times: {execution_times}")
```

Note that the `timeit` module uses a variety of techniques to measure execution time, including measuring the number of calls to a function, timing loops, and using benchmarking frameworks. The above examples demonstrate some of these techniques.
