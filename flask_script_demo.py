# # flask_script讲解
# # Flask-Script的作用是可以通过命令行的形式来操作Flask。
# # 如可以通过命令行跑一个开发版本的服务器、设置数据，定时任务等
# # 进入到虚拟环境中安装 命令： pip install flask-script
#
#
# from flask import Flask
#
# # app是flask的实例，接收包或模块的名字作为参数
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'hello world12!'
#
# if __name__ == '__main__':
#     app.run(debug=True)
