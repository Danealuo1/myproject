# for循环遍历
# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# # for循环遍历字典
# @app.route('/')
# def index():
#     # user ={
#     #     'username': '黄勇',
#     #     'age':18
#     # }
#     websites = ['www.baidu.com', 'www.google.com']
#     return render_template('index2.html',websites=websites)
#
# if __name__=='__main__':
#     app.run(debug=True)


# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     books = [
#         {
#             'name':'红楼梦',
#             'author':'曹雪芹',
#             'price':111
#         },
#         {
#             'name':'西游记',
#             'author':'吴承恩',
#             'price':200
#         },
#         {
#             'name': '三国演义',
#             'author': '罗贯中',
#             'price':150
#         },
#         {
#             'name': '水浒传',
#             'author': '施耐庵',
#             'price':160
#         }
#         ]
#     return render_template('index2.html',books=books)
#
#
#
# if __name__=='__main__':
#     app.run(debug=True)




"""
for循环遍历列表和字典：
1.字典的遍历
语法和python一样，可以使用items() keys() values()
iteritems()  iterkeys()
itervalues()

{% for k,v in user.items() %}
        <p>{{k}}:{{v}}</p>
    {% endfor %}

2.列表的遍历
语法和python一样
{% for website in websites %}
        <p>{{website}}</p>
    {% endfor %}



"""