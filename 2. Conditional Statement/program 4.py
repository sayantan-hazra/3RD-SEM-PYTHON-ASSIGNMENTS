# 4. Age category
age = int(input("Enter age: "))
if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20 <= age <= 64:
    print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Invalid age")
