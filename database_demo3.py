"""
SQLAlchemy外键约束
"""

# 导入
from flask import Flask
import config
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义user对象



# 初始化数据库连接
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/db_demo2",encoding='utf-8',echo=True)




app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main':
    app.run(debug=True)