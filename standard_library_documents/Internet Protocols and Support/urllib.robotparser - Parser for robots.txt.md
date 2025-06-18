# urllib.robotparser - Parser for robots.txt
## Table of Contents

1. [1. Checking Robots.txt for Disallowed Paths](#1-checking-robotstxt-for-disallowed-paths)
2. [2. Handling Different User Agents](#2-handling-different-user-agents)
3. [3. Monitoring Changes to Robots.txt](#3-monitoring-changes-to-robotstxt)
4. [4. Parsing Robots.txt for Disallowed Paths with a List of URLs](#4-parsing-robotstxt-for-disallowed-paths-with-a-list-of-urls)
5. [5. Handling Custom Paths in Robots.txt](#5-handling-custom-paths-in-robotstxt)



The `urllib.robotparser` module is part of Python's standard library, and it provides tools to parse a `robots.txt` file, which specifies rules about which web pages search engines should or should not index. Below are comprehensive code examples that demonstrate various functionalities provided by the `urllib.robotparser` module.

### 1. Checking Robots.txt for Disallowed Paths

```python
from urllib.robotparser import RobotFileParser

def check_disallowed_paths(url):
    # Create a RobotFileParser instance and set the URL of the robots.txt file
    robot_file = RobotFileParser()
    robot_file.set_url(url)

    # Read the robots.txt file
    robot_file.read()

    # Define the URLs you want to check
    urls_to_check = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/disallowed-page"
    ]

    # Check which URLs are allowed or disallowed
    for url in urls_to_check:
        if robot_file.can_fetch('*', url):
            print(f"Allowed: {url}")
        else:
            print(f"Disallowed: {url}")

# Example usage
check_disallowed_paths("http://example.com/robots.txt")
```

### 2. Handling Different User Agents

```python
from urllib.robotparser import RobotFileParser

def check_user_agent(url, user_agent):
    # Create a RobotFileParser instance and set the URL of the robots.txt file
    robot_file = RobotFileParser()
    robot_file.set_url(url)

    # Read the robots.txt file
    robot_file.read()

    # Check if the specified user agent can access the page
    if robot_file.can_fetch(user_agent, url):
        print(f"User-Agent: {user_agent} - Allowed to access {url}")
    else:
        print(f"User-Agent: {user_agent} - Disallowed from accessing {url}")

# Example usage
check_user_agent("http://example.com/robots.txt", "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
```

### 3. Monitoring Changes to Robots.txt

```python
from urllib.robotparser import RobotFileParser, parse_robot_file
import time

def monitor_robots_txt(url):
    # Create a RobotFileParser instance and set the URL of the robots.txt file
    robot_file = RobotFileParser()
    robot_file.set_url(url)

    # Read the initial robots.txt file
    robot_file.read()

    # Store the parsed rules in a dictionary for later comparison
    initial_rules = parse_robot_file(robot_file.get_url())

    try:
        while True:
            # Wait for 10 seconds before checking again
            time.sleep(10)

            # Read the updated robots.txt file
            robot_file.read()

            # Parse the updated rules
            updated_rules = parse_robot_file(robot_file.get_url())

            # Compare the initial and updated rules
            if initial_rules != updated_rules:
                print("robots.txt has been updated.")
                initial_rules = updated_rules

    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Example usage
monitor_robots_txt("http://example.com/robots.txt")
```

### 4. Parsing Robots.txt for Disallowed Paths with a List of URLs

```python
from urllib.robotparser import RobotFileParser

def check_disallowed_paths_for_list(urls):
    # Create a RobotFileParser instance
    robot_file = RobotFileParser()

    # Define the URL of the robots.txt file
    url = "http://example.com/robots.txt"
    robot_file.set_url(url)

    # Read the robots.txt file
    robot_file.read()

    # Check which URLs are allowed or disallowed
    for url in urls:
        if robot_file.can_fetch('*', url):
            print(f"Allowed: {url}")
        else:
            print(f"Disallowed: {url}")

# Example usage
urls = [
    "http://example.com/page1",
    "http://example.com/page2",
    "http://example.com/disallowed-page"
]
check_disallowed_paths_for_list(urls)
```

### 5. Handling Custom Paths in Robots.txt

```python
from urllib.robotparser import RobotFileParser

def check_custom_path(url):
    # Create a RobotFileParser instance and set the URL of the robots.txt file
    robot_file = RobotFileParser()
    robot_file.set_url(url)

    # Read the robots.txt file
    robot_file.read()

    # Define the path you want to check
    path_to_check = "/page1"

    # Check if the specified path is allowed or disallowed
    if robot_file.can_fetch('*', path_to_check):
        print(f"Path: {path_to_check} - Allowed")
    else:
        print(f"Path: {path_to_check} - Disallowed")

# Example usage
check_custom_path("http://example.com/robots.txt")
```

These examples demonstrate how to use the `urllib.robotparser` module to parse and check `robots.txt` files for access control. Each example includes comments explaining key steps and is designed to be clear and self-contained, suitable for integration into larger applications or documentation.
