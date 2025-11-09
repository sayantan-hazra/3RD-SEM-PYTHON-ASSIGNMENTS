# Q9: Write a program that replaces every vowel in a string with the character *.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for char in string:
    if char in vowels:
        result += "*"
    else:
        result += char
print("Modified string:", result)
