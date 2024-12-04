# keyword — Testing for Python keywords

Here's an example of how you can use the `keyword` module in Python:

```python
import keyword

# Define a function that takes a word as input and checks if it is a Python keyword
def check_keyword(word):
    """
    Checks if a given word is a Python keyword.

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word is a Python keyword, False otherwise.
    """
    # Use the `iskeyword()` function from the `keyword` module
    return keyword.iskeyword(word)

# Example usage
if __name__ == "__main__":
    words = ["class", "def", "for", "while", "import", "None"]
    
    for word in words:
        if check_keyword(word):
            print(f"'{word}' is a Python keyword.")
        else:
            print(f"'{word}' is not a Python keyword.")

# Output:
# 'class' is a Python keyword.
# 'def' is a Python keyword.
# 'for' is a Python keyword.
# 'while' is a Python keyword.
# 'import' is a Python keyword.
# 'None' is a Python keyword.
```

This code defines a function `check_keyword()` that takes a word as input and uses the `iskeyword()` function from the `keyword` module to check if it's a Python keyword. The example usage shows how to use this function with some common Python keywords.

**Other functions from the `keyword` module:**

- `keyword.kwlist`: Returns a list of all Python keywords.
- `keyword.iskeyword(word)`: Returns `True` if `word` is a Python keyword, `False` otherwise.
