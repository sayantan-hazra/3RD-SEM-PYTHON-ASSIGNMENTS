# 6. Calculate bill amount
qty = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
discount = float(input("Enter discount %: "))
tax = float(input("Enter tax %: "))
total = qty * price
total -= (discount / 100) * total
total += (tax / 100) * total
print("Bill Amount:", total)
