# logging - Logging facility for Python
## Table of Contents

1. [Example 1: Basic Configuration](#example-1-basic-configuration)
2. [Example 2: Logging to Files](#example-2-logging-to-files)
3. [Example 3: Logging with Custom Handlers](#example-3-logging-with-custom-handlers)
4. [Example 4: Logging with Formatters](#example-4-logging-with-formatters)
5. [Example 5: Logging with Rotating Files](#example-5-logging-with-rotating-files)
6. [Example 6: Logging with Timestamps](#example-6-logging-with-timestamps)
7. [Example 7: Logging with Levels and Filters](#example-7-logging-with-levels-and-filters)
8. [Example 8: Logging with Handlers and Filters](#example-8-logging-with-handlers-and-filters)



The `logging` module in Python provides a flexible framework for emitting log messages from Python programs. It supports formatting, coloring, and redirection of output to various destinations. Below are comprehensive code examples that demonstrate various functionalities of the `logging` module.

### Example 1: Basic Configuration

This example shows how to configure basic logging settings.

```python
import logging

# Create a logger object
logger = logging.getLogger('my_logger')

# Set the level of the logger
logger.setLevel(logging.DEBUG)

# Create a console handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

### Example 2: Logging to Files

This example shows how to configure logging to write messages to a file.

```python
import logging

# Create a logger object
logger = logging.getLogger('file_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level
fh = logging.FileHandler('app.log')
fh.setLevel(logging.ERROR)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(fh)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

### Example 3: Logging with Custom Handlers

This example shows how to create a custom logging handler.

```python
import logging

class MyHandler(logging.Handler):
    def emit(self, record):
        # Custom logic for handling log records
        print(f"Custom Handler - {record.levelname}: {record.getMessage()}")

# Create a logger object
logger = logging.getLogger('my_handler_logger')
logger.setLevel(logging.DEBUG)

# Create an instance of the custom handler and set its level
ch = MyHandler()
ch.setLevel(logging.ERROR)

# Add the custom handler to the logger
logger.addHandler(ch)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

### Example 4: Logging with Formatters

This example shows how to create and use different log record formats.

```python
import logging

# Create a logger object
logger = logging.getLogger('formatter_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Define different formatters for different levels
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(name)s: %(message)s')

# Add each formatter to the handler based on the log level
if logger.level == logging.DEBUG:
    ch.setFormatter(formatter1)
else:
    ch.setFormatter(formatter2)

# Add the handler to the logger
logger.addHandler(ch)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

### Example 5: Logging with Rotating Files

This example shows how to configure logging to rotate log files.

```python
import logging.handlers

# Create a logger object
logger = logging.getLogger('rotating_file_logger')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler and set its level
rh = logging.handlers.RotatingFileHandler('app.log', maxBytes=1024, backupCount=5)
rh.setLevel(logging.INFO)

# Set the formatter for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rh.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(rh)

# Log messages at different levels
for i in range(10):
    logger.debug(f'This is a debug message {i+1}.')
```

### Example 6: Logging with Timestamps

This example shows how to customize the timestamp format in log records.

```python
import logging

# Create a logger object
logger = logging.getLogger('timestamp_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Set a custom date format for timestamps
formatter = logging.Formatter('%Y-%m-%d %H:%M:%S - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Log messages at different levels
logger.debug('This is a debug message.')
```

### Example 7: Logging with Levels and Filters

This example shows how to set different log levels and apply filters to log records.

```python
import logging

# Create a logger object
logger = logging.getLogger('level_and_filter_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler and set its level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Define a filter that only allows warning and error messages
class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

# Add the filter to the handler
ch.addFilter(WarningFilter())

# Set the formatter for the handler
formatter = logging.Formatter('%(name)s: %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

### Example 8: Logging with Handlers and Filters

This example demonstrates how to configure multiple handlers and apply filters.

```python
import logging

# Create a logger object
logger = logging.getLogger('multiple_handlers_logger')
logger.setLevel(logging.DEBUG)

# Create console handlers for different levels
ch_info = logging.StreamHandler()
ch_info.setLevel(logging.INFO)
ch_info.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

ch_error = logging.StreamHandler()
ch_error.setLevel(logging.ERROR)
ch_error.setFormatter(logging.Formatter('%(name)s: %(message)s'))

# Create a file handler
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Define a filter that only allows warning and error messages
class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

# Add filters to the handlers
ch_info.addFilter(WarningFilter())
ch_error.addFilter(WarningFilter())

# Add handlers to the logger
logger.addHandler(ch_info)
logger.addHandler(ch_error)
logger.addHandler(fh)

# Log messages at different levels
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')
```

These examples cover various aspects of the `logging` module, including basic configuration, logging to files, custom handlers and formatters, rotating logs, timestamp customization, levels and filters, and handling multiple handlers and filters. Each example is designed to be clear and self-contained, suitable for integration into larger projects or documentation.
