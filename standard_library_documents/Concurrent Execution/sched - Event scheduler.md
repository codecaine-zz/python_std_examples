# sched - Event scheduler

The `sched` module in Python is a simple event scheduler that allows you to schedule and run functions at specific times or intervals. Below are comprehensive examples of how to use the `sched` module, including comments explaining each step:

```python
import sched
import time

# Initialize the scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def print_time(sc):
    # This function prints the current time and schedules itself again after 1 second
    print("Current time:", time.ctime())
    scheduler.enter(1, 1, print_time, (sc,))

# Schedule the first call to print_time
scheduler.enter(0, 1, print_time, (scheduler,))

# Run the scheduler
try:
    while True:
        scheduler.run(blocking=False)
except KeyboardInterrupt:
    print("Scheduler stopped.")
```

### Explanation:

1. **Initialize the Scheduler**: We create an instance of `sched.scheduler` with `time.time` as the time function and `time.sleep` as the delay function. This means that the scheduler will use Python's built-in `time` functions for current time and delays.

2. **Define a Task Function**: The `print_time` function is defined to print the current time and then schedule itself again after 1 second using the `scheduler.enter` method.

3. **Schedule the First Call**: We schedule the first call to `print_time` immediately (`0`) with a priority of `1`. This means it will be executed first.

4. **Run the Scheduler**: The scheduler is run in an infinite loop, which continues until interrupted by a keyboard interrupt (Ctrl+C). Inside the loop, `scheduler.run(blocking=False)` runs one event at a time and returns immediately if there are no events to process, allowing other tasks to execute.

### Key Features:

- **Time Functions**: The `sched` module uses Python's built-in `time` functions for current time and delays.
- **Priority Handling**: Tasks can be scheduled with different priorities. Lower numbers have higher priority.
- **Blocking vs Non-blocking Execution**: The scheduler can run in a blocking or non-blocking manner, depending on how it is called.

These examples provide a basic understanding of how to use the `sched` module to schedule and manage events in your Python applications.
