# Q2: Input n numbers into a list and print sum, largest, smallest.

def list_summary(lst):
    total = sum(lst)
    largest = max(lst)
    smallest = min(lst)
    print("Sum:", total)
    print("Largest:", largest)
    print("Smallest:", smallest)

list_summary([10, 3, 7, 25, 5])
