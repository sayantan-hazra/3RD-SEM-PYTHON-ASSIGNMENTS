# Q1: Write a Python function to find the maximum of three numbers.

def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example
print("Maximum:", maximum_of_three(10, 25, 15))
