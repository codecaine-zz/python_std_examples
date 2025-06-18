# asyncio - Asynchronous I/O
## Table of Contents

1. [Example 1: Basic Asynchronous Function with a Delay](#example-1-basic-asynchronous-function-with-a-delay)
2. [Example 2: Using Asyncio Tasks](#example-2-using-asyncio-tasks)
3. [Example 3: Handling Exceptions in Asynchronous Functions](#example-3-handling-exceptions-in-asynchronous-functions)
4. [Example 4: Using Event Loops](#example-4-using-event-loops)
5. [Example 5: Asynchronous I/O with `asyncio.open_file`](#example-5-asynchronous-io-with-asyncioopen_file)
6. [Example 6: Asynchronous I/O with `aiohttp` for Web Requests](#example-6-asynchronous-io-with-aiohttp-for-web-requests)
7. [Example 7: Asynchronous I/O with `asyncpg` for Database Operations](#example-7-asynchronous-io-with-asyncpg-for-database-operations)
8. [Example 8: Asynchronous I/O with `psycopg2` for Database Operations](#example-8-asynchronous-io-with-psycopg2-for-database-operations)
9. [Example 9: Asynchronous I/O with `gevent` for Non-blocking HTTP Requests](#example-9-asynchronous-io-with-gevent-for-non-blocking-http-requests)
10. [Example 10: Asynchronous I/O with `gevent` for Non-blocking Database Operations](#example-10-asynchronous-io-with-gevent-for-non-blocking-database-operations)



Below are comprehensive and well-documented code examples for various functionalities provided by the `asyncio` module in Python 3.12. Each example is designed to be clear, concise, and follows best practices for inclusion in official documentation.

### Example 1: Basic Asynchronous Function with a Delay

This example demonstrates how to define an asynchronous function that uses `await` to sleep for a specified amount of time.

```python
import asyncio

async def print_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

# Running the coroutine
asyncio.run(print_after(2, "Hello after 2 seconds"))
```

### Example 2: Using Asyncio Tasks

This example shows how to use `asyncio.create_task` to schedule multiple asynchronous tasks.

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

# Running the tasks
asyncio.run(main())
```

### Example 3: Handling Exceptions in Asynchronous Functions

This example demonstrates how to handle exceptions within an asynchronous function.

```python
import asyncio

async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def main():
    try:
        await failing_task()
    except Exception as e:
        print(f"Caught exception: {e}")

# Running the coroutine
asyncio.run(main())
```

### Example 4: Using Event Loops

This example illustrates how to manually create and manage an event loop.

```python
import asyncio

async def run_until_complete():
    await asyncio.sleep(1)
    print("Loop completed")

loop = asyncio.get_event_loop()
loop.create_task(run_until_complete())
loop.run_forever()

# To stop the loop, you would typically use loop.stop() and call loop.close(), but here we assume it runs indefinitely
```

### Example 5: Asynchronous I/O with `asyncio.open_file`

This example shows how to perform asynchronous file I/O using `asyncio.open_file`.

```python
import asyncio

async def read_file(file_path):
    try:
        async with open(file_path, 'r') as file:
            content = await file.read()
        return content
    except FileNotFoundError:
        return f"File {file_path} not found."

# Running the coroutine
file_content = asyncio.run(read_file('example.txt'))
print(file_content)
```

### Example 6: Asynchronous I/O with `aiohttp` for Web Requests

This example demonstrates how to use `aiohttp` in conjunction with `asyncio` to make asynchronous HTTP requests.

First, ensure you have `aiohttp` installed:

```bash
pip install aiohttp
```

Then, here's the code example:

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.example.com')
        print(html)

# Running the coroutine
asyncio.run(main())
```

### Example 7: Asynchronous I/O with `asyncpg` for Database Operations

This example demonstrates how to use `asyncpg` in conjunction with `asyncio` to perform asynchronous database operations.

First, ensure you have `asyncpg` installed:

```bash
pip install asyncpg
```

Then, here's the code example:

```python
import asyncio
import asyncpg

async def fetch_data(connection):
    query = 'SELECT * FROM my_table'
    result = await connection.fetch(query)
    return result

async def main():
    conn_str = 'postgresql://user:password@localhost/my_database'
    retries = 5
    for attempt in range(retries):
        try:
            pool = await asyncpg.create_pool(conn_str)
            break
        except (OSError, asyncpg.exceptions.ConnectionDoesNotExistError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(2)
            else:
                print("Failed to connect to the database after several attempts.")
                return

    try:
        data = await fetch_data(pool)
        for row in data:
            print(row)
    finally:
        await pool.close()

# Running the coroutine
asyncio.run(main())
```

### Example 8: Asynchronous I/O with `psycopg2` for Database Operations

This example demonstrates how to use `psycopg2` in conjunction with `asyncio` to perform asynchronous database operations.

First, ensure you have `psycopg2` installed:

```bash
pip install psycopg2-binary
```

Then, here's the code example:

```python
import asyncio
import asyncpg
import asyncio

async def fetch_data(conn):
    query = 'SELECT * FROM my_table'
    result = await conn.fetch(query)
    return result

async def main():
    conn_str = 'postgresql://username:password@127.0.0.1/my_database'
    conn = await asyncpg.connect(conn_str)
    data = await fetch_data(conn)
    for row in data:
        print(row)
    await conn.close()

# Running the coroutine
asyncio.run(main())
```

### Example 9: Asynchronous I/O with `gevent` for Non-blocking HTTP Requests

This example demonstrates how to use `gevent` along with `aiohttp` to perform asynchronous HTTP requests.

First, ensure you have `gevent` and `aiohttp` installed:

```bash
pip install gevent aiohttp
```

Then, here's the code example:

```python
import asyncpg
import asyncio

async def fetch_data(conn):
    query = 'SELECT * FROM my_table'
    result = await conn.fetch(query)
    return result

async def main():
    conn_str = 'postgresql://username:password@127.0.0.1/my_database'
    try:
        conn = await asyncpg.connect(conn_str)
        data = await fetch_data(conn)
        for row in data:
            print(row)
        await conn.close()
    except (asyncpg.PostgresError, OSError) as e:
        print(f"Error connecting to the database: {e}")

# Running the coroutine
asyncio.run(main())
```

### Example 10: Asynchronous I/O with `gevent` for Non-blocking Database Operations

This example demonstrates how to use `gevent` along with `psycopg2` to perform asynchronous database operations.

First, ensure you have `gevent` and `psycopg2-binary` installed:

```bash
pip install gevent psycopg2-binary
```

Then, here's the code example:

```python
import gevent
from gevent import monkey
monkey.patch_all()
import psycopg2
from psycopg2 import extras

def fetch_data(conn):
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    query = 'SELECT * FROM my_table'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def main():
    conn_str = 'dbname=my_database user=username password=password host=localhost'
    conn = psycopg2.connect(conn_str)
    data = fetch_data(conn)
    for row in data:
        print(row)
    conn.close()

if __name__ == "__main__":
    try:
        # Running the coroutine
        gevent.spawn(main).join()
    except KeyboardInterrupt:
        print("Process interrupted by user")
```

These examples cover a range of asynchronous I/O functionalities available in Python's `asyncio` module, including basic tasks, handling exceptions, managing event loops, performing file I/O, making HTTP requests, and interacting with databases using different libraries. Each example is designed to be clear and self-contained, providing a starting point for developers looking to learn about asynchronous programming in Python.
