# queue — A synchronized queue class

**Queue Module Code Examples**
=====================================

The `queue` module in Python provides an interface for working with queues, which are FIFO (First-In-First-Out) data structures.

### Creating a Queue

```python
from queue import Queue

# Create a new queue object
q = Queue()

# Add elements to the queue
q.put(1)
q.put(2)
q.put(3)

print(q.get())  # prints: 1
print(q.get())  # prints: 2
print(q.get())  # prints: 3

# Try to get an element from an empty queue
try:
    q.get()
except Empty:
    print("Queue is empty")
```

### Queue Operations

```python
from queue import Queue, Empty

# Create a new queue object
q = Queue()

# Put elements into the queue
q.put(1)
q.put(2)

# Get elements from the queue
while not q.empty():
    try:
        item = q.get()
        print(item)  # prints: 1 and then 2
    except Empty:
        print("Queue is empty")

# Create a new queue object with limited size (maxsize)
q = Queue(maxsize=3)

# Put elements into the queue
for i in range(5):
    q.put(i)

print(q.empty())  # prints: False

try:
    q.get()
except Full:
    print("Queue is full")

while not q.empty():
    try:
        item = q.get()
        print(item)  # prints: 0, 1, and then 2
    except Empty:
        break
```

### Blocking Operations

```python
from queue import Queue
import threading
import time

def worker(q):
    while True:
        item = q.get()
        print(f"Received {item}")
        if item == "stop":
            q.put("quit")
        else:
            time.sleep(1)

# Create a new queue object
q = Queue()

# Start 5 workers
for _ in range(5):
    t = threading.Thread(target=worker, args=(q,))
    t.start()

# Put elements into the queue
for i in range(10):
    q.put(i)

print("Waiting for all workers to finish")
```

### Non-Blocking Operations

```python
from queue import Queue
import threading
import time

def worker(q):
    while True:
        try:
            item = q.get_nowait()
            print(f"Received {item}")
        except Empty:
            break
        else:
            time.sleep(1)
        if item == "stop":
            q.put("quit")
            break

# Create a new queue object
q = Queue()

# Start 5 workers
for _ in range(5):
    t = threading.Thread(target=worker, args=(q,))
    t.start()

print("Stopping the workers")
```

### Lock-Free Operations (in Python 3.7 and later)

```python
from queue import Queue

class Consumer:
    def __init__(self, q):
        self.q = q
        self.lock = threading.Lock()

    def get(self):
        with self.lock:
            while True:
                item = self.q.get()
                if item is None:
                    break
                yield item
        self.q.task_done()

def producer(q):
    for i in range(10):
        q.put(i)

q = Queue()

consumer1 = Consumer(q)
consumer2 = Consumer(q)

p = threading.Thread(target=producer, args=(q,))
p.start()

for _ in range(5):
    consumer1.get()
    consumer2.get()
```
