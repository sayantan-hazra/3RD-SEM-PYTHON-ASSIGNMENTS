# Q9: Write a Program in Python to Print Elements 
#     With Frequency Greater Than a Given Value k.

def freq_greater_than_k(lst, k):
    res_list = []
    for i in lst:
        count = 0
        for j in lst:
            if j == i:
                count += 1
        if count > k and i not in res_list:
            res_list.append(i)
    return res_list

print("Elements with freq > k:", freq_greater_than_k([1,1,1,2,2,3,3,5,5,6,7], 2))
