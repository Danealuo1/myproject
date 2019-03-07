# 重定向和页面跳转
from flask import Flask,redirect,url_for

app = Flask(__name__)

# 重定向方法一
# @app.route('/')
# def index():
#     # redirect方法可以重定向
#     return redirect('/login/')
#     return '这是首页'

# 重定向方法二
# 可以这么写
# @app.route('/')
# def index():
#     login_url = url_for('login')
#     return redirect(login_url)
#     return "这是首页"
#
# @app.route('/login/')
# def login():
#     return "这是登录页面hhhllll"
#
# @app.route('/question/<is_login>/')
# def question(is_login):
#     if is_login == '1':
#         return "这是发布问答页面"
#     else:
#         return redirect(url_for('login'))

### 页面跳转和重定向
"""
用处：在用户访问一些需要登录的页面的时候，如果用户没有登录，那么可以让
她重定向到登录页面



"""
# if __name__=='__main__':
#     app.run(debug=True)