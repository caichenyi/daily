# encoding: utf-8
# Author: Cai Chenyi

'''
二分查找
'''

nums = [6, 11, 12, 13, 15, 16, 24, 32]
print(nums)

find = int(input('Please Input Find NUM:'))
start = 0
end = len(nums)

while True:
    middle = (start + end) // 2
    if find == nums[middle]:
        print('找到了{}，索引位置{}'.format(find, middle))
        break
    elif find < nums[middle]:
        end = middle - 1
    else:
        start = middle + 1
    if end < start:
        print('没有找到{}'.format(find))
        break
