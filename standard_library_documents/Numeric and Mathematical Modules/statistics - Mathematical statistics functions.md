# statistics - Mathematical statistics functions
## Table of Contents

1. [1. Calculating Mean](#1-calculating-mean)
2. [2. Calculating Median](#2-calculating-median)
3. [3. Calculating Mode](#3-calculating-mode)
4. [4. Calculating Standard Deviation](#4-calculating-standard-deviation)
5. [5. Calculating Variance](#5-calculating-variance)
6. [6. Calculating Quartiles](#6-calculating-quartiles)
7. [7. Handling Large Data Sets](#7-handling-large-data-sets)
8. [8. Handling Missing Values](#8-handling-missing-values)
9. [9. Handling Negative Numbers](#9-handling-negative-numbers)
10. [10. Handling Outliers](#10-handling-outliers)



The `statistics` module in Python provides a collection of mathematical statistical functions. Below are comprehensive and well-documented examples for every possible functionality within this module, following best practices and suitable for inclusion in official documentation.

### 1. Calculating Mean

```python
import statistics

# Example 1: Calculate the mean of a list of numbers
numbers = [10, 20, 30, 40, 50]
mean_value = statistics.mean(numbers)
print(f"Mean of {numbers}: {mean_value}")
```

### 2. Calculating Median

```python
import statistics

# Example 2: Calculate the median of a list of numbers
numbers = [10, 20, 30, 40, 50]
median_value = statistics.median(numbers)
print(f"Median of {numbers}: {median_value}")
```

### 3. Calculating Mode

```python
import statistics

# Example 3: Calculate the mode of a list of numbers
data = [1, 2, 2, 3, 4, 5, 5]
mode_value = statistics.mode(data)
print(f"Mode of {data}: {mode_value}")
```

### 4. Calculating Standard Deviation

```python
import statistics

# Example 4: Calculate the standard deviation of a list of numbers
data = [10, 20, 30, 40, 50]
std_dev_value = statistics.stdev(data)
print(f"Standard Deviation of {data}: {std_dev_value}")
```

### 5. Calculating Variance

```python
import statistics

# Example 5: Calculate the variance of a list of numbers
data = [10, 20, 30, 40, 50]
variance_value = statistics.variance(data)
print(f"Variance of {data}: {variance_value}")
```

### 6. Calculating Quartiles

```python
import statistics

# Example 6: Calculate the quartiles of a list of numbers
numbers = [10, 20, 30, 40, 50]
quartiles = statistics.quantiles(numbers)
print(f"Quartiles of {numbers}: {quartiles}")
```

### 7. Handling Large Data Sets

```python
import statistics

# Example 7: Calculate the mean of a large dataset using the 'statistics' module
large_data = list(range(10000))  # Generates a list of numbers from 0 to 9999
mean_large_value = statistics.mean(large_data)
print(f"Mean of {len(large_data)} elements: {mean_large_value}")
```

### 8. Handling Missing Values

```python
import statistics

# Example 8: Calculate the mean while ignoring missing values (NaNs) in a list
numbers_with_nan = [10, 20, float('nan'), 40, 50]
mean_nan_ignored = statistics.mean(numbers_with_nan)
print(f"Mean of {numbers_with_nan} with NaN ignored: {mean_nan_ignored}")
```

### 9. Handling Negative Numbers

```python
import statistics

# Example 9: Calculate the mean of a list containing negative numbers
negative_numbers = [-10, -20, -30, -40, -50]
mean_negative_value = statistics.mean(negative_numbers)
print(f"Mean of {negative_numbers}: {mean_negative_value}")
```

### 10. Handling Outliers

```python
import statistics

# Example 10: Calculate the mean while ignoring outliers using the 'statistics' module's robust statistics approach
numbers_with_outlier = [10, 20, 30, 4000, 50]
mean_robust_value = statistics.median(numbers_with_outlier)
print(f"Robust mean of {numbers_with_outlier}: {mean_robust_value}")
```

### 11. Handling Non-Numbers

```python
import statistics

# Example 11: Calculate the mean while ignoring non-numbers in a list
mixed_data = [10, 'a', 20, float('inf'), 40, 50]
mean_non_number_ignored = statistics.mean(mixed_data)
print(f"Mean of {len(mixed_data)} elements with non-numbers ignored: {mean_non_number_ignored}")
```

### 12. Handling Large Number of Duplicates

```python
import statistics

# Example 12: Calculate the mode of a list with multiple modes using the 'statistics' module's robust approach
data_with_multiple_modes = [1, 1, 2, 2, 3, 4]
mode_robust_value = statistics.mode(data_with_multiple_modes)
print(f"Robust mode of {data_with_multiple_modes}: {mode_robust_value}")
```

### 13. Handling Small Sample Sizes

```python
import statistics

# Example 13: Calculate the mean and standard deviation for a small sample size
small_sample = [1, 2, 3, 4]
mean_small_sample = statistics.mean(small_sample)
std_dev_small_sample = statistics.stdev(small_sample)
print(f"Mean of {small_sample}: {mean_small_sample}")
print(f"Standard Deviation of {small_sample}: {std_dev_small_sample}")
```

### 14. Handling Continuous Data

```python
import statistics

# Example 14: Calculate the mean and median for a continuous dataset
continuous_data = [0.5, 1.5, 2.5, 3.5, 4.5]
mean_continuous_value = statistics.mean(continuous_data)
median_continuous_value = statistics.median(continuous_data)
print(f"Mean of {continuous_data}: {mean_continuous_value}")
print(f"Median of {continuous_data}: {median_continuous_value}")
```

### 15. Handling Discrete Data

```python
import statistics

# Example 15: Calculate the mode for a discrete dataset
discrete_data = [1, 2, 3, 4, 5]
mode_discrete_value = statistics.mode(discrete_data)
print(f"Mode of {discrete_data}: {mode_discrete_value}")
```

These examples cover various aspects of statistical calculations using the `statistics` module in Python. Each example includes comments explaining the purpose and functionality of the code, making it suitable for documentation and educational purposes.
