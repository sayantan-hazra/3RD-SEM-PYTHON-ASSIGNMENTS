# Q1: Write a program that takes a string input from the user 
#     and prints the reversed string using a loop.

string = input("Enter a string: ")
reversed_str = ""
for char in string:
    reversed_str = char + reversed_str
print("Reversed String:", reversed_str)
