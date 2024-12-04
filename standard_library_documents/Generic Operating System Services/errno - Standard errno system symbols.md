# errno — Standard errno system symbols

**Error Number Definitions**
=====================================

The `errno` module provides constants representing standard error numbers used by the Unix operating system.

```python
# Import the errno module
importerrno = errno  # Use import instead of aliasing for compatibility with Python 3.x

# Define a function to raise an OSError with a given error number
def errno_error(number, message):
    """
    Raise an OSError with a given error number and message.
    
    Args:
        number (int): The error number.
        message (str): The error message.
    """
    # Use the raise statement to raise an OSError
    raise OSError(f"{message} ({number})")

# Example usage:
try:
    # Simulate an error with a specific error number and message
    errno_error(2, "No such file or directory")
except OSError as e:
    print(f"Error: {e}")
```

**Example Use Cases**
--------------------

1.  **Checking for errors**: You can use the `errno` constants to check if an operation failed with a specific error.
    ```python
import errno

# Example usage:
try:
    # Simulate an operation that may fail
    open("/nonexistent/file", "r")
except OSError as e:
    print(f"Error: {e}")
    # Check the error number
    if e.errno == errno.ENOENT:
        print("The file does not exist.")
```

2.  **Raising custom errors**: You can define a function to raise an `OSError` with a specific error number and message.
    ```python
def my_error(message):
    # Use the errno.error function to raise an OSError
    importerrno
    errno.error(errno.EINVAL, f"Invalid argument: {message}")

# Example usage:
my_error("The input is invalid.")
```

**Constants**
--------------

*   `ENOENT`: The file does not exist.
*   `EIO`: I/O error occurred while trying to access a file descriptor.
*   `ENOTDIR`: The specified path name is not a directory.
*   `ETIMEDOUT`: A connection timed out after the timeout period.
*   `EACCES`: Permission denied for a specific operation.
*   `EBADFILE`: The specified path name is not a valid file.
*   `ECHILD`: A child process was terminated without being waited on by the parent process.
*   `ECLDFOUND`: A signal was caught but not delivered to the process.
*   `ECANCELED`: Operation canceled after completion.
*   `EDEADLK`: Deadlock detected while trying to lock a resource.
*   `EDOM`: The domain of an error number is not defined for this operation.
*   `ENAMETOOLONG`: The length of the specified path name exceeds the maximum allowed value.
*   `ENOTEMPTY`: Directory is not empty.
*   `EPERM`: Operation not permitted.
*   `EROFS`: Operation not permitted because of file system restrictions.
*   `ESRCH`: No process with the specified ID exists.

**See Also**
--------------

The `os` and `sys` modules provide functions to interact with the operating system, including error handling.
