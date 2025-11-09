# Q6: Represent a matrix using list of lists and print row-wise.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(" ".join(str(x) for x in row))
