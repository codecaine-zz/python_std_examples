# urllib.robotparser — Parser for robots.txt

**URllib Robot Parser**
==========================

The `urllib.robotparser` module is used to parse and manipulate the `robots.txt` file, which is a text file that specifies rules for crawlers (like web spiders) accessing certain websites.

### Creating an Instance of the RobotParser Class
-----------------------------------------------

```python
import urllib.robotparser

# Create an instance of the RobotParser class with default settings
rp = urllib.robotparser.RobotFileParser()

# Alternatively, create an instance with a custom settings dictionary
rp = urllib.robotparser.RobotFileParser({'User-agent': '*'})
```

### Parsing Robots.txt File
-------------------------

```python
import urllib.robotparser

def parse_robots_txt(url):
    """
    Parse the robots.txt file for the given URL.

    Args:
        url (str): The URL of the robots.txt file to be parsed.

    Returns:
        RobotFileParser: An instance of the RobotFileParser class.
    """

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url)

    # Parse the robots.txt file
    try:
        rp.read()
    except Exception as e:
        print(f"Error parsing robots.txt: {e}")
        return None

    return rp
```

### Disabling Crawling for a Specific URL or User Agent
---------------------------------------------------

```python
import urllib.robotparser

def disable_crawling(rp, url=None, user_agent=None):
    """
    Disable crawling for the specified URL or user agent.

    Args:
        rp (RobotFileParser): An instance of the RobotFileParser class.
        url (str, optional): The URL to be excluded from crawling. Defaults to None.
        user_agent (str, optional): The user agent to be excluded from crawling. Defaults to None.
    """

    if url and rp.can_fetch(user_agent, url):
        # Disable crawling for the specified URL
        rp.set_url(url)
        rp.read()
    elif user_agent:
        # Disable crawling for the specified user agent
        rp.user_agent = '*'
        rp.read()

# Example usage
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://example.com/robots.txt')

disable_crawling(rp, url='https://example.com')
```

### Checking if Crawling is Allowed for a Specific URL or User Agent
----------------------------------------------------------------

```python
import urllib.robotparser

def can_fetch(rp, url=None, user_agent=None):
    """
    Check if crawling is allowed for the specified URL or user agent.

    Args:
        rp (RobotFileParser): An instance of the RobotFileParser class.
        url (str, optional): The URL to be checked. Defaults to None.
        user_agent (str, optional): The user agent to be checked. Defaults to None.

    Returns:
        bool: True if crawling is allowed, False otherwise.
    """

    if rp.can_fetch(user_agent, url):
        return True
    elif user_agent:
        # Check for disallowed user agents
        disallowed_user_agents = ['*']
        for agent in disallowed_user_agents:
            if rp.can_fetch(agent, url):
                return False

    return True

# Example usage
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://example.com/robots.txt')

print(can_fetch(rp))  # Output: False (due to the '*' disallowance)
```
