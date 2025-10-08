# 5. All prime numbers between two ranges
low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))
print("Prime numbers:")
for num in range(low, high + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
