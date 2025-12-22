# nnums = [100, 4, 200, 1, 3, 2]
# Output: 4  # sequence [1,2,3,4]

nnums = [100, 4, 200, 1, 3, 2]

nums_set = set(nnums)
longest = 0

for num in nums_set:
    if num - 1 not in nums_set:          
        length = 1
        while num + length in nums_set:  
            length += 1
        longest = max(longest, length)

print(longest)
 