# Q20: Write a program in Python to find the index of a character 
#      in a given string in reverse order.

string = input("Enter a string: ")
ch = input("Enter character to find index from reverse: ")
index = -1
for i in range(len(string) - 1, -1, -1):
    if string[i] == ch:
        index = i
        break
if index != -1:
    print("Index from reverse:", index)
else:
    print("Character not found in the string.")
