# utils模块写一些工具类的函数

from flask import g

def login_log():
    print('当前登录的用户是： %s' % g.username)

