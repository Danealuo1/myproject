# get请求和post请求获取参数

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('get_post.html')

@app.route('/search/')
def search():
    # 怎么在search视图函数中获取get传递过来的参数呢？
    # flask框架中提供请求上下文的request，其中有用于GET请求获取参数的
    # args方法和用于post请求获取参数的form方法
    # args只获取地址栏中参数，不分get请求方式还是post请求方式
    print(request.args.get('q'))   # 获取某一个参数
    print(request.args)     # 获取多个参数，是一个字典

    return 'search'

# 默认的视图函数，只能采用get请求
#
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('get_post.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('姓名是：%s，密码是: %s' % (username, password))
        return 'post请求'


if __name__ == '__main__':
    app.run(debug=True)

"""
get和post请求获取参数：
1.get请求是通过 flask.request.args 来获取
2.post请求是通过 flask.request.form 来获取
3.post请求在模板中要注意几点：
    input标签中，要写name来标识这个value的key，方便后台获取
    在写form表单的时候，要指定 method=post，并且要指定action=login

示例代码：

<form action="{{ url_for('login') }}" method="post">
    <table>
        <tbody>
            <tr>
                <td>用户名：</td>
                <td><input type="text" placeholder="请输入用户名" name="username"></td>
            </tr>
            <tr>
                <td>密码：</td>
                <td><input type="text" placeholder="请输入密码" name="password"></td>
            </tr>
            <tr>
                <td></td>
                <td><input type="submit" value="登录"></td>
            </tr>
        </tbody>
    </table>
</form>

"""