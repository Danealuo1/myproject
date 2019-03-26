# 第31讲，分开模型和解决循环引用   还有问题
# models.py 存放模型
# exts.py 写第三方的东西，如数据库

from flask import Flask
# 导入数据库
from exts import Base
from sqlalchemy import create_engine
from models import Article
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


# 初始化数据库连接
# 注意 create_engine()方法用来初始化数据库连接
# sqlAlchemy用以下
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/db_demo5",encoding='utf-8',echo=True)

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 数据库生成表
Base.metadata.create_all(engine)



@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)