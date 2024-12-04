# getpass — Portable password input

**getpass Module**
=================

The `getpass` module provides a way to get sensitive information like passwords from the user without echoing it on the terminal.

### Functions

#### `getpass([prompt])`

*   **Description:** Prompts the user to enter a password.
*   **Parameters:**

    *   `prompt`: Optional. A string that appears above the input prompt.
*   **Returns:** The password entered by the user as a string.

```python
import getpass

def main():
    # Get the password from the user without echoing it on the terminal
    password = getpass.getpass("Enter your password: ")
    
    # Print the entered password
    print("You entered:", password)

if __name__ == "__main__":
    main()
```

#### `getpass(getprompt=None)`

*   **Description:** Prompts the user to enter a password and returns the result.
*   **Parameters:**

    *   `getprompt`: Optional. A function that generates a prompt string. If None, uses a default prompt.

```python
import getpass

def custom_prompt():
    """Generate a custom prompt"""
    return "Enter your password: "

def main():
    # Get the password from the user using a custom prompt
    password = getpass.getpass(custom_prompt)
    
    # Print the entered password
    print("You entered:", password)

if __name__ == "__main__":
    main()
```

#### `getuser()`

*   **Description:** Returns the username of the current user.
*   **Returns:** The username as a string.

```python
import getpass

def main():
    # Get the username of the current user
    username = getpass.getuser()
    
    # Print the entered username
    print("Your username is:", username)

if __name__ == "__main__":
    main()
```

### Example Use Cases:

*   Getting a password from a user without echoing it on the terminal.
*   Generating a custom prompt for password input.
*   Getting the username of the current user.

### API Documentation

```python
getpass([prompt=None])

    Prompt the user to enter a password and return the result.

    Args:
        prompt (str, optional): A string that appears above the input prompt. Defaults to None.

    Returns:
        str: The password entered by the user.
```

```python
getuser()

    Return the username of the current user.

Returns:
    str: The username as a string.
```
