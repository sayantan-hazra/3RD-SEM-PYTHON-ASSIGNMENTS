# Q6: A palindrome is a string that reads the same backward as forward. 
#     Write a program to check if a given string is a palindrome using loops.

string = input("Enter a string: ")
reversed_str = ""
for char in string:
    reversed_str = char + reversed_str
if string == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")
