# arr = [4,3,2,7,8,2,3,1]
# Output: [2,3]

arr = [4, 3, 2, 7, 8, 2, 3, 1]

checked_num = set()
duplicate_num = set()

for num in arr:
    if num in checked_num:
        duplicate_num.add(num)
    else: 
        checked_num.add(num)

print(list(duplicate_num))


