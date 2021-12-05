from re import U
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from .user_models import Authors

class Books(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    authors = Column(ForeignKey(Authors.id))
    description = Column(String(500))
    categories = relationship('Category', secondary='BooksCategory', backref='Books')

    def __str__(self) -> str:
        return self.name


class Category(Base):
    __tablename__ = 'category'
    book = relationship('Books', secondary='BooksCategory', backref='Category')
    name = Column(String(30))
    description = Column(String(500))
    
    def __str__(self) -> str:
        return self.name




class BooksCategory(Base):
    __tablename__ = 'BooksCategory'

    id = Column(Integer, primary_key=True, index=True)
    booksId = Column(Integer, ForeignKey('Books.id'))
    categorylId = Column(Integer, ForeignKey('Category.id'))