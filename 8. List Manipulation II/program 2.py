# Q2: Write a Program in Python to Find the Smallest and the Largest 
#     List Elements on Inputs Provided by the User

def min_max(lst):
    smallest = largest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return smallest, largest

print("Min, Max:", min_max([10, 3, 25, 7, 19]))
