# concurrent.futures - Launching parallel tasks

Below are comprehensive code examples for the `concurrent.futures` module, which provides a high-level interface for asynchronously executing callables. The examples include various ways to use the module to launch parallel tasks.

## Table of Contents

1. [Using ThreadPoolExecutor](#1-using-threadpoolexecutor)
2. [Using ProcessPoolExecutor](#2-using-processpoolexecutor)
3. [Using ThreadPoolExecutor for I/O-bound Tasks](#3-using-threadpoolexecutor-for-i-o-bound-tasks)
4. [Using ProcessPoolExecutor for CPU-bound Tasks](#4-using-processpoolexecutor-for-cpu-bound-tasks)
5. [Using ThreadPoolExecutor and Future Objects](#5-using-threadpoolexecutor-and-future-objects)

### 1. Using ThreadPoolExecutor

The `ThreadPoolExecutor` class allows you to run multiple functions in separate threads. This is useful for I/O-bound operations where each task can be executed independently of others.

```python
import concurrent.futures
import time

def worker(number):
    """Worker function that takes an integer and returns its square."""
    print(f"Worker {number} starting")
    result = number * number
    print(f"Worker {number} finished, result: {result}")
    return result

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        future_to_number = {executor.submit(worker, i): i for i in range(10)}
        
        # Process results
        for future in concurrent.futures.as_completed(future_to_number):
            number = future_to_number[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"Worker {number} generated an exception: {exc}")
            else:
                print(f"Worker {number} completed with result: {result}")

if __name__ == "__main__":
    main()
```

### 2. Using ProcessPoolExecutor

The `ProcessPoolExecutor` class allows you to run multiple functions in separate processes. This is useful for CPU-bound operations where tasks are independent and can be executed concurrently.

```python
import concurrent.futures
import time

def worker(number):
    """Worker function that takes an integer and returns its square."""
    print(f"Worker {number} starting")
    result = number * number
    print(f"Worker {number} finished, result: {result}")
    return result

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        future_to_number = {executor.submit(worker, i): i for i in range(10)}
        
        # Process results
        for future in concurrent.futures.as_completed(future_to_number):
            number = future_to_number[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"Worker {number} generated an exception: {exc}")
            else:
                print(f"Worker {number} completed with result: {result}")

if __name__ == "__main__":
    main()
```

### 3. Using ThreadPoolExecutor for I/O-bound Tasks

The `ThreadPoolExecutor` can also be used for I/O-bound tasks by ensuring that each task does not require a lot of CPU resources.

```python
import concurrent.futures
import time

def worker(number):
    """Worker function that takes an integer and sleeps for it."""
    print(f"Worker {number} starting")
    time.sleep(number)
    print(f"Worker {number} finished")
    
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        future_to_number = {executor.submit(worker, i): i for i in range(10)}
        
        # Process results
        for future in concurrent.futures.as_completed(future_to_number):
            number = future_to_number[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"Worker {number} generated an exception: {exc}")
            else:
                print(f"Worker {number} completed with result: {result}")

if __name__ == "__main__":
    main()
```

### 4. Using ProcessPoolExecutor for CPU-bound Tasks

For CPU-bound tasks, you might want to use `ProcessPoolExecutor` because each process has its own memory space.

```python
import concurrent.futures
import math

def worker(data):
    """Worker function that takes a list of numbers and calculates their sum."""
    print(f"Worker processing data with {len(data)} elements")
    result = sum(data)
    print(f"Worker completed processing, total: {result}")
    return result

def main():
    data_chunks = [range(1000), range(1000), range(1000)]
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        future_to_data = {executor.submit(worker, chunk): chunk for chunk in data_chunks}
        
        # Process results
        for future in concurrent.futures.as_completed(future_to_data):
            chunk = future_to_data[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"Worker processing {chunk} generated an exception: {exc}")
            else:
                print(f"Worker processed {chunk} with total: {result}")

if __name__ == "__main__":
    main()
```

### 5. Using ThreadPoolExecutor and Future Objects

You can also use `Future` objects to manage the results of asynchronous tasks.

```python
import concurrent.futures
import time

def worker(number):
    """Worker function that takes an integer and returns its square."""
    print(f"Worker {number} starting")
    time.sleep(number)
    result = number * number
    print(f"Worker {number} finished, result: {result}")
    return result

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        future_list = [executor.submit(worker, i) for i in range(10)]
        
        # Process results
        for future in concurrent.futures.as_completed(future_list):
            try:
                result = future.result()
            except Exception as exc:
                print(f"Worker finished with an exception: {exc}")
            else:
                print(f"Worker completed with result: {result}")

if __name__ == "__main__":
    main()
```

These examples demonstrate how to use `concurrent.futures` for launching parallel tasks in Python, including both thread-based and process-based execution. Each example includes comments explaining the purpose of each part of the code.
