# re - Regular expression operations

Below are comprehensive code examples covering various functionalities provided by the `re` (regular expressions) module in Python 3.12. These examples include detailed comments explaining each step.

```python
import re

# Example 1: Basic pattern matching using search()
def example_search():
    """
    This function demonstrates basic pattern matching using re.search().
    
    The search() method scans through the string, looking for any location where 
    the regular expression pattern produces a match. It returns a Match object if found.
    If no matches are found, it returns None.
    """
    text = "Hello, my email is example@example.com"
    # Define the regex pattern to find an email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    
    match = re.search(pattern, text)
    if match:
        print(f"Email found: {match.group()}")
    else:
        print("No email found.")

# Example 2: Finding all matches using findall()
def example_findall():
    """
    This function demonstrates finding all non-overlapping matches of a pattern in a string.
    
    The findall() method returns a list containing all the match objects for every match 
    of the pattern found in the string. If no matches are found, it returns an empty list.
    """
    text = "The rain in Spain stays mainly in the plain."
    # Define the regex pattern to find words starting with 's'
    pattern = r"\bs\w+"
    
    matches = re.findall(pattern, text)
    print(f"Matches: {matches}")

# Example 3: Substituting strings using sub()
def example_sub():
    """
    This function demonstrates how to replace parts of a string where the 
    regular expression pattern matches.
    
    The sub() method replaces occurrences of the pattern with the specified replacement. 
    The replacement can be a string or a callable object (a function).
    """
    text = "The quick brown fox jumps over the lazy dog."
    # Define the regex pattern to replace 'fox' with 'cat'
    pattern = r"fox"
    
    # Using a simple string as the replacement
    result = re.sub(pattern, "cat", text)
    print(f"Simple substitution: {result}")
    
    # Using a function as the replacement
    def replacer(match):
        return match.group().upper()
    
    result_func = re.sub(pattern, replacer, text)
    print(f"Function-based substitution: {result_func}")

# Example 4: Compilation and usage of regular expressions using compile()
def example_compile():
    """
    This function demonstrates the use of re.compile() to create a pattern object.
    A compiled pattern can be used for multiple matches without the need to repeat the search().
    
    The compile() method returns a RegexObject that has methods suitable for searching 
    and replacing text according to the regular expression pattern.
    """
    text = "I have 12 apples, 34 bananas, and 56 cherries."
    # Define the regex pattern to find numbers
    pattern = r"\d+"
    
    compiled_pattern = re.compile(pattern)
    
    matches = compiled_pattern.findall(text)
    print(f"Matches: {matches}")

# Example 5: Using patterns with flags using match()
def example_match_flags():
    """
    This function demonstrates the use of different flags in regular expressions.
    
    Flags modify the behavior of a pattern. Commonly used flags include:
        - re.IGNORECASE
        - re.MULTILINE
        - re.DOTALL
    
    The match() method attempts to apply the pattern at the start of the string. 
    It returns a Match object if the pattern is found, otherwise None.
    """
    text = "Hello\nWorld"
    
    # Case-insensitive search
    pattern = r"hello"
    match = re.match(pattern, text, flags=re.IGNORECASE)
    print(f"Match (ignore case): {match}")
    
    # Multiline search
    pattern = r"^Hello.*World$"
    match = re.match(pattern, text, flags=re.MULTILINE)
    if match:
        print("Multiline match: Match found")
    else:
        print("Multiline match: No match")

# Example 6: Matching patterns with lookaheads and lookbehinds
def example_lookahead():
    """
    This function demonstrates the use of positive and negative lookahead and lookbehind assertions.
    
    Lookaheads and lookbehinds are zero-width matching assertions. 
    They check for a pattern without including it in the match result.
    """
    text = "The quick brown fox jumps over the lazy dog."
    
    # Positive lookahead
    pattern = r"fox(?=\s+jumps)"
    matches = re.findall(pattern, text)
    print(f"Positive lookahead: {matches}")
    
    # Negative lookbehind
    pattern = r"(?<!quick)\s+"
    matches = re.findall(pattern, text)
    print(f"Negative lookbehind: {matches}")

# Running the examples
if __name__ == "__main__":
    example_search()
    example_findall()
    example_sub()
    example_compile()
    example_match_flags()
    example_lookahead()
```

This code provides a comprehensive set of examples to demonstrate various functionalities provided by the `re` module, including basic pattern matching, finding all matches, substituting strings, compiling patterns, using flags, and utilizing lookaheads/lookbehinds.
