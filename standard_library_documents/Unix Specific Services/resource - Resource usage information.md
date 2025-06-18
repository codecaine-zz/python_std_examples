# resource - Resource usage information
## Table of Contents

1. [Example 1: Monitoring Memory Usage](#example-1-monitoring-memory-usage)
2. [Example 2: Setting CPU Time Limits](#example-2-setting-cpu-time-limits)
3. [Example 3: Monitoring File Descriptor Limits](#example-3-monitoring-file-descriptor-limits)
4. [Example 4: Monitoring Memory Limits](#example-4-monitoring-memory-limits)
5. [Example 5: Monitoring CPU Usage](#example-5-monitoring-cpu-usage)
6. [Example 6: Monitoring Maximum File Descriptor Usage](#example-6-monitoring-maximum-file-descriptor-usage)
7. [Example 7: Monitoring Maximum Stack Size](#example-7-monitoring-maximum-stack-size)



The `resource` module in Python provides a portable interface to system resources. It allows you to monitor and control various aspects of program execution, such as memory limits, CPU time, open file descriptors, etc.

Here are comprehensive code examples that demonstrate the functionalities of the `resource` module:

### Example 1: Monitoring Memory Usage

This example demonstrates how to monitor the current memory usage of a process.

```python
import resource

def monitor_memory_usage():
    # Get the current peak memory usage in kilobytes
    peak_memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    
    print(f"Peak Memory Usage: {peak_memory_usage} MB")

if __name__ == "__main__":
    monitor_memory_usage()
```

### Example 2: Setting CPU Time Limits

This example shows how to set a limit on the CPU time that a process can use.

```python
import resource

def set_cpu_time_limit(seconds):
    try:
        # Set the soft and hard limits for CPU time (in seconds)
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, -1))
        print(f"CPU Time Limit Set: {seconds} seconds")
    except OSError as e:
        print(f"Failed to set CPU time limit: {e}")

if __name__ == "__main__":
    set_cpu_time_limit(10)  # Set a 10-second CPU time limit
```

### Example 3: Monitoring File Descriptor Limits

This example shows how to monitor and set limits on the number of file descriptors a process can open.

```python
import resource

def get_file_descriptor_limits():
    try:
        # Get the current soft and hard limits for file descriptors
        soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
        
        print(f"Current File Descriptor Limits: Soft {soft_limit}, Hard {hard_limit}")
    except OSError as e:
        print(f"Failed to get file descriptor limits: {e}")

def set_file_descriptor_limits(soft_limit, hard_limit):
    try:
        # Set the soft and hard limits for file descriptors
        resource.setrlimit(resource.RLIMIT_NOFILE, (soft_limit, hard_limit))
        print(f"File Descriptor Limits Set: Soft {soft_limit}, Hard {hard_limit}")
    except OSError as e:
        print(f"Failed to set file descriptor limits: {e}")

if __name__ == "__main__":
    get_file_descriptor_limits()
    set_file_descriptor_limits(256, 1024)
```

### Example 4: Monitoring Memory Limits

This example demonstrates how to monitor and set memory limits for a process.

```python
import resource

def get_memory_limits():
    try:
        # Get the current soft and hard limits for memory usage (in bytes)
        soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_AS)
        
        print(f"Current Memory Limits: Soft {soft_limit} bytes, Hard {hard_limit} bytes")
    except OSError as e:
        print(f"Failed to get memory limits: {e}")

def set_memory_limits(soft_limit, hard_limit):
    try:
        # Set the soft and hard limits for memory usage (in bytes)
        resource.setrlimit(resource.RLIMIT_AS, (soft_limit, hard_limit))
        print(f"Memory Limits Set: Soft {soft_limit} bytes, Hard {hard_limit} bytes")
    except OSError as e:
        print(f"Failed to set memory limits: {e}")

if __name__ == "__main__":
    get_memory_limits()
    set_memory_limits(1024 * 1024 * 512, -1)  # Set a 512MB soft limit and no hard limit
```

### Example 5: Monitoring CPU Usage

This example demonstrates how to monitor the current CPU usage of a process.

```python
import resource

def get_cpu_usage():
    try:
        # Get the current user and system CPU time used by the process (in seconds)
        user_time, sys_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime
        
        print(f"CPU Usage: User {user_time} seconds, System {sys_time} seconds")
    except OSError as e:
        print(f"Failed to get CPU usage: {e}")

if __name__ == "__main__":
    get_cpu_usage()
```

### Example 6: Monitoring Maximum File Descriptor Usage

This example demonstrates how to monitor and set the maximum number of open files a process can have.

```python
import resource

def get_max_open_files():
    try:
        # Get the current hard limit for the maximum number of open files
        max_open_files = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
        
        print(f"Maximum Open Files Limit: {max_open_files}")
    except OSError as e:
        print(f"Failed to get maximum open files limit: {e}")

def set_max_open_files(max_open_files):
    try:
        # Set the hard limit for the maximum number of open files
        resource.setrlimit(resource.RLIMIT_NOFILE, (resource.getrlimit(resource.RLIMIT_NOFILE)[0], max_open_files))
        print(f"Maximum Open Files Limit Set: {max_open_files}")
    except OSError as e:
        print(f"Failed to set maximum open files limit: {e}")

if __name__ == "__main__":
    get_max_open_files()
    set_max_open_files(1024)
```

### Example 7: Monitoring Maximum Stack Size

This example demonstrates how to monitor and set the maximum stack size a process can use.

```python
import resource

def get_stack_size():
    try:
        # Get the current soft and hard limits for the maximum stack size (in bytes)
        soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_STACK)
        
        print(f"Stack Size Limits: Soft {soft_limit} bytes, Hard {hard_limit} bytes")
    except OSError as e:
        print(f"Failed to get stack size limits: {e}")

def set_stack_size(soft_limit, hard_limit):
    try:
        # Set the soft and hard limits for the maximum stack size (in bytes)
        resource.setrlimit(resource.RLIMIT_STACK, (soft_limit, hard_limit))
        print(f"Stack Size Limits Set: Soft {soft_limit} bytes, Hard {hard_limit} bytes")
    except OSError as e:
        print(f"Failed to set stack size limits: {e}")

if __name__ == "__main__":
    get_stack_size()
    set_stack_size(1024 * 1024, -1)  # Set a 1MB soft limit and no hard limit
```

These examples cover various aspects of resource usage management in Python, demonstrating how to monitor and control different system resources such as memory, CPU time, file descriptors, and stack size. Each example includes comments explaining the purpose of each part of the code and handling any potential exceptions that might occur.
