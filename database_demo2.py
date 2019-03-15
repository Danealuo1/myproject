"""
数据库的增删改查

"""

# from flask import Flask
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column,Integer,String,Text
# from sqlalchemy.orm import sessionmaker
#
# app = Flask(__name__)
#
# # 生成ORM基类
# Base = declarative_base()
#
# # echo=True 把所有的信息都打印出来
# # create_engine()用来初始化数据库连接，SQLAlchemy用一个字符串表示连接信息：
# # 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
# engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/db_demo2",encoding='utf-8',echo=True)
#


# 设计article表
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
# )

# 继承父类  Base
# 创建模型对象
# class Article(Base):
#     # 给表格取名
#     __tablename__= 'article'
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     title = Column(String(100),nullable=False)
#     content = Column(Text,nullable=False)
#
# # 定义初始化数据库函数
# Base.metadata.create_all(engine)
#
# # 创建DBSession类型，可视为当前数据库连接
# DBSession = sessionmaker(bind=engine)
#
# # 创建Session对象
# session = DBSession()
#
#
# @app.route('/')
# def index():
    # 往数据库中增加一条数据
    # 创建article对象
    # article1 = Article(title='aaa',content='bbb')
    # # 提交到session
    # session.add(article1)
    # # 提交即保存到数据库
    # session.commit()
    # # 关闭session
    # session.close()


    # 往数据库中增加多条数据
    # article1 = Article(title='baidu',content='www.baidu.com')
    # article2 = Article(title='xixi',content='vvvvb')
    # session.add_all([article1,article2])   # 注意这里的语法，提交多条数据
    # session.commit()
    # session.close()

    # 查数据库中的数据
    # 创建Query查询，filter是where的条件，最后调用one（）返回一行，调用first（）返回第一行
    # 如果调用all（）则返回所有行
    # content_query = session.query(Article).filter(Article.title=='aaa').one()
    # print('content:',content_query.content)
    #
    # # 关闭session
    # session.close()

    # 改数据库中的数据
    # 1.先把要更改的数据查找出来
    # article1 = session.query(Article).filter(Article.title=='aaa').first()
    # # 2.把这条数据需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3.做事物的提交
    # session.commit()
    # # 关闭session
    # session.close()

    # 删
    # 1.把需要删除的数据查找出来
    # article1 = session.query(Article).filter(Article.title=='baidu').first()
    # # 2.把这条数据删除掉
    # session.delete(article1)
    #
    # # 3.做事务的提交
    # session.commit()
    # session.close()
    #
    # return '哼哼vv哈哈'

# if __name__=='__main__':
#     app.run(debug=True)


"""
SQLAlchemy数据增删改查：
增：
 # 创建article对象
    article1 = Article(title='aaa',content='bbb')
    # 提交到session
    session.add(article1)
    # 提交即保存到数据库
    session.commit()
    # 关闭session
    session.close()

查：
# 查数据库中的数据
    # 创建Query查询，filter是where的条件，最后调用one（）返回一行，
    # 如果调用all（）则返回所有行
    content_query = session.query(Article).filter(Article.title=='aaa').one()
    print('content:',content_query.content)
    
    # 关闭session
    session.close()

改：
# 改数据库中的数据
    # 1.先把要更改的数据查找出来
    # article1 = session.query(Article).filter(Article.title=='aaa').first()
    # # 2.把这条数据需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3.做事物的提交
    # session.commit()
    # # 关闭session
    # session.close()

 删
    # 1.把需要删除的数据查找出来
    article1 = session.query(Article).filter(Article.title=='baidu').first()
    # 2.把这条数据删除掉
    session.delete(article1)

    # 3.做事务的提交
    session.commit()
    session.close()


"""

