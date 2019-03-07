# 继承和使用block

# from flask import Flask,render_template
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('extend_block.html')
#
# @app.route('/login/')
# def login():
#     return render_template('login.html')
#
# if __name__=='__main__':
#     app.run(debug=True)


"""
继承和block：
1. 继承作用和语法：
作用：可以把一些公共的代码放在父模板中，避免每个模板写
同样的代码
语法：
 {% extends 'base.html' %}
2. block实现：
作用： 可以让子模板实现一些自己的需求，父模板需要提前定义好
注意点：子模板中的代码必须放在block块中。
"""