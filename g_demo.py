# 第39课时  线程隔离的g对象,g是global的简写

from flask import Flask, g, render_template, request
from utils import login_log

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('g_demo.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        if username == 'luo' and password == '123456':
            # 就认为当前这个用户的用户名和密码正确
            # 用g对象绑定一些用户自定义的东西,g对象在项目的所有地方都可以使用
            g.username = 'luo'
            login_log()
            return '恭喜！登录成功！'
        else:
            return '您的用户名或密码错误！'



if __name__ == '__main__':
    app.run(debug=True)


"""
保存全局变量的g属性：
g： global
1. g对象是专门用来保存用户的数据的
2. g对象在一次请求中的所有代码的地方，都是可以使用的

"""