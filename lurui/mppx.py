nums=[6,11,7,9,4,2,1]
print('要排序的数字为：', str(nums))
i = 0
while i < 7:
    j = 0
    while j < i:
        if nums[i] < nums[j]:
            x = 0
            x = nums[j]
            nums[j] = nums[i]
            nums[i] = x
        j += 1
    i += 1
print('排序后的数字：',str(nums))
print('最大的数字为：', str(nums[6]))
