# logging — Logging facility for Python

**Logging Facility**
=====================

The `logging` module provides a flexible logging mechanism that allows you to log events at different levels of severity.

**Installation**
---------------

To use the `logging` module, import it in your Python script and enable logging:
```python
import logging
```
You can also set the logging level using the following constants:

*   `logging.DEBUG`: Debug messages (usually turned off)
*   `logging.INFO`: Informational messages
*   `logging.WARNING`: Warning messages
*   `logging.ERROR`: Error messages
*   `logging.CRITICAL`: Critical error messages

**Basic Usage**
-----------------

### Enable Logging

To enable logging, create a logger object:
```python
logger = logging.getLogger(__name__)
```
`__name__` is the name of the current module.

### Set the Logging Level

Set the logging level for the logger:
```python
logging.basicConfig(level=logging.INFO)
```
This will set the logging level to `INFO`, which means that only messages with a severity of `INFO` or higher will be logged.

### Log Messages

Use the `logger` object to log messages at different levels:
```python
import time

def main():
    logger.debug("Debug message")
    logger.info("Informational message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical error message")

if __name__ == "__main__":
    main()
```
This will log the messages to the console.

### Formatting Log Messages

You can customize the format of log messages using the `basicConfig` method:
```python
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
```
This will add a timestamp, logging level, and message to each logged message.

### Logging to a File

To log messages to a file instead of the console, you can use the `FileHandler` class:
```python
import logging

logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler("log_file.log")

# Set the logging level for the file handler
file_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the file handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
```
This will log messages to `log_file.log` instead of the console.

**Advanced Topics**
--------------------

### Log Levels

The following are the predefined log levels:

*   `logging.DEBUG`: Debug messages
*   `logging.INFO`: Informational messages
*   `logging.WARNING`: Warning messages
*   `logging.ERROR`: Error messages
*   `logging.CRITICAL`: Critical error messages

You can use these constants to set the logging level.

### Log Messages in Different Formats

You can customize the format of log messages using a `Formatter` object. The formatter can be created with different attributes, such as:

*   `%s`: Timestamp
*   `%d`: Date and time in UTC
*   `%r`: Message (default formatting)
*   `%p`: Process ID
*   `%h`: Hostname
*   `%e`: Exception type and value

You can use these attributes to format log messages.

### Logging Multiple Loggers

You can create multiple logger objects and add them to the `logging.root` logger. This allows you to control the logging behavior for each logger individually.

```python
import logging

logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

# Set the logging level for each logger
logger1.setLevel(logging.INFO)
logger2.setLevel(logging.ERROR)

# Add a handler to each logger
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler("log_file2.log")

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger1.addHandler(handler1)
logger2.addHandler(handler2)
```
This will create two separate loggers, `logger1` and `logger2`, each with its own logging level and handler.
