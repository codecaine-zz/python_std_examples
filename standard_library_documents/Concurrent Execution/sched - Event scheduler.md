# sched — Event scheduler

**Sched Module: Event Scheduler**
====================================

The `sched` module provides a way to schedule tasks to run at specific times or after a certain delay.

**Example Use Cases:**

*   Scheduling system tasks, such as backing up files or sending emails.
*   Creating cron-like jobs for recurring tasks.
*   Implementing a scheduling system for games or simulations.

**Code Generation:**
```python
import sched
import time

# Create a scheduler object
s = sched.scheduler(time.time, time.sleep)

def job(name):
    """A sample task function."""
    print(f"Running job: {name}")
    # Add some sleep to demonstrate the task duration.
    s.enter(5, 1, job, ('Subjob',))  # schedule subjobs
    s.run()  # run the scheduler

# Schedule a task to run after 10 seconds.
s.enter(10, 0, job, ('Main Job',))

# Start the scheduler and keep it running until manually stopped.
while True:
    try:
        s.run()
    except KeyboardInterrupt:
        print('\nScheduler stopped.')
        break
```

**Scheduling Subjobs:**

```python
def subjob(name):
    """A sample task function."""
    print(f"Running subjob: {name}")
    # Schedule another subjob to run after a short delay.
    s.enter(2, 1, subjob, ('Subsubjob',))

# In the main job function:
s.enter(5, 1, job, ('Subjob',))  # schedule this subjob
```

**Creating a Cron-like Job:**

```python
import sched

def job(name):
    print(f"Running job: {name}")

# Schedule tasks with different frequencies.
s = sched.scheduler(time.time, time.sleep)

def daily_job():
    s.enter(86400, 0, job, ('Daily',))  # every day at midnight.

def weekly_job():
    s.enter(604800, 0, job, ('Weekly',))  # every Sunday.

# Start the scheduler and keep it running.
while True:
    try:
        s.run()
    except KeyboardInterrupt:
        print('\nScheduler stopped.')
        break
```

**Real-World Example:**

Suppose we want to create a simple email sender that sends emails at specific times. We can use the `sched` module to schedule tasks.

```python
import sched
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message):
    # Simulate sending an email.
    print(f"Sending email with subject: {subject}")
    print(message)

s = sched.scheduler(time.time, time.sleep)

# Schedule tasks to run at different times.
s.enter(86400, 0, send_email, ('Hello from cron', 'This is a test email.'))  # every day at midnight.
s.enter(604800, 1, send_email, ('Good morning!', 'This is another test email.'))  # every Sunday.

# Start the scheduler and keep it running.
while True:
    try:
        s.run()
    except KeyboardInterrupt:
        print('\nScheduler stopped.')
        break
```

Note: This example simulates sending emails. In a real-world scenario, you would use an actual email library to send emails programmatically.
