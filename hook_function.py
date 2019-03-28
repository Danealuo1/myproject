# 第40课时，before_requests钩子函数   钩子（hook）
# 第41课时，上下文处理器钩子函数
from flask import Flask, render_template, request, session, redirect, url_for, g
import os

app = Flask(__name__)
# 给session设置 secret_key
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET','POST'])
def hello_world():

    if request.method == 'GET':
        return render_template('hook_function.html')
    else:
        pass
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'luo' and password == '123456':

            # 在这里设置session
            session['username'] = 'luo'
            return '登录成功'
        else:
            return '用户名或密码错误'

# before_request: 在请求之前执行的
# before_request是在试图函数执行之前执行的
# before_request这个函数只是一个装饰器，可以把需要设置为钩子函数
# 的代码放到试图函数中

@app.before_request
def my_before_request():
    print('hhh')
    # 把session.get('username')绑定到g对象上去
    if session.get('username'):
        g.username = session.get('username')

# 上下文处理器也是一个装饰器
@app.context_processor
def my_context_processor():
    # 判断用户是否登录
    # username = session.get('username')
    # if username:
    #     # 如果有，直接把username传给模板，怎么传呢？直接返回一个字典就可以
    #
    #     # 只要在上下文处理器中返回了字典，在所有模板中都能用
    #     return {'username': username}

    return {'username': 'luo'}




@app.route('/edit/')
def edit():
    # if session.get('username'):
    # if hasattr(g, 'username'):
    #     return '修改成功'
    # else:
    #     return redirect(url_for('hello_world'))

    return render_template('context_processor.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
context_processor:
1.上下文处理器应该返回一个字典。字典中的key会被模板中当成
变量来渲染
2.上下文处理器中返回的字典，在所有页面中都是可用的



"""