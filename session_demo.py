
# 在flask中操作session

from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
# 注意 secret_key必须是24个字符的字符串
# os.urandom(n) 返回n个byte那么长的字符串，很适合用于加密
app.config['SECRET_KEY'] = os.urandom(24)
# 自定义设置session的过期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 添加数据到session中
# 操作session的时候，跟操作字典是一样的
# 需要设置 SECRET_KEY
@app.route('/')
def hello_world():
    session['username'] = 'luo'
    # 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束

    # 设置session的过期时间,如果设置session的permanent属性为True，那么过期
    # 时间为31天
    session.permanent = True
    return 'hello world2222'

# 获取session
@app.route('/get/')
def get():
    return session.get('username')

# 删除session
@app.route('/delete/')
def delete():
    print(session.get('username'))
    # 删除session中的数据
    session.pop('username')
    print(session.get('username'))
    return 'success'

# 清空session
@app.route('/clear/')
def clear():
    print(session.get('username'))
    # 删除session中的所有数据
    session.clear()
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)


"""
操作session：
使用session需要从flask中导入session，以后所有和session相关的操作都是通过
这个变量来的
使用session需要设置SECRET_KEY,用来作为加密用的。并且这个SECRET_KEY如孤傲每次服务器
启动后都变化的话，那么之前的session就不能再通过当前这个SECRET_KEY进行解密了
操作session的时候，跟擦做字典是一样的
添加session： session['username']
删除session： session.pop('username') 
清除所有session： session.clear()
获取session： session.get('username')

设置session的过期时间：
如果没有指定session的过期时间，默认是浏览器关闭后就自动结束
如果设置了session的permanent属性为True，那么过期时间是31天
如果通过给app.config设置PERMANENT_SESSION_LIFETIME来更改过期时间，
这个值得数据类型是 datatime.timedelay类型

"""

