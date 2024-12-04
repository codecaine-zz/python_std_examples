# threading — Thread-based parallelism

**Threading Module**
====================
The `threading` module provides a way to create multiple threads within a single process, which can improve responsiveness and throughput in concurrent programs.

### Importing the Module

```python
import threading
```

### Creating Threads

You can create a new thread by creating an instance of the `Thread` class and passing a target function, arguments, and any additional keyword arguments to its constructor.

```python
def print_numbers():
    for i in range(5):
        print(i)

# Create a new thread that runs the print_numbers function
thread = threading.Thread(target=print_numbers)
thread.start()  # Start the thread

# The main program continues running here
for i in range(10):
    print(f"Main: {i}")
```

### Main Function in the Thread

You can also pass a main function to be executed when the thread is created.

```python
def main_function():
    for i in range(5):
        print(i)

def print_numbers():
    # Wait for the main function to finish before starting its execution
    threading.event.wait()
    for i in range(10):
        print(f"Thread: {i}")

# Create a new thread that runs both functions concurrently
thread = threading.Thread(target=main_function, args=(print_numbers,))
thread.start()  # Start the thread

# Wait for the main function to finish before exiting
for _ in range(15):
    pass
```

### Synchronization Using Locks

When multiple threads access shared resources, you may need to synchronize their execution to prevent data corruption or inconsistencies.

```python
import threading

lock = threading.Lock()

def increment_counter():
    for i in range(10**6):  # Simulate some work
        with lock:  # Acquire the lock before accessing shared resource
            global counter  # Access the global variable counter
            counter += 1

counter = 0  # Shared resource

# Create two threads that increment the counter concurrently
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before checking the final value of the counter
thread1.join()
thread2.join()

print(f"Final counter: {counter}")  # Should be equal to 20,000,000

```

### Synchronization Using Semaphores

Semaphores can be used to limit the number of concurrent accesses to a shared resource.

```python
import threading
import time

semaphore = threading.Semaphore(3)  # Allow at most 3 threads to access the resource concurrently

def access_resource():
    semaphore.acquire()  # Acquire the semaphore before accessing the shared resource
    try:
        print("Accessing the shared resource...")
        time.sleep(1)
    finally:
        print(f"Released semaphore")  # Release the semaphore after accessing the shared resource
        semaphore.release()

# Create five threads that access the shared resource concurrently
threads = []
for _ in range(5):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()  # Start all threads

# Wait for all threads to finish before checking their status
for thread in threads:
    thread.join()
```

### Synchronization Using Events

Events can be used to signal the end of a task.

```python
import threading
import time

event = threading.Event()

def run_task():
    print("Task started")
    time.sleep(2)
    print("Task finished")
    event.set()  # Signal the end of the task

thread = threading.Thread(target=run_task)

# Start the thread and wait for it to finish
thread.start()
thread.join()

# Wait for the event to be set before proceeding
event.wait()
print("Main program continues running")
```

### Synchronization Using Condition Variables

Condition variables can be used to synchronize threads waiting for a specific condition.

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

def worker(counter):
    while True:
        counter.increment()
        print(f"Worker: {counter.value}")
        if counter.value == 10:
            break

counter = Counter()

# Create two threads that access the shared resource concurrently
thread1 = threading.Thread(target=worker, args=(counter,))
thread2 = threading.Thread(target=worker, args=(counter,))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before checking the final value of the counter
thread1.join()
thread2.join()
```

### Synchronization Using RLocks

RLocks are a variation of locks that allow a thread to acquire the lock multiple times.

```python
import threading

rlock = threading.RLock()

def increment_counter():
    for i in range(10**6):  # Simulate some work
        with rlock:  # Acquire the lock before accessing shared resource
            global counter  # Access the global variable counter
            counter += 1

counter = 0  # Shared resource

# Create two threads that increment the counter concurrently
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before checking the final value of the counter
thread1.join()
thread2.join()

print(f"Final counter: {counter}")  # Should be equal to 20,000,000

```

### Creating daemons

You can use the `daemon` attribute on a thread to indicate that it should be run in the background and terminated when the main program exits.

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.daemon = True  # Set the thread as a daemon
```

### Creating threads with priority

You can set the priority of a thread using the `setpriority` function.

```python
import threading

def print_numbers():
    for i in range(10):
        print(i)

# Create two threads with different priorities
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers, priority=5)  # Higher priority

# Set the priority of both threads
threading.setpriority(thread1._ident_, -20)
threading.setpriority(thread2._ident_, -10)

# Start both threads
thread1.start()
thread2.start()

```

### Creating a thread pool

You can create a thread pool to manage a group of worker threads.

```python
import threading

class ThreadPool:
    def __init__(self, num_workers):
        self.num_workers = num_workers
        self.workers = []

        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker)
            worker.setDaemon(True)  # Set the worker as a daemon
            worker.start()

    def submit(self, func, *args, **kwargs):
        return threading.Thread(target=func, args=args, kwargs=kwargs)

# Create a thread pool with five workers
pool = ThreadPool(5)

def main_function():
    for i in range(10):
        print(i)
        result = pool.submit(lambda: print(f"Worker {i}: {i}"))()  # Submit the function to be executed by a worker

# Start the main program and wait for all tasks to finish
for _ in range(15):
    pass
```
