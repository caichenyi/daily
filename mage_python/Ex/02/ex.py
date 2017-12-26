# encoding: utf-8
# Author: Cai Chenyi

# 定义列表list
nums = [1, 'kk', True, False, 2.2, [1, 2, 3]]
print(nums)

# 打印/修改列表内容
# print(nums[5][1])
# nums[1] = 'caichenyi'
# print(nums[1])

# 遍历输出列表内容
# for i in nums:
#     print(i)

# 将其他可迭代对象转换成列表类型(str)
# STR = 'abc'
# print(list(STR))

# range生成一个可迭代的对象
# print(list(range(16)))
# for i in range(16):
#     print(i)

# range生成一个间隔2次可迭代的对象
# for i in range(10, 21, 2):
#     print(i)

# range生成倒叙列表[9到5]
# for i in range(9, 4, -2):
#     print(i)

# 冒泡排序
# nums = [6, 11, 7, 9, 4, 2, 1]
# for j in range(len(nums) - 1):
#     for i in range(len(nums) - 1 - j):
#         if nums[i] > nums[i + 1]:
#             temp = nums[i]
#             nums[i] = nums[i + 1]
#             nums[i + 1] = temp
# print(nums)

# 着队列中最大值/最小值
# print(max(nums))
# print(min(nums))

# 判断元素是否在列表中
# print(7 in nums)
# print(8 in nums)

# 删除元素
# del nums[0]
# print(nums)

# 列表四则运算
# nums = ['a', 'b']
# print(nums + [1, 2])
# print(nums * 3)

# 切片
# nums = list(range(10))
# print(nums)
# print(nums[:5])
# print(nums[4:])
# print(nums[4:7])
# print(nums[4:7:2])

# 复制/反转列表
# nums = list(range(10))
# nums_temp = nums[:]
# nums_temp_1 = nums[::-1]
# print(nums, nums_temp, nums_temp_1)


# 队列练习
# tasks = []
# while True:
#     input_task = input('please input do or a task:')
#     if input_task != 'do':
#         tasks.append(input_task)
#     else:
#         if len(tasks) == 0:
#             print('无任务')
#             break
#         else:
#             print('做', tasks.pop(0))

# 获取两个数组中的相同的，放到第三个数组中
# nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
# nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]
# nums_new = []
# for i in nums_1:
#     if i in nums_2 and i not in nums_new:
#         nums_new.append(i)
# print(nums_new)

users = []
tpl = '|{:>10}|{:>5}|{:>15}|'
header = tpl.format('name', 'age', 'tel')

while True:
    action = input('Please input a command:\n(find/list/add/delete/update/exit):')
    action = action.strip()
    if action == 'add':
        useradd = input('请按格式输入信息  用户名:年龄:联系方式  ').strip()
        name = useradd.split(':')[0]
        age = useradd.split(':')[1]
        tel = useradd.split(':')[2]
        user_tuple = (name, age, tel)
        is_exists = False
        for user in users:
            if user[0] == user_tuple:
                is_exists = True
                print('用户存在！')
                break
        if not is_exists:
            users.append(user_tuple)
            print('添加成功')
    elif action == 'delete':
        name = input('请输入删除的用户：')
        is_exists = False
        for user in users:
            if user[0] == name:
                is_exists = True
                users.remove(user)
        if not is_exists:
            print('用户不存在')
    elif action == 'update':
        name = input('请输入名字：')
        age = input('请输入年龄：')
        tel = input('请输入手机号：')
        user_tuple = (name, age, tel)
        is_exists = False
        for user in users:
            if user[0] == user_tuple[0]:
                is_exists = True
                users.remove(user)
                users.append(user_tuple)
                print('更新成功')
                break
        if not is_exists:
            print('没有这个用户')
    elif action == 'find':
        name = input('请输入查找的用户名：')
        is_exists = False
        for user in users:
            if user[0] == name:
                print(header)
                print(tpl.format(user[0], user[1], user[2]))
                is_exists = True
                break
        if not is_exists:
            print('用户不存在')
    elif action == 'list':
        print(header)
        for user in users:
            print(tpl.format(user[0], user[1], user[2]))
    elif action == 'exit':
        print('exit')
        break
    else:
        print('输入错误')

