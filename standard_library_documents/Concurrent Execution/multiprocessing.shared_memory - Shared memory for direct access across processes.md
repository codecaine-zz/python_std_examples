# multiprocessing.shared_memory — Shared memory for direct access across processes

**Shared Memory Example**
==========================

Here's an example of using `multiprocessing/shared_memory` to create shared memory between two processes.

```python
import multiprocessing
import numpy as np

def producer(shared_memory):
    # Create a numpy array in the shared memory space
    arr = np.array([1, 2, 3], dtype=np.int32)
    
    # Write the array to the shared memory space
    with shared_memory.create_view(np.ndarray) as view:
        view[0] = 10
    
    # Get the value of the first element in the shared memory space
    print(shared_memory.get_value(0, 1))

def consumer(shared_memory):
    # Create a numpy array from the shared memory space
    arr = np.array([], dtype=np.int32)
    
    # Read values from the shared memory space and append to our array
    with shared_memory.create_view(np.ndarray) as view:
        for i in range(5):
            arr = np.append(arr, view[i])
    
    print(arr)

if __name__ == "__main__":
    # Create a new shared memory region
    shared_mem = multiprocessing.SharedMemory(create=True)
    
    # Get the address of the shared memory space
    address = shared_mem.get_addr()
    
    # Start two new processes to access the shared memory space
    p1 = multiprocessing.Process(target=producer, args=(shared_mem,))
    p2 = multiprocessing.Process(target=consumer, args=(shared_mem,))
    
    # Start both processes
    p1.start()
    p2.start()
    
    # Wait for both processes to finish
    p1.join()
    p2.join()
    
    # Close the shared memory region
    shared_mem.close()
```

**How it Works**
-----------------

1.  We first create a new shared memory region using `multiprocessing.SharedMemory(create=True)`.
2.  The address of this shared memory space is obtained using `shared_mem.get_addr()`.
3.  A new process is started for each task that accesses the shared memory space.
4.  In the producer process, we create a numpy array in the shared memory space and write to it.
5.  In the consumer process, we read values from the shared memory space using `shared_mem.get_value()`, append them to our own array, and print the result.

**Note**: Make sure to use `if __name__ == "__main__":` to ensure that the code is run in a child process only when executed directly. This prevents some features of multiprocessing from working correctly if run as a module.
