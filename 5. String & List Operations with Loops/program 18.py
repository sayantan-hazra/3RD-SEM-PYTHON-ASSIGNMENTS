# Q18: Write a program in Python to check whether a given substring exists in a string or not.

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

found = False
for i in range(len(string) - len(substring) + 1):
    match = True
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match = False
            break
    if match:
        found = True
        break

if found:
    print("Substring exists in the string.")
else:
    print("Substring does not exist in the string.")
