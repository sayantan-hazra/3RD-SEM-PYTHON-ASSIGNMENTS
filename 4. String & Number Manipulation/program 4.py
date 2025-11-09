# 4. Check whether a number is Armstrong
num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum_pow = 0
while temp != 0:
    digit = temp % 10
    sum_pow += digit ** order
    temp //= 10
if sum_pow == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
