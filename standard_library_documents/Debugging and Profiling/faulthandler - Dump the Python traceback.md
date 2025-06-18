# faulthandler - Dump the Python traceback
## Table of Contents

1. [1. Basic Usage](#1-basic-usage)
2. [2. Customizing Core Dump Generation](#2-customizing-core-dump-generation)
3. [3. Disabling Core Dump Generation](#3-disabling-core-dump-generation)
4. [4. Listing Enabled Core Dump Filenames](#4-listing-enabled-core-dump-filenames)
5. [5. Setting Custom Dump Directory](#5-setting-custom-dump-directory)
6. [6. Listing All Supported Formats](#6-listing-all-supported-formats)
7. [7. Setting Custom Format](#7-setting-custom-format)
8. [8. Listing All Threads](#8-listing-all-threads)
9. [9. Dumping Traceback for a Specific Thread](#9-dumping-traceback-for-a-specific-thread)
10. [10. Printing a Stack Trace](#10-printing-a-stack-trace)



The `faulthandler` module in Python is used to enable a core dump of the Python interpreter on segmentation faults, errors, or other unhandled exceptions. This can be particularly useful for debugging and recovering from crashes. Below are some comprehensive code examples that demonstrate various functionalities of the `faulthandler` module.

### 1. Basic Usage

```python
import faulthandler

# Enable core dump generation
faulthandler.enable()

try:
    # Code that might cause a crash
    import sys
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
```

### 2. Customizing Core Dump Generation

```python
import faulthandler

# Enable core dump generation with custom options
faulthandler.enable(file="core", all_threads=True, chain=False)

try:
    # Code that might cause a crash
    import sys
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
```

### 3. Disabling Core Dump Generation

```python
import faulthandler

# Disable core dump generation
faulthandler.disable()

try:
    # Code that might cause a crash
    import sys
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
```

### 4. Listing Enabled Core Dump Filenames

```python
import faulthandler

# List all core dump filenames enabled by the program
print(faulthandler.get_enabled())
```

### 5. Setting Custom Dump Directory

```python
import faulthandler

# Set a custom directory for saving core dumps
faulthandler.set_dump_dir("/path/to/directory")

try:
    # Code that might cause a crash
    import sys
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
```

### 6. Listing All Supported Formats

```python
import faulthandler

# List all supported formats for dumping the traceback
print(faulthandler.get_dump_formats())
```

### 7. Setting Custom Format

```python
import faulthandler

# Set a custom format for dumping the traceback
faulthandler.set_dump_format("c")

try:
    # Code that might cause a crash
    import sys
    sys.exit(0)
except Exception as e:
    print("An error occurred:", e)
```

### 8. Listing All Threads

```python
import faulthandler

# List all threads in the current process
print(faulthandler.get_all_threads())
```

### 9. Dumping Traceback for a Specific Thread

```python
import faulthandler

# Get a specific thread object
thread = faulthandler.get_thread(123)

if thread:
    # Dump the traceback for the specified thread
    print("Dumping traceback for thread", thread.ident)
    faulthandler.dump_traceback(thread)
else:
    print("Thread not found")
```

### 10. Printing a Stack Trace

```python
import faulthandler

# Print the current stack trace
faulthandler.print_stack()
```

These examples cover various aspects of using the `faulthandler` module, from enabling and disabling core dump generation to customizing options and handling exceptions. Each example includes comments explaining key steps and uses standard library functions and modules effectively.
