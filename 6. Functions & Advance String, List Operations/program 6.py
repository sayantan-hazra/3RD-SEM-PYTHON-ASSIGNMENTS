# Q6: Write a Python function that checks whether a passed string is a palindrome or not.

def is_palindrome(s):
    rev = ""
    for char in s:
        rev = char + rev
    return s == rev

# Example
print("Is palindrome:", is_palindrome("madam"))
print("Is palindrome:", is_palindrome("hello"))
