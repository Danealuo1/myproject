# 过滤器的使用

# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     contents = [
#         {
#             'user':'小红',
#             'comment':'啊哈哈哈'
#         },
#         {
#             'user':'小明',
#             'comment':'嘻嘻嘻'
#         }
#     ]
#     return render_template('index_filter.html',contents=contents)
# if __name__=='__main__':
#     app.run(debug=True)

"""
过滤器：
1.过滤器可以处理变量，把原始变量经过处理后再展示出来。作用的对象是变量
语法：
{{ avatar | default('xxx')}}

2. default过滤器： 如果当变量不存在，这时候可以指定默认值
3. length过滤器：求出列表或者字符串或者字典或者元组的长度



"""