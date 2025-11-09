# Q3: Reverse a list without using reverse() function.

def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev

print("Reversed:", reverse_list([1, 2, 3, 4, 5]))
