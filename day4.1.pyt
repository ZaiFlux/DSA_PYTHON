arr = [1, 2, 3, 4, 5, 6, 7,8 ,9, 10]
even = 0
for num in arr:
    if num % 2 == 0:
        print(num)
        even += 1
print(f"The number of even is {even}")
    