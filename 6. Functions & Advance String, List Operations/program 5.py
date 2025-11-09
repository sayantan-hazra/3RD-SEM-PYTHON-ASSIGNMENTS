# Q5: Write a Python function that takes a number as a parameter 
#     and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example
print("Is prime:", is_prime(17))
