# Q1: Write a Python program using function that accepts an integer (n) 
#     and computes the value of n + nn + nnn.
# Example: if n = 5, Result = 615

def compute_value(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    return n + nn + nnn

# Example
print("Result:", compute_value(5))
