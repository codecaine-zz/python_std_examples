# threading - Thread-based parallelism

Below are comprehensive and well-documented code examples for various functionalities of the `threading` module in Python. Each example is designed to be clear, concise, and follows best practices suitable for inclusion in official documentation.

### 1. Creating and Starting Threads

```python
import threading
import time

def worker():
    """Example worker function that sleeps for a random amount of time."""
    import random
    sleep_time = random.uniform(1, 3)
    print(f"Thread {threading.current_thread().name} sleeping for {sleep_time:.2f} seconds")
    time.sleep(sleep_time)

# Create and start multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, name=f'Thread-{i+1}')
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
```

**Explanation:**
- The `worker` function simulates a task that takes a random amount of time to execute.
- We create multiple threads, each running the `worker` function. Each thread has a unique name.
- We start each thread using the `start()` method.
- Finally, we use `join()` on each thread to ensure all threads have completed before proceeding.

### 2. Synchronizing Threads with Locks

```python
import threading
import time

# Shared resource
shared_resource = 0
lock = threading.Lock()

def increment():
    """Increment the shared resource using a lock."""
    global shared_resource
    for _ in range(100):
        # Acquire the lock before modifying the shared resource
        with lock:
            shared_resource += 1
        time.sleep(0.001)  # Simulate some processing

# Create and start multiple threads that increment the shared resource
threads = []
for i in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final value of shared_resource: {shared_resource}")
```

**Explanation:**
- We use a `Lock` to ensure that only one thread can modify the shared resource at a time, preventing race conditions.
- The `increment` function repeatedly increments the shared resource while holding the lock. This ensures that each increment operation is atomic.
- Multiple threads are created and started to perform concurrent modifications.

### 3. Using Condition Variables

```python
import threading
import time

# Shared resources
condition = threading.Condition()
shared_resource = []

def producer():
    """Producer thread that adds items to the shared list."""
    for i in range(10):
        with condition:
            shared_resource.append(f"Item {i}")
            print(f"Produced: {i}")
            condition.notify()  # Notify one waiting consumer
        time.sleep(0.5)

def consumer():
    """Consumer thread that takes items from the shared list."""
    while True:
        with condition:
            while not shared_resource:
                condition.wait()  # Wait if no item is available
            item = shared_resource.pop()
            print(f"Consumed: {item}")
            condition.notify()  # Notify one producer

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()
```

**Explanation:**
- A `Condition` object is used to synchronize access to the shared list.
- The producer thread adds items to the list and notifies a waiting consumer. Similarly, the consumer waits until an item is available in the list before consuming it.

### 4. Using Semaphore

```python
import threading
import time

# Shared resource with semaphore control
semaphore = threading.Semaphore(3)
shared_resource = []

def producer():
    """Producer thread that adds items to the shared list."""
    for i in range(10):
        with semaphore:
            shared_resource.append(f"Item {i}")
            print(f"Produced: {i}")
        time.sleep(0.5)

def consumer():
    """Consumer thread that takes items from the shared list."""
    while True:
        with semaphore:
            if not shared_resource:
                continue
            item = shared_resource.pop()
            print(f"Consumed: {item}")

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread1 = threading.Thread(target=consumer)
consumer_thread2 = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread1.start()
consumer_thread2.start()

# Wait for both producer and consumer threads to complete
producer_thread.join()
consumer_thread1.join()
consumer_thread2.join()
```

**Explanation:**
- A `Semaphore` is used to limit the number of concurrent access to a shared resource. In this example, up to 3 producers can write to the list at a time.
- The consumers wait until there are items in the list before consuming them.

### 5. Using Event Objects

```python
import threading
import time

# Shared event object
event = threading.Event()
shared_resource = None

def producer():
    """Producer thread that sets the shared resource and signals the event."""
    for i in range(10):
        item = f"Item {i}"
        print(f"Produced: {item}")
        shared_resource = item
        event.set()  # Signal the consumer that an item is ready
        time.sleep(0.5)

def consumer():
    """Consumer thread that waits for the event to be set and processes the shared resource."""
    event.wait()  # Wait until the producer signals
    print(f"Consumed: {shared_resource}")

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()
```

**Explanation:**
- An `Event` object is used to coordinate between the producer and consumer. The producer sets the event when it has a new item, and the consumer waits until the event is set before processing the resource.

These examples cover various aspects of using threads in Python, including thread creation, synchronization with locks, condition variables, semaphores, and events. Each example is self-contained and demonstrates best practices for handling concurrent programming tasks.
