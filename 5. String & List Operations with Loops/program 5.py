# Q5: Write a program that counts the number of words in a sentence. 
#     You may assume words are separated by spaces.

string = input("Enter a sentence: ")
count = 0
in_word = False
for char in string:
    if char != " " and not in_word:
        count += 1
        in_word = True
    elif char == " ":
        in_word = False
print("Number of words:", count)
