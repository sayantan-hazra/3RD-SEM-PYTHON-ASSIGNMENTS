# Q15: Write a program in Python to print only the characters from an alphanumeric string.

string = input("Enter an alphanumeric string: ")
print("Only characters:", end=" ")
for char in string:
    if char.isalpha():
        print(char, end="")
