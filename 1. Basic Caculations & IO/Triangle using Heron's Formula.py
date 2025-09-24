# Program to calculate area of a triangle using Heron's formula

# Input sides of the triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Calculate semi-perimeter
s = (a + b + c) / 2

# Calculate area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The area of the triangle is:", area)
