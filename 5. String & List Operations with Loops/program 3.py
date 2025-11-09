# Q3: Write a program that counts the number of consonants in a given string using a loop.

string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in string:
    if char.isalpha() and char not in vowels:
        count += 1
print("Number of consonants:", count)
