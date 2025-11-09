# Q4: Write a Python function that accepts a string and counts 
#     the number of upper and lower case letters.

def count_case(s):
    upper = lower = 0
    for char in s:
        if 'A' <= char <= 'Z':
            upper += 1
        elif 'a' <= char <= 'z':
            lower += 1
    print("No. of Upper case characters:", upper)
    print("No. of Lower case characters:", lower)

# Example
count_case("The quick Brow Fox")
