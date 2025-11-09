# 7. Count number of each vowel in a string
s = input("Enter a string: ").lower()
vowels = "aeiou"
for v in vowels:
    print(f"{v}: {s.count(v)}")
