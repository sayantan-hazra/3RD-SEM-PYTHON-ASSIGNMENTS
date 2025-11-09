# Q14: Write a program in Python to count the number of characters, 
#      special characters and integers in a given string.

string = input("Enter a string: ")
chars = digits = specials = 0
for char in string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        specials += 1
print("Characters:", chars)
print("Digits:", digits)
print("Special characters:", specials)
