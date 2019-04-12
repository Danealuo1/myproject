# url链接和加载静态文件
# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('url_link.html')
#
#
# @app.route('/login/')
# def login():
#     return render_template('login_url_link.html')
#
# if __name__=='__main__':
#     app.run(debug=True)


"""
url链接： 使用url_for(视图函数名称)可以反转成url
加载静态文件：
1.语法： url_for('static',filename='路径')
url_for(文件夹的名字, filename='文件所在的路径')

**2.静态文件，flask会从static文件夹中开始寻找，所以不需要再写static这个
路径了（可以加载css文件、js文件、image文件）  

例如：
加载css文件
<link rel="stylesheet" href="{{url_for('static',filename='css/index.css')}}">
加载js文件
<script src="{{url_for('static',filename='js/index.js')}}"></script>
加载图片文件
<img src="{{url_for('static',filename='images/cat.jpg')}}" alt="">
"""

