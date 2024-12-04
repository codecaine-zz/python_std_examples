# concurrent.futures — Launching parallel tasks

**concurrent.futures Example Code**
=====================================

The `concurrent.futures` module provides a high-level interface for asynchronously executing callables.

### 1. Threading Pool Executor

A thread pool executor is a type of executor that maintains a pool of worker threads that can be reused across multiple tasks.

```python
import concurrent.futures
import time
from threading import Thread

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        future.result()
```

### 2. Process Pool Executor

A process pool executor is a type of executor that maintains a pool of worker processes.

```python
import concurrent.futures
import time

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        future.result()
```

### 3. Thread Pool Executor with Timeout

A thread pool executor can be configured to timeout on completion.

```python
import concurrent.futures
import time
from threading import Thread

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(3)
    try:
        # This will raise a TimeoutError after 2 seconds
        result = yield from future
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
    else:
        print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()
        except concurrent.futures.TimeoutError as e:
            print(f"Timeout: {e}")
```

### 4. Process Pool Executor with Timeout

A process pool executor can also be configured to timeout on completion.

```python
import concurrent.futures
import time

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(3)
    try:
        # This will raise a TimeoutError after 2 seconds
        result = yield from future
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
    else:
        print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()
        except concurrent.futures.TimeoutError as e:
            print(f"Timeout: {e}")
```

### 5. Asyncio-Based Executor

The `concurrent.futures` module also supports asyncio-based executors.

```python
import concurrent.futures
import asyncio

async def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    await asyncio.sleep(2)
    print(f"Task {num} finished")

# Create an asyncio-based executor with 5 worker tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    await concurrent.futures.as_completed(futures)
```

### 6. Asyncio-Based Process Executor

The `concurrent.futures` module also supports asyncio-based process executors.

```python
import concurrent.futures
import asyncio

async def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    await asyncio.sleep(2)
    print(f"Task {num} finished")

# Create an asyncio-based process executor with 5 worker processes
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    await concurrent.futures.as_completed(futures)
```

### 7. Executor with Cancellation

Executors can be configured to cancel ongoing tasks.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for 2 seconds and cancel ongoing tasks
    time.sleep(2)
    try:
        for future in concurrent.futures.as_completed(futures):
            future.cancel()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 8. Executor with Deadline

Executors can be configured to timeout on completion.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 9. Executor with Deadline and Cancellation

Executors can be configured to timeout on completion or cancel ongoing tasks.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for 1 second and cancel ongoing tasks
    time.sleep(1)
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
                future.cancel()
            else:
                print(f"Task {future.result()}")
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 10. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 11. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 12. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 13. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 14. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 15. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 16. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 17. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 18. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 19. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a process pool executor with 5 worker processes and a timeout of 2 seconds
with concurrent.futures.ProcessPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 20. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 21. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 22. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 23. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 24. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 25. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 26. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 27. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 28. Executor with Deadline, Cancellation and Thread Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a thread pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 29. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 30. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 31. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 32. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 33. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 34. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 35. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 36. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 37. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 38. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 39. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```

### 40. Executor with Deadline, Cancellation and Process Pool

Executors can be configured to timeout on completion or cancel ongoing tasks in a process pool.

```python
import concurrent.futures
from threading import Thread
import time
from functools import partial

def task(num):
    """Simulate a task that takes some time to complete"""
    print(f"Task {num} started")
    # Simulate a delay
    time.sleep(2)
    print(f"Task {num} finished")

# Create a thread pool executor with 5 worker threads and a timeout of 2 seconds
with concurrent.futures.ThreadPoolExecutor(max_workers=5, timeout=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete
    try:
        for future in concurrent.futures.as_completed(futures):
            if not future.done():
                print("Timeout: Task is still running")
            else:
                future.result()
    except concurrent.futures.TimeoutError as e:
        print(f"Timeout: {e}")
```
