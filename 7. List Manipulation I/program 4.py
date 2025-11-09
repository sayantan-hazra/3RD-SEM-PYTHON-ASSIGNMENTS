# Q4: Write a function that will take the height and symbol as input 
#     and print the triangle.
# Example: height = 5, symbol = "*"

def print_triangle(height, symbol):
    for i in range(1, height + 1):
        for j in range(i):
            print(symbol, end=" ")
        print()

# Example
print_triangle(5, "*")
