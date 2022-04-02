import sqlalchemy
from book_backend.app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    metadata = sqlalchemy.MetaData()

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
