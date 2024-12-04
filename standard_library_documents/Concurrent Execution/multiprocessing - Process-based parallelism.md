# multiprocessing — Process-based parallelism

**Multiprocessing Module**
==========================

The `multiprocessing` module provides support for spawning new Python processes and managing their resources.

**Importing the Module**
------------------------

```python
import multiprocessing
```

**Creating a New Process**
---------------------------

You can create a new process by creating a new `Process` object and passing it an callable function that will be executed in the new process:

```python
def worker(num):
    """Simulate some work"""
    print(f"Worker {num} is working")
    # Add your code here

if __name__ == "__main__":
    # Create two processes, one for each worker
    p1 = multiprocessing.Process(target=worker, args=(1,))
    p2 = multiprocessing.Process(target=worker, args=(2,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    print("All workers have finished")
```

**Using `Pool`**
-----------------

You can also use a `Pool` of worker processes to execute multiple tasks in parallel. The `Pool` class takes a list of callable functions as an argument and returns an object that you can call to execute the tasks:

```python
import multiprocessing

def square(x):
    """Return the square of x"""
    return x ** 2

if __name__ == "__main__":
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Apply the square function to a list of numbers in parallel
        results = pool.map(square, [1, 2, 3, 4])

    print(results)
```

**Using `ProcessPoolExecutor`**
---------------------------------

The `ProcessPoolExecutor` class is similar to the `Pool` class, but it provides more features and flexibility:

```python
import multiprocessing

def square(x):
    """Return the square of x"""
    return x ** 2

if __name__ == "__main__":
    # Create a pool of 4 worker processes
    with multiprocessing.ProcessPoolExecutor(max_workers=4) as executor:
        # Submit tasks to the pool and retrieve the results
        results = list(executor.map(square, [1, 2, 3, 4]))

    print(results)
```

**Using `Pool.apply_async`**
-----------------------------

The `apply_async` method allows you to execute a task asynchronously in the pool:

```python
import multiprocessing

def square(x):
    """Return the square of x"""
    return x ** 2

if __name__ == "__main__":
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Execute a task asynchronously in the pool
        p = pool.apply_async(square, args=(5,))
        print(f"Task started: {p.id}")

        # Wait for the task to finish
        p.get()
```

**Using `Pool.submit`**
-------------------------

The `submit` method allows you to execute a task synchronously in the pool:

```python
import multiprocessing

def square(x):
    """Return the square of x"""
    return x ** 2

if __name__ == "__main__":
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Execute a task synchronously in the pool
        p = pool.submit(square, 5)
        print(f"Task started: {p.id}")

        # Wait for the task to finish and retrieve the result
        result = p.result()
```

**Sharing Data Between Processes**
---------------------------------

You can share data between processes using shared memory or queues:

```python
import multiprocessing

def worker(q):
    """Simulate some work"""
    q.put("Worker has finished")

if __name__ == "__main__":
    # Create a queue to share data between processes
    q = multiprocessing.Queue()

    # Create two processes, one for each worker
    p1 = multiprocessing.Process(target=worker, args=(q,))
    p2 = multiprocessing.Process(target=worker, args=(q,))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    print(q.get())  # Should print "Worker has finished"
```

**Exiting a Process**
------------------------

You can exit a process using the `join` method:

```python
import multiprocessing

def worker():
    """Simulate some work"""
    print("Worker is working")

if __name__ == "__main__":
    # Create a process for each worker
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=worker)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
```

**Process Termination**
-------------------------

The `multiprocessing` module provides a number of methods and functions that can be used to terminate a process:

```python
import multiprocessing

def worker():
    """Simulate some work"""
    print("Worker is working")

if __name__ == "__main__":
    # Create a process for each worker
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=worker)

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    # Terminate the main process
    exit(42)  # Exit with status code 42
```
