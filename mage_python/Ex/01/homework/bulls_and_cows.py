# encoding: utf-8
# Author: Cai Chenyi

# 猜数字
import random
random_num = random.randint(0, 100)
print(random_num)
loop = 5
min = 0
max = 100
for i in range(1, loop + 1):
    num = int(input('请输入第%d次猜测[%d~%d]：' % (i, min, max)))
    if num == random_num:
        print('恭喜猜对了，游戏结束')
        break
    elif num < random_num:
        print('你猜的太小了')
        min = num + 1
    elif num > random_num:
        print('你猜的太大了')
        max = num - 1
if num != random_num:
    print('%d次机会用完，游戏失败' % loop)