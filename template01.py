### 用falsk渲染模板。传递参数
# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     class Person(object):
#         name = '罗大仙'
#         age = 18
#
#     p = Person()
#
#     # 有多个参数需要渲染时，可用一个字典来保存参数
#     context = {
#         'username':'最爱喝苦咖啡',
#         'gender':'男',
#         'age':20,
#         'person': p,
#         'websites':{
#             'baidu':'www.baidu.com',
#             'google':'www.google.com'
#         }
#
#     }
#     # 用     **变量名  引用
#     return render_template('index.html',**context)
#
#
#
# if __name__=='__main__':
#     app.run(debug=True)

"""
1.如何渲染模板：
模板放在‘templates’文件夹下
在flask中导入render_template函数
在视图函数中，使用render_template函数渲染模板。注意：只需要填写模板的名字
，不需要填写templates这个文件夹的路径
2.模板传参：
如果只有一个或者少量参数，直接在render_template函数中添加关键字参数就可以了
如果有多个参数的时候，那么可以先把所有的参数放在字典中，然后在render_template
中使用两个星号，把字典转换成关键字参数传递进去。方便代码的管理和使用
3.在模板中如果要使用一个变量，语法是： {{params}}
4.访问模型中的属性或者是字典，可以通过{{params.property}}的形式

"""