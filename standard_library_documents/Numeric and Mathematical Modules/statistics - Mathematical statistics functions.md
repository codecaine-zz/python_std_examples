# statistics — Mathematical statistics functions

Here's an example of how you can use the `statistics` module in Python 3.12:

```python
# Importing the statistics module
import statistics

def main():
    # Example 1: Finding the mean (average) of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    mean = statistics.mean(numbers)
    print("Mean:", mean)

    # Example 2: Finding the median of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    median = statistics.median(numbers)
    print("Median:", median)

    # Example 3: Finding the mode (most frequently occurring value) of a list of numbers
    numbers = [1, 2, 2, 3, 3, 3]
    try:
        mode = statistics.mode(numbers)
        print("Mode:", mode)
    except statistics.StatisticsError:
        print("No unique mode found")

    # Example 4: Finding the standard deviation of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    stdev = statistics.stdev(numbers)
    print("Standard Deviation:", stdev)

    # Example 5: Finding the variance of a list of numbers
    numbers = [1, 2, 3, 4, 5]
    try:
        variance = statistics.variance(numbers)
        print("Variance:", variance)
    except statistics.StatisticsError:
        print("No unique mean found")

if __name__ == "__main__":
    main()
```

The `statistics` module includes functions for calculating various mathematical statistics:

*   `mean`: returns the arithmetic mean (average) of a list of numbers.
*   `median`: returns the median of a sorted list of numbers.
*   `mode`: returns the most frequently occurring value in a list of numbers. If there is no unique mode, it raises a `StatisticsError`.
*   `stdev`: returns the standard deviation of a list of numbers.
*   `variance`: returns the variance of a list of numbers.

Please note that for certain functions like `mode`, `stdev` and `variance`, they require the input data to be sorted, so you need to sort the input before calling these functions. 

Also note that in case of floating point operations some results may have tiny rounding errors due to limitations in binary representation, but these should not affect your program's behavior for most practical purposes.

Each function has a corresponding function with an `Error` raised if you try to use it on non-numeric data or if the number is less than 1 and the function used.
