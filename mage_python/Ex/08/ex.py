# encoding: utf-8
# Author: Cai Chenyi

# import MySQLdb
#
# # 获取连接
# conn = MySQLdb.connect(host='192.168.6.15', port=3306, user='root', passwd='iscs@2016up', db='caichenyi', charset='utf8')
# # 获取游标
# cursor = conn.cursor()
# # 获取数据
# cursor.execute('select * from message')
# # 读取所有信息（fetchone()读取一条信息）
# cursor.fetchall()
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()


# conn = MySQLdb.connect(host='192.168.6.15', port=3306, user='root', passwd='iscs@2016up', db='caichenyi', charset='utf8')
# cursor = conn.cursor()
# cursor.execute('insert into message values(username, title, content, publish_date) values("tom", "abc", "abc", now()')
# conn.commit()
# cursor.close()
# conn.close


# conn = MySQLdb.connect(host='192.168.6.15', port=3306, user='root', passwd='iscs@2016up', db='caichenyi', charset='utf8')
# cursor = conn.cursor()
# cursor.execute('update message set username = "ccy" where username = "11111"')
# conn.commit()
# cursor.close()
# conn.close()


# conn = MySQLdb.connect(host='192.168.6.15', port=3306, user='root', passwd='iscs@2016up', db='caichenyi', charset='utf8')
# cursor = conn.cursor()
# cursor.execute('delete from message where username = "kk"')
# conn.commit()
# cursor.close()
# conn.close()


# conn = MySQLdb.connect(host='192.168.6.15', port=3306, user='root', passwd='iscs@2016up', db='caichenyi', charset='utf8')
# cursor = conn.cursor()
# cursor.execute('insert into message(username, title, content, publish_date) values(%s, %s, %s, %s);', ('a', 'b', 'c', '2017-05-20 15:46:00'))
# conn.commit()
# cursor.close()
# conn.close()

# import traceback
#
# print('before')
#
# try:
#     1/1
# except BaseException as e:
#     print(e)
#
# print('after')
#
#
# def test1():
#     print('test1 before')
#     try:
#         l = []
#         l[1]
#     except BaseException as e:
#         print(e)
#         return
#     print('test after')
#
# def test2():
#     print('test2 before')
#     try:
#         d = {}
#         d['kk']
#     except BaseException as e:
#         print(e)
#         print(traceback.format_exc())
#         return
#     finally:
#         print('test2 after')
#
#
# test1()
# test2()


users = ({'id': 1, 'username': 'caicy1', 'age': 55, 'tel': '130'}, {'id': 2, 'username': 'caicy2', 'age': 26, 'tel': '15268889158'}, {'id': 3, 'username': 'caicy3', 'age': 26, 'tel': '15268889158'}, {'id': 4, 'username': 'caicy4', 'age': 66, 'tel': '147852'}, {'id': 6, 'username': 'caicy5', 'age': 77, 'tel': '15268889158'})
_id = '1'

for user in users:
    if user['id'] == int(_id):
        print('pass')
        print(user['id'])
        print(_id + '\n')
    else:
        print('fail')
        print(user['id'])
        print(_id + '\n')
