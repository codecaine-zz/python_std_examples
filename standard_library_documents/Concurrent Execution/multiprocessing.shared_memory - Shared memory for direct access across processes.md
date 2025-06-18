# multiprocessing.shared_memory - Shared memory for direct access across processes

The `multiprocessing.shared_memory` module provides a way to create shared memory objects that can be accessed by multiple processes directly. This is useful for sharing large amounts of data between processes without having to copy it. Below are comprehensive examples of how to use this module, including creating and accessing shared memory objects in Python 3.12.

## Table of Contents

1. [Creating a Shared Memory Object](#example-1-creating-a-shared-memory-object)
2. [Creating a Shared Memory Object for an Integer](#example-2-creating-a-shared-memory-object-for-an-integer)
3. [Creating a Shared Memory Object for a Float](#example-3-creating-a-shared-memory-object-for-a-float)
4. [Creating a Shared Memory Object for a List](#example-4-creating-a-shared-memory-object-for-a-list)
5. [Creating and Accessing Shared Memory Objects Across Multiple Processes](#example-5-creating-and-accessing-shared-memory-objects-across-multiple-processes)
6. [Creating and Accessing Shared Memory Objects with Initial Data](#example-6-creating-and-accessing-shared-memory-objects-with-initial-data)

### Example 1: Creating a Shared Memory Object

This example demonstrates how to create a shared memory object and map it into a shared array.

```python
import multiprocessing as mp


def worker(shared_array):
    # Accessing the shared array from the worker process
    for i in range(len(shared_array)):
        shared_array[i] += 1

if __name__ == "__main__":
    # Create a shared memory object of type 'i' (integer) with size 10
    shm = mp.Array('i', 10)

    # Start a new process that will modify the shared array
    p = mp.Process(target=worker, args=(shm,))
    p.start()
    p.join()

    # Print the modified shared array
    print("Modified shared array:", list(shm))
```

### Example 2: Creating a Shared Memory Object for an Integer

This example shows how to create a shared memory object of type 'i' (int) and initialize it with a specific value.

```python
import multiprocessing as mp

def worker(shared_int):
    # Accessing the shared integer from the worker process
    print("Initial shared integer:", shared_int.value)
    shared_int.value += 1

if __name__ == "__main__":
    # Create a shared memory object of type 'i' (int) with size 1
    shm = mp.Value('i', 5)

    # Start a new process that will modify the shared integer
    p = mp.Process(target=worker, args=(shm,))
    p.start()
    p.join()

    # Print the modified shared integer
    print("Modified shared integer:", shm.value)
```

### Example 3: Creating a Shared Memory Object for a Float

This example demonstrates how to create a shared memory object of type 'f' (float) and initialize it with a specific value.

```python
import multiprocessing as mp

def worker(shared_float):
    # Accessing the shared float from the worker process
    print("Initial shared float:", shared_float.value)
    shared_float.value += 0.1

if __name__ == "__main__":
    # Create a shared memory object of type 'f' (float) with size 1
    shm = mp.Value('f', 5.0)

    # Start a new process that will modify the shared float
    p = mp.Process(target=worker, args=(shm,))
    p.start()
    p.join()

    # Print the modified shared float
    print("Modified shared float:", shm.value)
```

### Example 4: Creating a Shared Memory Object for a List

This example shows how to create a shared memory object of type 'l' (list) and initialize it with a list of values.

```python
import multiprocessing as mp

def worker(shared_list):
    # Accessing the shared list from the worker process
    print("Initial shared list:", shared_list)
    for i in range(len(shared_list)):
        shared_list[i] += 1

if __name__ == "__main__":
    # Create a manager object to manage shared state
    manager = mp.Manager()
    # Create a shared list with the manager
    shm = manager.list([1, 2, 3, 4, 5])

    # Start a new process that will modify the shared list
    p = mp.Process(target=worker, args=(shm,))
    p.start()
    p.join()

    # Print the modified shared list
    print("Modified shared list:", shm)
```

### Example 5: Creating and Accessing Shared Memory Objects Across Multiple Processes

This example demonstrates how to create and access shared memory objects in a more complex scenario involving multiple processes.

```python
import multiprocessing as mp

def worker(shared_array):
    # Accessing the shared array from the worker process
    for i in range(len(shared_array)):
        shared_array[i] += 1

def main():
    # Create a shared memory object of type 'i' (integer) with size 10
    shm = mp.Array('i', 10)

    # Start multiple processes that will modify the shared array
    processes = []
    for _ in range(5):
        p = mp.Process(target=worker, args=(shm,))
        p.start()
        processes.append(p)

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Print the final modified shared array
    print("Final shared array:", list(shm))

if __name__ == "__main__":
    main()
```

### Example 6: Creating and Accessing Shared Memory Objects with Initial Data

This example demonstrates how to create a shared memory object of type 'l' (list) with initial data and modify it from multiple processes.

```python
import multiprocessing as mp

def worker(shared_list):
    # Accessing the shared list from the worker process
    for i in range(len(shared_list)):
        shared_list[i] += 1

def main():
    # Create a manager object to manage shared data
    manager = mp.Manager()
    # Create a shared list with initial data and size 5
    shm = manager.list([1, 2, 3, 4, 5])

    # Start multiple processes that will modify the shared list
    processes = []
    for _ in range(5):
        p = mp.Process(target=worker, args=(shm,))
        p.start()
        processes.append(p)

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Print the final modified shared list
    print("Final shared list:", shm)

if __name__ == "__main__":
    main()
```

These examples cover various scenarios of using `multiprocessing.shared_memory` to share data between processes. Each example includes comments explaining key steps and demonstrates how to handle different types of shared memory objects (e.g., strings, integers, floats, lists).
