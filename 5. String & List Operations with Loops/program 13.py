# Q13: Write a program in Python to find a character in a given string.

string = input("Enter a string: ")
ch = input("Enter a character to search: ")
found = False
for char in string:
    if char == ch:
        found = True
        break
if found:
    print("Character found in the string.")
else:
    print("Character not found in the string.")
