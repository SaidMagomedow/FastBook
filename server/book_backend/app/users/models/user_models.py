from book_backend.app.database import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String(8))

    def __str__(self) -> str:
        return self.username


class Authors(User):
    __tablename__ = "author"

    first_name = Column(String(15))
    middle_name = Column(String(15))
    last_name = Column(String(15))
    nickname = Column(String(15), unique=True)
