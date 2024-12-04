# re — Regular expression operations

**Regular Expression Operations using re Module**
=====================================================

The `re` module in Python provides support for regular expressions, which are a powerful way to match patterns in strings.

### Importing the `re` Module

To use the `re` module, you need to import it in your Python script or interactive session:
```python
import re
```

### Patterns and Substitutions

Regular expressions can be used to search for patterns in strings and make substitutions. Here are a few examples:

#### Pattern Matching

You can use regular expressions to match patterns in strings using the `search()` function:
```python
import re

# Define a pattern
pattern = r"\d{4}-\d{2}-\d{2}"  # Matches dates in YYYY-MM-DD format

# Search for matches
date_str = "My birthday is February 12, 1990."
match = re.search(pattern, date_str)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")
```

#### Substitutions

You can use regular expressions to make substitutions in strings using the `sub()` function:
```python
import re

# Define a pattern and replacement string
pattern = r"\d{4}"
replacement = "XXXX"

# Search for matches and substitute
date_str = "My birthday is February 12, 1990."
new_date_str = re.sub(pattern, replacement, date_str)

print("New date:", new_date_str)
```

#### Searching and Replacing Multiple Occurrences

You can use the `findall()` function to search for all occurrences of a pattern in a string:
```python
import re

# Define a pattern
pattern = r"\d{4}-\d{2}-\d{2}"

# Search for matches
date_strs = ["My birthday is February 12, 1990.", "My anniversary is June 20, 2001."]
matches = re.findall(pattern, date_strs)

print("Matches:", matches)
```

#### Compiling Regular Expressions

You can use the `compile()` function to compile regular expressions into a pattern object:
```python
import re

# Define a pattern
pattern = r"\d{4}-\d{2}-\d{2}"

# Compile the pattern
compiled_pattern = re.compile(pattern)

# Search for matches using the compiled pattern
date_strs = ["My birthday is February 12, 1990.", "My anniversary is June 20, 2001."]
for date_str in date_strs:
    match = compiled_pattern.search(date_str)
    if match:
        print("Match found:", match.group())
```

### Common Regular Expression Syntax

Here are some common regular expression syntax elements:

* `.` matches any single character
* `^` matches the start of a string
* `$` matches the end of a string
* `*` matches zero or more occurrences of the preceding element
* `+` matches one or more occurrences of the preceding element
* `?` matches zero or one occurrence of the preceding element
* `{n}` matches exactly n occurrences of the preceding element
* `{n, m}` matches at least n and at most m occurrences of the preceding element
* `[abc]` matches any single character in the set
* `\d` matches a digit
* `\w` matches a word character (alphanumeric plus underscore)
* `\s` matches a whitespace character

### Best Practices

Here are some best practices for using regular expressions:

* Use raw strings (`r"..."`) to avoid backslash escaping issues.
* Use `re.escape()` to escape special characters in your patterns.
* Test your patterns using the `re.test()` function before searching for matches.
* Use the `re.IGNORECASE` flag to make matching case-insensitive.

Note: This is not an exhaustive list of regular expression operations, but it covers many common use cases. For more information, see the Python [official documentation](https://docs.python.org/3/library/re.html) and the [regular expression documentation](https://www.regular-expressions.info/.
