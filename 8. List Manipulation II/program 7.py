# Q7: Write a Python function that takes two lists 
#     and returns True if they have at least one common member.

def common_member(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False

print("Common member:", common_member([1, 2, 3], [4, 5, 3]))
