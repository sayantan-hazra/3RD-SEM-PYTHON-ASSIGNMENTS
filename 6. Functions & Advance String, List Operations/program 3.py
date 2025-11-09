# Q3: Write a Python function to check whether a number falls within a given range.

def in_range(n, start, end):
    if start <= n <= end:
        return True
    else:
        return False

# Example
print("Is in range:", in_range(10, 5, 15))
