# logging.config — Logging configuration

**Logging Configuration Module**
=====================================

The `logging.config` module provides functions and classes for configuring logging, including loading configurations from files and setting up loggers.

**Example Code**
---------------

```python
import logging.config

# Define a simple logger configuration
logger_config = {
    'version': 1,
    'formatters': {
        'simple': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
}

# Load the configuration
logging.config.dictConfig(logger_config)

# Create a logger with the loaded configuration
logger = logging.getLogger('example')

# Set the log level
logger.setLevel(logging.INFO)

# Log some messages
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
```

**Functions and Classes**
---------------------------

### `logging.config.dictConfig()`

*   Loads a logging configuration from a dictionary.
*   The dictionary should contain the following keys:
    *   `version`: The version of the logger configuration (required).
    *   `formatters`, `handlers`, and `root`: Dictionaries containing log formatter and handler configurations.

### `logging.config.fileConfig()`

*   Loads a logging configuration from a file.
*   Supports three formats: `.ini`, `.yaml`, and `.json`.
*   The file should contain a valid logger configuration dictionary.

### `logging.config.dictDefaults()`

*   Returns a default logger configuration dictionary.
*   This dictionary can be used as a starting point for creating custom log configurations.

### `logging.config.yamlConfig()` and `logging.config.jsonConfig()`

*   Loads a logging configuration from a YAML or JSON file, respectively.
*   Supports the same formats as `fileConfig`.

**Example Use Cases**
--------------------

*   **Configure Logging with a File**: Load a logging configuration from an `.ini` file using `dictConfig`.
```python
import logging.config

logger_config = logging.config.fileConfig('logging.ini')
```
*   **Create a Custom Logger**: Create a logger with the loaded configuration and set its log level.
```python
import logging.config

# Load the configuration
logging.config.dictConfig(logger_config)

# Create a logger with the loaded configuration
logger = logging.getLogger('example')
logger.setLevel(logging.INFO)
```
*   **Configure Logging in an App**: Configure logging at application startup using `dictConfig`.
```python
import logging.config

def main():
    # Load the configuration
    logging.config.dictConfig(logger_config)

    # Create loggers and set their levels
    logger1 = logging.getLogger('logger1')
    logger1.setLevel(logging.INFO)

    logger2 = logging.getLogger('logger2')
    logger2.setLevel(logging.WARNING)

if __name__ == '__main__':
    main()
```
