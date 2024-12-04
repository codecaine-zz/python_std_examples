# fileinput — Iterate over lines from multiple input streams

Here's an example of using the `fileinput` module in Python:

```python
import fileinput

def main():
    # Print a header message to let users know what we're doing
    print("Processing files:")

    # Use the `fileinput` function to iterate over lines from multiple input streams
    for line_num, line in enumerate(fileinput.input()):
        # Print the current line number and line contents
        print(f"Line {line_num+1}: {line.strip()}")

if __name__ == "__main__":
    main()
```

This code will prompt the user to select one or more files to process. It then iterates over each file, printing its line numbers and contents.

Here's a breakdown of what this code does:

*   We import the `fileinput` module.
*   In the `main()` function, we print a header message to let users know that we're processing files.
*   We use the `fileinput.input()` function to get input from standard input (usually the command line). This function returns an iterator over the lines in each file. The `enumerate` function is used to get both the line number and contents.
*   Inside the loop, we print the current line number (`line_num+1`) and its contents using the `strip()` method to remove leading/trailing whitespace.

When you run this code from the command line:

```bash
python fileinput_example.py < file1.txt file2.txt
```

And select a few files, it will display something like this:

```
Processing files:
Line 1: Hello World!
Line 2: This is a test.
Line 3: Line with leading whitespace

Line 4: Another line with trailing whitespace.
Line 5: Another line.

Line 6: Line with extra spaces     .
```
