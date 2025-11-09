# Q12: Write a program in Python to concatenate two strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = ""
for char in str1:
    result += char
for char in str2:
    result += char
print("Concatenated string:", result)
