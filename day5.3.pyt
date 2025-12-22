# arr = [1, 2, 3, 7, 5]
# k = 12
# Output: (1, 3)

arr = [1, 2, 3, 7, 5]
k = 12

for i in range(len(arr)):
   total = 0
   for j in range(i, len(arr)):
        total += arr[j]
        if total == k:
            print(arr[i:j+1])
            break
            


