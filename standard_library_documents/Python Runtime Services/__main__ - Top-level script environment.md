# __main__ - Top-level script environment

The `__main__` module is a special module in Python that serves as the entry point for standalone scripts or when a script is executed from the command line. It allows you to define functions, classes, and variables that are not accessible by other modules.

Here's a comprehensive set of code examples demonstrating different functionalities within the `__main__` module:

### Example 1: Printing a Message

```python
# Main script file, e.g., my_script.py

def main():
    """
    This function is the entry point for the script.
    It prints a welcome message when the script is run.
    """
    print("Welcome to my Python script!")

if __name__ == "__main__":
    # Check if this script is being run directly (not imported)
    main()
```

### Example 2: Defining a Function with Command-Line Arguments

```python
import sys

def sum_numbers(numbers):
    """
    This function takes a list of numbers as input and returns their sum.
    It uses command-line arguments for flexibility.
    """
    total = 0
    for number in numbers:
        total += int(number)
    return total

if __name__ == "__main__":
    # Check if this script is being run directly (not imported)
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        result = sum_numbers(numbers)
        print(f"The sum of {numbers} is {result}.")
    else:
        print("Please provide a list of numbers as command-line arguments.")
```

### Example 3: Handling Exceptions

```python
def divide(a, b):
    """
    This function divides two numbers and handles exceptions.
    It returns the result or an error message if division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

if __name__ == "__main__":
    # Check if this script is being run directly (not imported)
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = divide(num1, num2)
        print(f"The result of {num1} divided by {num2} is {result}.")
    except ValueError:
        print("Error: Please enter valid integers.")
```

### Example 4: Using a Main Function

```python
def add(a, b):
    """
    This function adds two numbers.
    It returns the sum of `a` and `b`.
    """
    return a + b

def subtract(a, b):
    """
    This function subtracts `b` from `a`.
    It returns the result of `a - b`.
    """
    return a - b

def multiply(a, b):
    """
    This function multiplies two numbers.
    It returns the product of `a` and `b`.
    """
    return a * b

def divide(a, b):
    """
    This function divides `a` by `b`.
    It returns the result of `a / b`.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

if __name__ == "__main__":
    # Check if this script is being run directly (not imported)
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid choice.")
        exit()

    print(f"The result of {num1} {choice} {num2} is {result}.")
```

### Example 5: Using `if __name__ == "__main__":` for Test Execution

```python
def multiply(a, b):
    """
    This function multiplies two numbers.
    It returns the product of `a` and `b`.
    """
    return a * b

# Test cases to verify the correctness of the multiply function
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 7) == 0
    assert multiply(4.5, 2) == 9.0

if __name__ == "__main__":
    # Check if this script is being run directly (not imported)
    test_multiply()
    print("All tests passed!")
```

### Explanation:

- **Example 1**: Demonstrates how to define a `main` function and use it as the entry point of a script.
- **Example 2**: Shows how to handle command-line arguments and perform calculations based on those inputs.
- **Example 3**: Illustrates error handling using try-except blocks, specifically for division by zero.
- **Example 4**: Provides a simple calculator with menu-driven operations, demonstrating function definition and usage.
- **Example 5**: Uses the `if __name__ == "__main__":` idiom to run test cases only when the script is executed directly.

These examples cover various aspects of using the `__main__` module effectively, from basic structure to more complex interactions with command-line arguments and error handling.
