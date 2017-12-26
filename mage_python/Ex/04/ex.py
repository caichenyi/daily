# encoding: utf-8
# Author: Cai Chenyi

# path = 'kk.txt'

# fhandler = open(path)
#
# while True:
#     cxt = fhandler.readline()
#     if cxt == '':
#         break
#     print(cxt)
#
# fhandler.close()


# fhandler = open(path)
#
# cxt = fhandler.readlines()
# print(cxt)
#
# fhandler.close()


# fhandler = open(path)
# for line in fhandler:
#     print('[', line, ']')
# fhandler.close()


# fhandler = open(path, 'rb')
# print(fhandler.read(5).decode())
#
# fhandler.close()


# fhandler = open('user2.txt', 'wt')
# fhandler.write('abcdef')
# fhandler.write('123456\n')
# fhandler.write('123456')
# fhandler.close()

# fhandler = open('user2.txt', 'wt')
# fhandler.write('abcdef')
# fhandler.write('123456\n')
# fhandler.write('123456')
# fhandler.close()

# fhandler = open('user2.txt', 'wt')
# fhandler.write('abcdef')
# fhandler.writelines(['123', 'abc', '456'])
# fhandler.flush()
# fhandler.write('123456\n')
# fhandler.close()


# src = 'src.txt'
# dst = 'dst.txt'

# fhandler = open(src, 'rb')
# cxt = fhandler.read()
# fhandler.close()
#
# fhandler = open(dst, 'wb')
# fhandler.write(cxt)
# fhandler.close()


# src = 'src.txt'
# dst = 'dst.txt'
# BUFFERSIZE = 1024
# src_fhandler = open(src, 'rb')
# dst_fhandler = open(dst, 'wb')
# while True:
#     cxt = src_fhandler.read(BUFFERSIZE)
#     if cxt == b'':
#         break
#     dst_fhandler.write(cxt)
#
# src_fhandler.close()
# dst_fhandler.close()


# fhandler = open('user4.txt', 'xt')
# fhandler.write('123')
#
# fhandler.close()


# fhandler = open('user4.txt', 'at')
# fhandler.write('xyz')
# fhandler.close()

# fhandler = open('user2.txt', 'rt')
# print(fhandler.tell())
# print(fhandler.read(2))
# print(fhandler.tell())
# fhandler.close()


# fhandle = open('user2.txt', 'rt')
# print(fhandle.read())
# print(fhandle.seek(0, 0))
# print(fhandle.read())
# print(fhandle.seek(3, 0))
# print(fhandle.read())


# fhandle = open('user2.txt', 'rb')
# print(fhandle.tell())
# print(fhandle.seek(-3, 2))
# print(fhandle.read())
# print(fhandle.read())
# print(fhandle.tell())


# import time
# src = '/tmp/log.txt'
# fhandler = open(src, 'rb')
# fhandler.seek(0, 2)
# while True:
#     line = fhandler.readline()
#     if line != '':
#         print(line.decode(), end='')
#     else:
#         time.sleep(3)

# fhandle = open('n.txt', 'a+')
# print(fhandle.read())
# fhandle.write('123456789')
# print(fhandle.read())
# fhandle.seek(0)
# print(fhandle.read())
# fhandle.close()

nums = [13, 8, 1, 2, 7, 3, 11, 10, 0]
for i in range(0, len(nums) - 1):
    for j in range(i + 1, 0, -1):
        print('22')
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            print(nums)
    print('==================')
print(nums)