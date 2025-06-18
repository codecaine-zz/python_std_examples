# trace - Trace or track Python statement execution
## Table of Contents

1. [Example 1: Basic Tracing with `trace.tracemalloc`](#example-1-basic-tracing-with-tracetracemalloc)
2. [Example 2: Tracing Execution with `trace.Trace`](#example-2-tracing-execution-with-tracetrace)
3. [Example 3: Tracing with Custom Filters](#example-3-tracing-with-custom-filters)
4. [Example 4: Tracing with Custom Output](#example-4-tracing-with-custom-output)



The `trace` module is a part of the Python Standard Library that provides a way to trace the execution of Python programs. It allows you to instrument your program to log each statement as it executes, which can be useful for debugging and profiling.

Below are comprehensive code examples demonstrating various functionalities provided by the `trace` module:

### Example 1: Basic Tracing with `trace.tracemalloc`

```python
import trace
import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

try:
    # Your code to be traced goes here
    for i in range(100000):
        x = [i] * 1000000
except KeyboardInterrupt:
    pass

# Print the top 10 memory allocation entries
print(tracemalloc.get_top(10))

# Stop tracing memory allocations and print statistics
tracemalloc.stop()
```

**Explanation:**
- `trace.tracemalloc.start()` starts monitoring memory allocations.
- The code block to be traced is wrapped in a try-except block to allow graceful termination with a keyboard interrupt (Ctrl+C).
- `tracemalloc.get_top(10)` retrieves the top 10 memory allocation entries, which can help identify memory leaks or inefficient usage.
- `tracemalloc.stop()` stops monitoring and prints statistics.

### Example 2: Tracing Execution with `trace.Trace`

```python
import trace

# Define a function to be traced
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Create a Trace object
tracer = trace.Trace(
    countcalls=True, # Count calls made by functions
    trace=2,         # Trace function calls with level 2 (deep)
    countlines=True   # Count lines of code executed
)

# Run the function under tracing
tracer.run('factorial(10)')

# Report the results
tracer.results().write_results(show_missing=True, coverdir=".")
```

**Explanation:**
- `trace.Trace` is used to create a tracer object with options to count function calls, trace function calls deeply, and count lines of code executed.
- The `run` method executes the specified Python expression (e.g., `factorial(10)`) under tracing.
- `tracer.results().write_results(show_missing=True, coverdir=".")` writes the results to a file in a directory named `.`, showing missing calls and providing a coverage report.

### Example 3: Tracing with Custom Filters

```python
import trace

# Define a custom filter function
def filter_frame(frame):
    # Exclude frames from specific modules or functions
    if frame.f_code.co_filename.startswith('/usr/lib/python3'):
        return False
    if 'trace.py' in frame.f_code.co_name:
        return False
    return True

# Create a Trace object with a custom filter
tracer = trace.Trace(
    countcalls=True,
    trace=2,
    countlines=True,
    ignore_function=filter_frame
)

# Run the function under tracing
tracer.run('factorial(10)')

# Report the results
tracer.results().write_results(show_missing=True, coverdir=".")
```

**Explanation:**
- A custom filter function `filter_frame` is defined to exclude frames from specific modules or functions.
- The `ignore_function` option in `trace.Trace` uses this filter to skip certain frames during tracing.
- The results are written to a file with missing calls and coverage report.

### Example 4: Tracing with Custom Output

```python
import trace

# Define custom output functions
def write_start(message):
    print(f"Starting {message}")

def write_end(message):
    print(f"Ending {message}")

# Create a Trace object with custom output
tracer = trace.Trace(
    countcalls=True,
    trace=2,
    countlines=True,
    start_func=write_start,
    finish_func=write_end
)

# Run the function under tracing
tracer.run('factorial(10)')

# Report the results
tracer.results().write_results(show_missing=True, coverdir=".")
```

**Explanation:**
- Custom start and end functions `write_start` and `write_end` are defined to log messages at the beginning and end of each traced function.
- The `start_func` and `finish_func` options in `trace.Trace` use these functions to log trace events.
- The results are written to a file with missing calls and coverage report.

These examples demonstrate various ways to use the `trace` module for tracing Python execution, including memory allocation monitoring, detailed execution traces, custom filtering, and custom output.
