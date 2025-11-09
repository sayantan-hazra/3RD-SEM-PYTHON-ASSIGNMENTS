# Q7: Write a program that prints all characters of a string 
#     that are at even indexes (0, 2, 4, ...).

string = input("Enter a string: ")
print("Characters at even indexes:", end=" ")
for i in range(0, len(string), 2):
    print(string[i], end=" ")
