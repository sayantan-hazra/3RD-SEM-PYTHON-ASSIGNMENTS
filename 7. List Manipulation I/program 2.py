# Q2: Write a function that displays all the multiples of 4 within a given range.

def multiples_of_4(start, end):
    print("Multiples of 4:")
    for i in range(start, end + 1):
        if i % 4 == 0:
            print(i, end=" ")

# Example
multiples_of_4(1, 30)
