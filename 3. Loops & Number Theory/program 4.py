# 4. Fibonacci sequence up to n numbers
n = int(input("Enter how many Fibonacci numbers: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1
