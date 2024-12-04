# readline - GNU readline interface

The `readline` module in Python provides a convenient way to handle command line editing, history management, and completion features using GNU Readline.

Here are comprehensive code examples demonstrating various functionalities of the `readline` module:

### 1. Basic Usage

```python
import readline

# Prompt the user for input with basic readline capabilities
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
```

### 2. Customizing the Prompt

You can customize the prompt to provide more context or instructions to the user.

```python
import readline

def custom_prompt(line):
    return ">>> "

readline.set_completer_delims(' \t\n')
readline.set_completer(complete_func)
readline.set_startup_hook(lambda: readline.parse_and_bind("tab: complete"))
readline.parse_and_bind("set show-all-if-ambiguous on")
readline.parse_and_bind("bind ^I rl_complete")  # Use Tab for completion

def complete_func(text, state):
    lines = ["apple", "banana", "cherry"]
    return (lines[state] + ' ') if state < len(lines) else None

readline.set_pre_input_hook(custom_prompt)
```

### 3. Adding History Management

The `readline` module supports history management using the `history` list.

```python
import readline

# Append input to the history list
readline.add_history("first entry")
readline.add_history("second entry")

# Retrieve and print a specific entry from the history list
print(f"History item 1: {readline.get_history_item(1)}")
```

### 4. Using Completion Functions

Completion functions allow you to provide suggestions based on user input.

```python
import readline

def complete_func(text, state):
    lines = ["apple", "banana", "cherry"]
    return (lines[state] + ' ') if state < len(lines) else None

readline.set_completer(complete_func)
readline.parse_and_bind("tab: complete")
```

### 5. Prompting with Multiple Choices

You can prompt the user for multiple choices by using a custom completion function.

```python
import readline

def choice_completion(text, state):
    choices = ["yes", "no", "maybe"]
    return (choices[state] + ' ') if state < len(choices) else None

readline.set_completer(choice_completion)
readline.parse_and_bind("tab: complete")

user_choice = input("Do you agree? (yes/no/maybe): ")
print(f"Your choice was: {user_choice}")
```

### 6. Using Pre Input Hooks

Pre-input hooks allow you to modify user input before it is processed.

```python
import readline

def custom_prompt(line):
    return ">>> "

readline.set_completer_delims(' \t\n')
readline.set_completer(complete_func)
readline.set_startup_hook(lambda: readline.parse_and_bind("tab: complete"))
readline.parse_and_bind("set show-all-if-ambiguous on")
readline.parse_and_bind("bind ^I rl_complete")  # Use Tab for completion

def complete_func(text, state):
    lines = ["apple", "banana", "cherry"]
    return (lines[state] + ' ') if state < len(lines) else None

readline.set_pre_input_hook(custom_prompt)
```

### 7. Using History Manipulation Functions

The `history` list provides functions to manipulate history entries.

```python
import readline

# Append a new entry to the history
readline.add_history("first entry")

# Delete an entry from the history by index
readline.remove_history_item(0)

# Retrieve all entries in the history as a list
history_list = readline.get_current_history_length()
print(f"Number of history items: {history_list}")

# Clear the entire history
readline.clear_history()
```

### 8. Using Readline Options

You can set various options to customize the behavior of `readline`.

```python
import readline

# Set option to display all possible completions when ambiguous
readline.set_show_all_if_ambiguous(True)

# Enable tab completion
readline.parse_and_bind("tab: complete")

# Disable echo of typed characters
readline.set_echo_mode(False)
```

These examples cover a range of functionalities available in the `readline` module, demonstrating how to customize prompts, manage history, implement completions, and manipulate user input through pre-input hooks.
