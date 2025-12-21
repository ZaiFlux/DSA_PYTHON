numbers = list(map(int, input("Enter number here: ").split()))

freq = {}

for num in numbers:
    freq.append(num)

if numbers in freq:
    print(freq)