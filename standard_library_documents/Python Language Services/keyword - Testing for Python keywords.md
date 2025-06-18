# keyword - Testing for Python keywords
## Table of Contents

1. [Example 1: Basic Usage](#example-1-basic-usage)
2. [Example 2: Using `all()` with `keyword.iskeyword()`](#example-2-using-all-with-keywordiskeyword)
3. [Example 3: Handling Non-String Inputs](#example-3-handling-non-string-inputs)
4. [Example 4: Testing Keywords in Specific Contexts](#example-4-testing-keywords-in-specific-contexts)
5. [Example 5: Using `list()` to Get All Keywords](#example-5-using-list-to-get-all-keywords)
6. [Example 6: Using `in` Operator to Check if a String is a Keyword](#example-6-using-in-operator-to-check-if-a-string-is-a-keyword)
7. [Example 7: Testing Keywords in Different Programming Styles](#example-7-testing-keywords-in-different-programming-styles)
8. [Example 8: Testing Keywords in Different Module Contexts](#example-8-testing-keywords-in-different-module-contexts)



The `keyword` module in Python is used to test if a given string is a reserved word in the language. It provides a function called `iskeyword()` that returns `True` if the string is a keyword and `False` otherwise.

Here are some examples of how to use the `keyword` module:

### Example 1: Basic Usage

```python
import keyword

# Check if 'def' is a keyword
print(keyword.iskeyword('def'))  # Output: True

# Check if 'if' is also a keyword
print(keyword.iskeyword('if'))    # Output: True

# Check if 'not' is not a keyword
print(keyword.iskeyword('not'))   # Output: False

# Check if '0x123' is not a keyword
print(keyword.iskeyword('0x123'))  # Output: False
```

### Example 2: Using `all()` with `keyword.iskeyword()`

```python
import keyword

# List of words to test
words_to_test = ['def', 'if', 'not', '0x123', 'True']

# Check if all elements in the list are keywords
print(all(keyword.iskeyword(word) for word in words_to_test))  # Output: True
```

### Example 3: Handling Non-String Inputs

```python
import keyword

# Attempt to use iskeyword() with a non-string input
try:
    print(keyword.iskeyword(123))   # Raises TypeError
except TypeError as e:
    print(e)  # Output: iskeyword() argument must be a string, not int
```

### Example 4: Testing Keywords in Specific Contexts

```python
import keyword

# Check if keywords are correctly recognized in function definitions
def my_function():
    pass

print(keyword.iskeyword('my_function'))  # Output: False

# Define a local variable named 'for'
for i in range(10):
    pass

print(keyword.iskeyword('for'))  # Output: True

# Check if keywords are correctly recognized in class definitions
class MyClass:
    pass

print(keyword.iskeyword('MyClass'))  # Output: False
```

### Example 5: Using `list()` to Get All Keywords

```python
import keyword

# Convert all keywords into a list
all_keywords = list(keyword.kwlist)

# Print the first and last keywords in the list
print("First keyword:", all_keywords[0])  # Output: 'False'
print("Last keyword:", all_keywords[-1])   # Output: 'yield'
```

### Example 6: Using `in` Operator to Check if a String is a Keyword

```python
import keyword

# List of words to check against keywords
words = ['def', 'if', 'else', 'return']

# Use the in operator to check each word
for word in words:
    print(f"'{word}' is a keyword: {keyword.iskeyword(word)}")
```

### Example 7: Testing Keywords in Different Programming Styles

```python
import keyword

# Define a function using keyword-style argument assignment
def my_function(name='World'):
    print(f'Hello, {name}!')

# Check if 'print' and 'if' are keywords
print(keyword.iskeyword('print'))   # Output: False
print(keyword.iskeyword('if'))    # Output: True

# Define a class with keyword-style member variables
class MyClass:
    def __init__(self, name):
        self.name = name

# Check if 'name' is a keyword
print(keyword.iskeyword('name'))  # Output: False
```

### Example 8: Testing Keywords in Different Module Contexts

```python
import keyword

# Define a function using keyword-style argument assignment in another module
def my_function(name='World'):
    print(f'Hello, {name}!')

# Check if 'print' and 'if' are keywords
print(keyword.iskeyword('print'))   # Output: False
print(keyword.iskeyword('if'))    # Output: True

# Define a class with keyword-style member variables in another module
class MyClass:
    def __init__(self, name):
        self.name = name

# Check if 'name' is a keyword
print(keyword.iskeyword('name'))  # Output: False
```

These examples demonstrate various use cases of the `keyword` module, including basic testing, handling non-string inputs, and understanding keywords in different programming contexts.
