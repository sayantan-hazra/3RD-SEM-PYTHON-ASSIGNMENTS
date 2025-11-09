# 6. Count letters, digits, and special symbols
s = input("Enter a string: ")
letters = digits = symbols = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1
print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", symbols)

