# encoding: utf-8
# Author: Cai Chenyi

# 插入排序

nums = [13, 8, 1, 2, 7, 3, 11, 10, 0]
for i in range(0, len(nums) - 1):
    for j in range(i + 1, 0, -1):
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
print(nums)