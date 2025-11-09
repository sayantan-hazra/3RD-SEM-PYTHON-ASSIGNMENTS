# Q8: Write a Python Program to Square Each Element of the List 
#     and Print List in Reverse Order.

def square_reverse(lst):
    squared = []
    for i in lst:
        squared.append(i * i)
    return squared[::-1]

print("Squared & reversed:", square_reverse([1, 2, 3, 4]))
