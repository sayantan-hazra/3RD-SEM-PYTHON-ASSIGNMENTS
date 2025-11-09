# Q1: Maintain a list of numbers. 
# Perform insert (end/index), delete, display evens, sum/avg, max/min, avg of evens, avg of positives.

def list_operations():
    nums = []

    # Insert at end
    nums.append(10)
    nums.append(20)

    # Insert at index
    nums.insert(1, 15)

    # Delete number
    nums.remove(10)

    # Display even numbers
    evens = [n for n in nums if n % 2 == 0]

    # Sum & Average
    total = sum(nums)
    avg = total / len(nums)

    # Max & Min
    maximum = max(nums)
    minimum = min(nums)

    # Avg of evens
    avg_even = sum(evens) / len(evens) if evens else 0

    # Avg of positives
    positives = [n for n in nums if n > 0]
    avg_pos = sum(positives) / len(positives) if positives else 0

    print("List:", nums)
    print("Even numbers:", evens)
    print("Sum:", total, "Average:", avg)
    print("Max:", maximum, "Min:", minimum)
    print("Avg of evens:", avg_even)
    print("Avg of positives:", avg_pos)

list_operations()
