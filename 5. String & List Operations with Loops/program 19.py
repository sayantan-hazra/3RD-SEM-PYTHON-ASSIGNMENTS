# Q19: Write a program in Python to find index of a given character in a string.

string = input("Enter a string: ")
ch = input("Enter character to find index: ")
index = -1
for i in range(len(string)):
    if string[i] == ch:
        index = i
        break
if index != -1:
    print("Index of character:", index)
else:
    print("Character not found in the string.")
