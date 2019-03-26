from exts import Base
from sqlalchemy import Column, String,Integer,Text,ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String(100), nullable=False)


