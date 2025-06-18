# timeit - Measure execution time of small code snippets
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [Explanation:](#explanation)
3. [2. Measuring Multiple Statements](#2-measuring-multiple-statements)
4. [Explanation:](#explanation)
5. [3. Measuring Time for a Function](#3-measuring-time-for-a-function)
6. [Explanation:](#explanation)
7. [4. Using Timeit.Timer for Detailed Control](#4-using-timeittimer-for-detailed-control)
8. [Explanation:](#explanation)
9. [5. Measuring Time for Multiple Statements with Timer](#5-measuring-time-for-multiple-statements-with-timer)
10. [Explanation:](#explanation)



The `timeit` module in Python is a simple timing interface that helps measure short durations by running a given statement multiple times. It's particularly useful for benchmarking and profiling Python code. Below are comprehensive and well-documented examples demonstrating various functionalities of the `timeit` module.

### 1. Basic Usage

```python
import timeit

# Measure execution time of a simple addition
result = timeit.timeit("a + b", globals=globals(), number=1000)
print(f"Execution time: {result:.6f} seconds")
```

#### Explanation:
- **Function**: `timeit.timeit()`
  - This function measures the execution time of a specified code snippet.
  - The `stmt` parameter is the statement to be timed. It can include variables and functions defined in `globals` or `locals`.
  - `number` specifies how many times the statement should be executed.

### 2. Measuring Multiple Statements

```python
import timeit

# Measure execution time of multiple statements
result = timeit.timeit("""
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
""", globals=globals(), number=1000)
print(f"Execution time: {result:.6f} seconds")
```

#### Explanation:
- The `stmt` parameter can contain multiple statements separated by semicolons.
- This example demonstrates using the `map` function to perform element-wise addition of two lists.

### 3. Measuring Time for a Function

```python
import timeit

def my_function():
    return [i * i for i in range(1000)]

# Measure execution time of a defined function
result = timeit.timeit("my_function()", globals=globals(), number=1000)
print(f"Execution time: {result:.6f} seconds")
```

#### Explanation:
- You can define your own functions and measure their execution time directly.
- This example demonstrates using a list comprehension to create a list of squares of numbers from 0 to 999.

### 4. Using Timeit.Timer for Detailed Control

```python
import timeit

# Create a Timer object for more detailed control
timer = timeit.Timer("a + b", globals=globals())

# Measure execution time in seconds
result_seconds = timer.timeit(number=1000)
print(f"Execution time (seconds): {result_seconds:.6f}")

# Measure execution time in number of loops
result_loops = timer.repeat(3, 1000)  # Repeat the measurement 3 times with 1000 iterations each
print("Execution times per repetition:", result_loops)
```

#### Explanation:
- The `timeit.Timer` class provides more detailed control over timing.
  - `timeit.timeit()` measures the execution time of a statement in seconds.
  - `repeat(n, number)` repeats the measurement n times and returns a list of durations.

### 5. Measuring Time for Multiple Statements with Timer

```python
import timeit

timer = timeit.Timer("""
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
""", globals=globals())

# Measure execution time in seconds for multiple statements
result_seconds = timer.timeit(number=1000)
print(f"Execution time (seconds): {result_seconds:.6f}")

# Measure execution time in number of loops
result_loops = timer.repeat(3, 1000)  # Repeat the measurement 3 times with 1000 iterations each
print("Execution times per repetition:", result_loops)
```

#### Explanation:
- Using `timeit.Timer` allows you to measure multiple statements in a single block.
- This example demonstrates measuring the execution time of an `if` statement and a list comprehension.

### 6. Timing Code with Setup

```python
import timeit

# Measure execution time with setup code
result = timeit.timeit("result = sum(a)", globals=globals(), number=1000, setup="a = [i for i in range(1000)]")
print(f"Execution time: {result:.6f} seconds")
```

#### Explanation:
- The `setup` parameter allows you to define code that is executed before the timing starts.
  - This example demonstrates setting up a list and measuring the execution time of the `sum()` function on it.

### 7. Measuring Execution Time with Additional Options

```python
import timeit

# Measure execution time with additional options
result = timeit.timeit("result = sum(a)", globals=globals(), number=1000, repeat=3, setup="a = [i for i in range(1000)]")
print(f"Execution times (seconds): {result:.6f}")
```

#### Explanation:
- You can specify the number of repeats and additional options to control the measurement process.
  - This example demonstrates repeating the measurement three times and setting up a list.

### Conclusion

The `timeit` module is a powerful tool for measuring the execution time of small code snippets in Python. It provides flexibility through the use of parameters like `number`, `setup`, and `repeat`, allowing you to control the timing behavior according to your needs. These examples cover basic usage, multiple statements, function execution, detailed control with `timeit.Timer`, and more, demonstrating its versatility for performance analysis and benchmarking.

### Further Reading

- [Python 3.12 Documentation: timeit Module](https://docs.python.org/3/library/timeit.html)

This code is designed to be clear, concise, and suitable for inclusion in official documentation examples.
