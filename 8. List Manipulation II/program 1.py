# Q1: Write a Python program to sum all the items in a list.

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

print("Sum:", sum_list([1, 2, 3, 4, 5]))
