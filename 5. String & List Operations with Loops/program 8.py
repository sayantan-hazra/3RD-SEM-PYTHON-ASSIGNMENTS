# Q8: Write a program that prints the frequency of each character 
#     in the string (excluding spaces).

string = input("Enter a string: ")
freq = {}
for char in string:
    if char != " ":
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
print("Character Frequencies:")
for char in freq:
    print(char, ":", freq[char])
