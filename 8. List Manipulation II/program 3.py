# Q3: Write a Python Program to Interchange First and Last Elements in a List.

def swap_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print("Swapped list:", swap_first_last([1, 2, 3, 4, 5]))
