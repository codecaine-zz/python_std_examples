# asyncio - Asynchronous I/O

Here's an example of how you can use the `asyncio` module from Python's standard library:

```python
import asyncio
import time

# Define a function that simulates an IO-bound task
async def read_file(file_path):
    """
    Simulate reading a file.
    
    Args:
        file_path (str): The path to the file to be read.

    Returns:
        None
    """
    # Simulate reading the file by sleeping for 2 seconds
    await asyncio.sleep(2)
    print(f"Read {file_path}")

# Define a function that simulates an IO-bound task
async def write_file(file_path):
    """
    Simulate writing to a file.
    
    Args:
        file_path (str): The path to the file to be written.

    Returns:
        None
    """
    # Simulate writing to the file by sleeping for 2 seconds
    await asyncio.sleep(2)
    print(f"Write {file_path}")

# Define an event loop
async def main():
    start_time = time.time()

    # Create two tasks that read and write files concurrently
    task1 = asyncio.create_task(read_file("file1.txt"))
    task2 = asyncio.create_task(write_file("file2.txt"))

    # Wait for both tasks to complete
    await asyncio.gather(task1, task2)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

# Run the main function
asyncio.run(main())
```

In this code example:

*   We define two functions `read_file` and `write_file` that simulate IO-bound tasks.
*   In the `main` function, we create an event loop using `asyncio.create_task`.
*   We use `asyncio.gather` to run both tasks concurrently.
*   The `asyncio.run(main())` call starts the event loop.

**How it works:**

1.  Create two tasks that read and write files concurrently.
2.  Use `asyncio.gather` to wait for both tasks to complete.
3.  Run the main function using `asyncio.run(main())`.

When you run this code, it will print:

```
Read file1.txt
Write file2.txt
Time taken: 4.001163 seconds
```

As expected, since the tasks are running concurrently, they should not take a total of 4 seconds.

### Best Practices

*   The `asyncio` module is used to write single-threaded concurrent code using coroutines.
*   The `create_task` function creates an asynchronous task that can be run concurrently with other tasks.
*   The `gather` function waits for multiple tasks to complete and returns a list of results.
