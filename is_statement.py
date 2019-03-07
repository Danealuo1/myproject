# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/<is_login>/')
# def index(is_login):
#     if is_login == "1":
#         user = {
#             'username': '黄勇',
#             'age': 18
#         }
#         return render_template('index1.html',user=user)
#     else:
#         return render_template('index1.html')
#
# if __name__=='__main__':
#     app.run(debug=True)

"""
if判断：
1.语法：
{% if xxx %}
{% else %}
{% endif %}
2.if的使用，可以和python中相差无几

"""
