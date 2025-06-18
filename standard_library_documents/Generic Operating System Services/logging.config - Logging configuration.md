# logging.config - Logging configuration
## Table of Contents

1. [1. Basic Configuration using a Dictionary](#1-basic-configuration-using-a-dictionary)
2. [Explanation:](#explanation)
3. [2. Configuration using a JSON File](#2-configuration-using-a-json-file)
4. [Explanation:](#explanation)
5. [3. Using a Configuration Module](#3-using-a-configuration-module)
6. [Explanation:](#explanation)



Below are comprehensive code examples for the `logging.config` module in Python's standard library, along with detailed explanations of each example.

### 1. Basic Configuration using a Dictionary

```python
import logging.config

# Define a dictionary configuration
config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - '
                      '%(message)s - %(lineno)d - %(filename)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'detail'
        }
    },
    'loggers': {
        'my_logger': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        }
    }
}

# Apply the configuration
logging.config.dictConfig(config)

# Get a logger instance
logger = logging.getLogger('my_logger')

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Explanation:

- **Version**: Specifies the version of the configuration format.
- **disable_existing_loggers**: Determines whether existing loggers should be disabled.
- **formatters**: Defines custom formatting for different log levels and formats.
  - `simple`: A basic format that includes timestamp, logger name, level, and message.
  - `detail`: An extended format that includes line number and file name in addition to the simple format.
- **handlers**: Specifies where logs should be sent.
  - `console`: Sends logs to the console with a specified format.
  - `file`: Writes logs to a file with a specific format.
- **loggers**: Defines which loggers should use which handlers and what level of logging they should handle.

### 2. Configuration using a JSON File

```python
import logging.config

# Load configuration from a JSON file
with open('logging_config.json') as f:
    config = json.load(f)

# Apply the configuration
logging.config.dictConfig(config)

# Get a logger instance
logger = logging.getLogger('my_logger')

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Explanation:

- **JSON File**: Contains the same configuration as above but in JSON format.
- **Loading from a file**: Uses Python's built-in `json` module to load the configuration from a file.

### 3. Using a Configuration Module

Create a separate Python file, e.g., `logging_config.py`, with the following content:

```python
import logging.config

# Define a dictionary configuration
config = {
    'version': 1,
    'disable_existing_loggers': False,
    # ... (same as above)
}

# Apply the configuration
logging.config.dictConfig(config)
```

Then, in your main application file, import and use this module:

```python
import logging_config

# Get a logger instance
logger = logging.getLogger('my_logger')

# Log messages at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

### Explanation:

- **Separate Module**: Encapsulates the configuration in a separate file, promoting code organization and reusability.
- **Importing from a module**: Imports the configuration from another Python file.

These examples demonstrate how to configure logging using different methods, including dictionary-based configuration, JSON file loading, and external configuration modules. Each example follows best practices for clarity and maintainability.
