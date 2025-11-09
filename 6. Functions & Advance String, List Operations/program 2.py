# Q2: Write a Python function to calculate the factorial of a number (non-negative integer).
#     The function accepts the number as an argument.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print("Factorial:", factorial(5))
