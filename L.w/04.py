nums_1 = [1, 33, 5, 2, 1, 13, 14,  ]
nums_2 = [22, 55, 5, 2, 1, 13, 14,  12, 34]

nums_3 = []

for x in range(len(nums_1)):
    if nums_1[x] in nums_2 and nums_1[x] not in nums_3:
        nums_3.append(nums_1[x])
print(nums_3)

