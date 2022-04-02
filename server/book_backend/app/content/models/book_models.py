from app.database import Base
from book_backend.app.users.models.user_models import Authors
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    authors = Column(ForeignKey(Authors.id))
    description = Column(String(500))
    categories = relationship("Category", secondary="BooksCategory", backref="Books")

    def __str__(self) -> str:
        return self.name


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    book = relationship("Books", secondary="BooksCategory", backref="Category")
    name = Column(String(30))
    description = Column(String(255))

    def __str__(self) -> str:
        return self.name


class BooksCategory(Base):
    __tablename__ = "BooksCategory"

    id = Column(Integer, primary_key=True, index=True)
    books_id = Column(Integer, ForeignKey("Books.id"))
    category_id = Column(Integer, ForeignKey("Category.id"))
