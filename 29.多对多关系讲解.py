# ## 多对多关系讲解     用的数据库是db_demo4
#
# from flask import Flask
# from sqlalchemy import Column, String,Integer,Text,ForeignKey, create_engine, Table
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# app = Flask(__name__)
#
# # 创建对象的基类
# Base = declarative_base()
#
# # 初始化数据库连接
# engine = create_engine\
#     ("mysql+pymysql://root:root@127.0.0.1:3306/db_demo4", encoding='utf-8', echo=True)
#
# # 创建DBsession类型
# DBsession = sessionmaker(bind=engine)
#
# # 创建session对象
# session = DBsession()
#
# # 注意这里加上 Base.metadata  表继承的类，没加这个会报错
# # 中间表 表article和表tag并不知道有这个中间表的存在
# article_tag = Table('article_tag', Base.metadata,
#                     Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
#                     Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
#                     )
#
# # 创建文章的映射
# class Article(Base):
#     __tablename__ = 'article'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(100), nullable=False)
#     tag = relationship('Tag', secondary=article_tag)
#
# # 创建标签的映射
# class Tag(Base):
#     __tablename__ = 'tag'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     article = relationship('Article', secondary=article_tag)
#
#
# # 数据库生成表,创建表结构
# Base.metadata.create_all(engine)
#
# @app.route('/')
# def index():
#     # 创建两篇文章
#     # article1 = Article(title='aaa')
#     # article2 = Article(title='bbb')
#     #
#     # # 创建两个标签
#     # tag1 = Tag(name='xiaohong')
#     # tag2 = Tag(name='ming')
#     #
#     # # 通过 tag外键 article1文章 添加 tag1，tag2标签
#     # # article2文章 添加 tag1， tag2标签
#     # article1.tag = [tag1, tag2]
#     # article2.tag = [tag1, tag2]
#     # # 写入数据
#     # session.add(article1)
#     # session.add(article2)
#     # session.add(tag1)
#     # session.add(tag2)
#     #
#     # session.commit()
#
#     # 练习1： 拿到文章标题为 aaa的 文章的标签
#     article1 = session.query(Article).filter(Article.title == 'aaa').first()
#     tags = article1.tag
#     for tag in tags:
#         print(tag.name)
#
#
#     return 'index123'
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# """
# 多对多：
# 1）多对多的关系，要通过一个中间表来关联
# 2）中间表，不能通过class的方式实现，只能通过Table的方法实现
# 3）设置关联：
# tag = relationship('Tag', secondary=article_tag)
# article = relationship('Article', secondary=article_tag)
# 注意： 需要使用一个关键字 secondary=中间表来进行关联
#
# 添加数据：
#  # 创建两篇文章
#     # article1 = Article(title='aaa')
#     # article2 = Article(title='bbb')
#     #
#     # # 创建两个标签
#     # tag1 = Tag(name='xiaohong')
#     # tag2 = Tag(name='ming')
#     #
#     # # 通过 tag外键 article1文章 添加 tag1，tag2标签
#     # # article2文章 添加 tag1， tag2标签
#     # article1.tag = [tag1, tag2]
#     # article2.tag = [tag1, tag2]
#     # # 写入数据
#     # session.add(article1)
#     # session.add(article2)
#     # session.add(tag1)
#     # session.add(tag2)
#     #
#     # session.commit()
#
# 访问数据：
#
#  # 练习1： 拿到文章标题为 aaa的 文章的标签
# #     article1 = session.query(Article).filter(Article.title == 'aaa').first()
# #     tags = article1.tag
# #     for tag in tags:
# #         print(tag.name)
#
# """