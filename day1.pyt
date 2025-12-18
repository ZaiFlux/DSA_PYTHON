# Find the **second largest number** in a list

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a > c and a < b):
    print(f"{a} is the second largest number.")
elif (b > a and b < c) or (b > c and b < a):
    print(f"{b} is the second larget number.")
else: 
    print("Invalid input")

