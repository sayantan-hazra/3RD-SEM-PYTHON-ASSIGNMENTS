# Q4: Write a program to remove all spaces from a string using a loop.

string = input("Enter a string: ")
result = ""
for char in string:
    if char != " ":
        result += char
print("String without spaces:", result)
