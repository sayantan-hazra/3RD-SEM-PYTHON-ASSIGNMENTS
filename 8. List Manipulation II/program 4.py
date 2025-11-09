# Q4: Write a Python program to count the number of strings in a list.
# Condition: Length >= 2 and first and last characters are the same.

def count_strings(lst):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

print("Count:", count_strings(['abc', 'xyz', 'aba', '1221']))
