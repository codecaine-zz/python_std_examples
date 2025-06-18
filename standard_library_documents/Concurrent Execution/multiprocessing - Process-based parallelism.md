# multiprocessing - Process-based parallelism

Below are comprehensive examples of how to use various functionalities provided by the `multiprocessing` module in Python, along with detailed comments explaining each step.

## Table of Contents

1. [Basic Multiprocessing](#1-basic-multiprocessing)
2. [Using Process Class](#2-using-process-class)
3. [Sharing Data Between Processes](#3-sharing-data-between-processes)
4. [Handling Exceptions in Processes](#4-handling-exceptions-in-processes)
5. [Using Queue for Inter-Process Communication](#5-using-queue-for-inter-process-communication)
6. [Using Lock for Synchronization](#6-using-lock-for-synchronization)

### 1. Basic Multiprocessing

```python
import multiprocessing
from multiprocessing import Pool
import os

def worker(x):
    """Example function to be executed in a separate process."""
    return x * x

if __name__ == '__main__':
    # Create a pool of worker processes using all system cores
    with Pool(processes=os.process_cpu_count()) as pool:
        # Use the map method to apply the worker function to a list of numbers
        results = pool.map(worker, [1, 2, 3, 4, 5])
    print(os.process_cpu_count())
    print("Results:", results)

```

### 2. Using `Process` Class

```python
import multiprocessing

def worker(x):
    """Example function to be executed in a separate process."""
    return x * x

if __name__ == '__main__':
    # Define a target function for the Process class
    def target_function():
        print("Running in a separate process")

    # Create a Process object and start it
    p = multiprocessing.Process(target=target_function)
    p.start()
    p.join()  # Wait for the process to complete

    print("Process completed")
```

### 3. Sharing Data Between Processes

```python
import multiprocessing
from multiprocessing import Manager

def modify_list(data):
    """Function to modify a shared list."""
    data.append(100)

if __name__ == '__main__':
    # Create a manager object for shared objects
    with Manager() as manager:
        # Use the list object from the manager
        shared_data = manager.list([1, 2, 3])
        
        # Spawn a process to modify the shared data
        p = multiprocessing.Process(target=modify_list, args=(shared_data,))
        p.start()
        p.join()

        print("Shared data after modification:", shared_data)
```

### 4. Handling Exceptions in Processes

```python
import multiprocessing
from multiprocessing import Pool

def worker(x):
    """Example function to be executed in a separate process."""
    if x == 0:
        raise ValueError("Division by zero")
    return 1 / x

if __name__ == '__main__':
    with Pool(processes=2) as pool:
        results = []  # Initialize results to ensure it is defined
        try:
            results = pool.map(worker, [5, 0, 3])
        except Exception as e:
            print(f"An error occurred: {e}")

        # Note: The second and third elements in the list are None because of the exception
        print("Results:", results)
```

### 5. Using `Queue` for Inter-Process Communication

```python
import multiprocessing
from multiprocessing import Queue

def producer(q):
    """Producer function to add items to a queue."""
    q.put(10)
    q.put(20)

def consumer(q):
    """Consumer function to retrieve items from the queue."""
    while True:
        item = q.get()
        if item is None:
            break
        print("Received:", item)

if __name__ == '__main__':
    # Create a queue object
    q = Queue()

    # Start producer and consumer processes
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    # Wait for all processes to complete
    p1.join()
    q.put(None)  # Signal the consumer process to exit
    p2.join()
```

### 6. Using `Lock` for Synchronization

```python
import multiprocessing
from multiprocessing import Lock, Manager

def shared_task(lock, counter):
    """Function that increments a counter and prints its value."""
    with lock:
        print(f"Thread {multiprocessing.current_process().name}: Lock acquired")
        counter.value += 1
        print(f"Counter value: {counter.value}")

if __name__ == '__main__':
    # Create a lock object
    lock = Lock()

    # Define a counter using Value from the Manager class for shared data
    with Manager() as manager:
        counter = manager.Value('i', 0)

        # Start multiple processes to increment the counter
        processes = [multiprocessing.Process(target=shared_task, args=(lock, counter)) for _ in range(10)]
        for p in processes:
            p.start()

        # Wait for all processes to complete
        for p in processes:
            p.join()

```

These examples cover a range of functionalities provided by the `multiprocessing` module, including creating and managing processes, sharing data between them, handling exceptions, using queues for inter-process communication, and synchronizing access to shared resources.
