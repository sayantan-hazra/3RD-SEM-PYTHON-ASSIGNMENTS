# Q17: Write a program in Python to compare two strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

i = 0
while i < len(str1) and i < len(str2):
    if str1[i] < str2[i]:
        print("First string is smaller.")
        break
    elif str1[i] > str2[i]:
        print("First string is greater.")
        break
    i += 1
else:
    if len(str1) < len(str2):
        print("First string is smaller.")
    elif len(str1) > len(str2):
        print("First string is greater.")
    else:
        print("Both strings are equal.")
