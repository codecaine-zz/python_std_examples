# queue - A synchronized queue class

The `queue` module provides a set of synchronization primitives that can be used to implement concurrent data structures such as queues, stacks, and priority queues. Here are comprehensive and well-documented code examples for each functionality in the `queue` module:

## Table of Contents

1. [Basic Queue Example](#1-basic-queue-example)
2. [Priority Queue Example](#2-priority-queue-example)
3. [LIFO Queue Example](#3-lifo-queue-example)
4. [Double-Ended Queue Example](#4-double-ended-queue-example)
5. [Custom Queue Example](#5-custom-queue-example)
6. [Queue with Priority](#6-queue-with-priority)

### 1. Basic Queue Example

This example demonstrates how to use a simple FIFO queue (FIFO - First In, First Out).

```python
import queue

# Create a FIFO queue
fifo_queue = queue.Queue()

# Add items to the queue
fifo_queue.put(1)
fifo_queue.put(2)
fifo_queue.put(3)

# Process the queue in order
print("Processing elements from FIFO queue:")
while not fifo_queue.empty():
    item = fifo_queue.get()
    print(item)

# Output:
# Processing elements from FIFO queue:
# 1
# 2
# 3
```

### 2. Priority Queue Example

This example demonstrates how to use a priority queue (min-heap) where the smallest item is retrieved first.

```python
import queue

# Create a min-heap priority queue
priority_queue = queue.PriorityQueue()

# Add items to the queue with priorities
priority_queue.put((3, 'bar'))
priority_queue.put((1, 'foo'))
priority_queue.put((2, 'baz'))

# Process the queue in order of priority
print("Processing elements from priority queue:")
while not priority_queue.empty():
    item = priority_queue.get()
    print(item)

# Output:
# Processing elements from priority queue:
# (1, 'foo')
# (2, 'baz')
# (3, 'bar')
```

### 3. LIFO Queue Example

This example demonstrates how to use a stack (LIFO - Last In, First Out).

```python
import queue

# Create a stack (FIFO) using the `queue.Queue` class
stack = queue.Queue()

# Add items to the stack
stack.put(1)
stack.put(2)
stack.put(3)

# Process the stack in reverse order
print("Processing elements from stack:")
while not stack.empty():
    item = stack.get()
    print(item)

# Output:
# Processing elements from stack:
# 3
# 2
# 1
```

### 4. Double-Ended Queue Example

This example demonstrates how to use a deque (double-ended queue) which supports efficient appends and pops from both ends.

```python
import queue

# Create a double-ended queue
deque = queue.deque()

# Add items to the front and back of the deque
deque.append(1)
deque.appendleft(2)
deque.append(3)
deque.appendleft(4)

# Process elements from both ends
print("Processing elements from deque:")
while len(deque) > 0:
    item = deque.popleft()
    print(item)

# Output:
# Processing elements from deque:
# 4
# 3
# 2
# 1
```

### 5. Custom Queue Example

This example demonstrates how to create a custom queue class using the `queue.Queue` class as a base.

```python
import queue

class MyQueue(queue.Queue):
    def __init__(self, maxsize=0):
        super().__init__(maxsize)

    def get(self):
        # Custom behavior: print item before removing it
        item = super().get()
        print(f"Retrieved: {item}")
        return item

# Create a custom queue
custom_queue = MyQueue()

# Add items to the queue
custom_queue.put(1)
custom_queue.put(2)
custom_queue.put(3)

# Process the queue in order
print("Processing elements from custom queue:")
while not custom_queue.empty():
    item = custom_queue.get()
    print(item)

# Output:
# Processing elements from custom queue:
# Retrieved: 1
# 1
# Retrieved: 2
# 2
# Retrieved: 3
# 3
```

### 6. Queue with Priority

This example demonstrates how to use a priority queue that stores items along with their priority.

```python
import queue

class PriorityItem:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    # Required for the priority queue to compare items by priority
    def __lt__(self, other):
        return self.priority < other.priority

# Create a min-heap priority queue with custom PriorityItem objects
priority_queue = queue.PriorityQueue()

# Add items to the queue with priorities
priority_queue.put(PriorityItem(3, 'bar'))
priority_queue.put(PriorityItem(1, 'foo'))
priority_queue.put(PriorityItem(2, 'baz'))

# Process the queue in order of priority
print("Processing elements from priority queue:")
while not priority_queue.empty():
    item = priority_queue.get()
    print(item.value)

# Output:
# Processing elements from priority queue:
# foo
# baz
# bar
```

These examples cover various aspects of using Python's `queue` module, including creating different types of queues and implementing custom behaviors. Each example is well-documented with comments explaining the purpose and functionality of each part of the code.
