# Q5: Write a Python program to remove duplicates from a list.

def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
