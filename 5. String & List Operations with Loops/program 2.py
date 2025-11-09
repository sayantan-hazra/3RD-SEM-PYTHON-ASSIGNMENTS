# Q2: Write a program that counts the number of vowels (a, e, i, o, u) 
#     in a given string using a loop.

string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
