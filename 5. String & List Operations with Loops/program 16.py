# Q16: Write a program in Python to check whether two strings are equal or not.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
equal = True

if len(str1) != len(str2):
    equal = False
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            equal = False
            break

if equal:
    print("Strings are equal.")
else:
    print("Strings are not equal.")
