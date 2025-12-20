# Find **missing number** in range 1..N

numbers = list(map(int, input("Enter the numbers: ").split()))

n = len(numbers) + 1

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing numbers: ", i)