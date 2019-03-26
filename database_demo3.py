"""
SQLAlchemy外键约束  一对多
"""

# 导入
from flask import Flask
from sqlalchemy import Column, String,Integer,Text,ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# 创建对象的基类（创建模型对象的基类）
Base = declarative_base()

# 定义表的对象
# 表的名字  表的结构
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    # 以下是重点，怎么添加外键
    author_id = Column(Integer, ForeignKey('user.id'))

    # 通过relationship方法来#################  第二种方法
    # 注意 User这里写的东西要跟想要关联到的模型的名字保持一致
    author = relationship('User', backref='articles')

# 初始化数据库连接
# 注意 create_engine()方法用来初始化数据库连接
# sqlAlchemy用以下
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/db_demo3",encoding='utf-8',echo=True)

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()

# 数据库生成表
Base.metadata.create_all(engine)




# @app.route('/')
# def index():
    # 首先添加一篇文章，因为文章必须依赖用户而存在，先添加一个用户
    # 创建新的user对象
    # user1 = User(username='xiaohong')
    #     # # 添加到session
    #     # session.add(user1)
    #     # # 提交即保存到数据库
    #     # session.commit()

    # article1 = Article(title='aaa', content='bbb', author_id=1)
    # session.add(article1)
    # session.commit()

    # 找文章为aaa的作者
    # 查询找到 标题为 aaa 的记录
    # 重点是这里的查询语法
    # article = session.query(Article).filter(Article.title == 'aaa').first()
    #
    # author_id = article.author_id
    # # 查询到 id为author_id里的记录
    # user = session.query(User).filter(User.id == author_id).first()
    #
    # print(user.username)

#################  创建1篇文章  ########
    # article = Article(title='aaa', content='bbb')
    #     # # 下面这种用法再体会一下
    #     # article.author = session.query(User).filter(User.id == 1).first()
    #     # # 添加到事物中
    #     # session.add(article)
    #     # # 事物的提交
    #     # session.commit()

    # article = session.query(Article).filter(Article.title == 'aaa').first()
    # print('username: %s' % article.author.username)

    # 再添加一条数据
    # article = Article(title='111', content='222',author_id=1)
    # session.add(article)
    # session.commit()
    #
    # # 关闭session
    # session.close()

    # 找到文章标题为aaa的这个作者
    # article = session.query(Article).filter(Article.title =='aaa').first()
    # print('username: %s' % article.author.username)

    # 现在要找到 xiaohong 写过的所有文章，目前article表中只有一条数据，再创建一条数据
    # article = Article(title='today', content='happy mood',author_id = 1)
    # session.add(article)
    # session.commit()

    # user = session.query(User).filter(User.username == 'xiaohong').first()
    #
    # result = user.articles
    # for article in result:
    #     print('-' * 10)
    #     print(article.title)



    # return 'index1'


# if __name__ == '__main__':
#     app.run(debug=True)


"""
1.外键

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    # 以下是重点，怎么添加外键
    author_id = Column(Integer, ForeignKey('user.id'))

    # 通过relationship方法来#################  第二种方法
    # 注意 User这里写的东西要跟想要关联到的模型的名字保持一致
    author = relationship('User', backref='articles')

2.author = relationship('User', backref='articles')的解释：
1）给Article这个模型添加一个author属性，可以访问这篇文章的作者的数据，
像访问普通模型一样
2）backref是定义反向引用，可以通过user.articles这个模型访问这个模型所写的所有文章


"""