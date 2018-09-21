nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]

nums_3 = []

for x in range(len(nums_1)):
    if nums_1[x] in nums_2:
        nums_3.append(nums_1[x])
print(nums_3)
