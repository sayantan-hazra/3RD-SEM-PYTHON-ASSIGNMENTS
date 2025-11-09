# Q5: Merge two lists and remove duplicates.

def merge_remove_duplicates(lst1, lst2):
    merged = lst1 + lst2
    result = []
    for i in merged:
        if i not in result:
            result.append(i)
    return result

print("Merged without duplicates:", merge_remove_duplicates([1,2,3],[3,4,5]))
