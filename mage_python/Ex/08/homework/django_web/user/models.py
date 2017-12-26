from django.db import models

import MySQLdb
from MySQLdb.cursors import DictCursor

HOST = '192.168.6.15'
PORT = 3306
DB = 'django_web'
USER = 'root'
PASSWD = 'iscs@2016up'
CHARSET = 'utf8'

SQL_USER_LIST = 'select username, age, tel from user;'
SQL_USER_LOGIN = 'select username, age, tel from user where username=%s and password=%s;'
SQL_USER_DELETE = 'delete from user where username=%s;'
SQL_USER_MODIFY = 'update user set password=%s, tel=%s, age=%s where username=%s;'
SQL_USER_ADD = 'insert into user(username, password, tel, age) values(%s, %s, %s, %s);'

# Create your models here.

def get_users():
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LIST)
    user_list = cur.fetchall()
    cur.close()
    conn.close()
    return user_list

def validate_login(username, password):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LOGIN, (username, password))
    rt = cur.fetchone()
    cur.close()
    conn.close()
    if rt is None:
        return False, '用户认证失败'
    else:
        return True, '用户认证成功'

def delete_user(username):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_DELETE, (username,))
    conn.commit()
    cur.close()
    conn.close()

def validate_modify(username, password, tel, age):
    if username and age and tel and password:
        if len(password) < 8:
            return False, '密码长度必须大于等于8个字符'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        return True, '验证成功'
    else:
        return False, '输入不能为空'

def list_user(users, field='username'):
    user_list = list(users)
    return sorted(user_list, key=lambda x: x.get(field))

def modify_user(username, password, tel, age):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_MODIFY, (password, tel, age, username))
    conn.commit()
    cur.close()
    conn.close()

def validate_add(username, password, tel, age):
    if username and age and tel and password:
        users = get_users()
        for user in users:
            if user['username'] == username:
                return False, '用户名重复'
        if len(password) < 8:
            return False, '密码长度必须大于等于8个字符'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        return True, '验证成功'
    else:
        return False, '输入不能为空'

def add_user(username, password, tel, age):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_ADD, (username, password, tel, age))
    conn.commit()
    cur.close()
    conn.close()