# Q7: Write a program to check whether a given element exists in a list or not.

def element_exists(lst, elem):
    for i in lst:
        if i == elem:
            return True
    return False

print("Exists?", element_exists([10,20,30,40], 30))
