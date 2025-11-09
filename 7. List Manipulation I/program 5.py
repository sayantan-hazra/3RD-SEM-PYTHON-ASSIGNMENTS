# Q5: Write a function that will print all the even multiples of 3 within a given range.

def even_multiples_of_3(start, end):
    print("Even multiples of 3:")
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 2 == 0:
            print(i, end=" ")

# Example
even_multiples_of_3(1, 50)
