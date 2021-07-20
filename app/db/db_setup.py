from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ARRAY,
    DateTime,
    REAL,
	Float,
   	ForeignKey
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os


engine = create_engine(os.environ.get('PSQL_DB'))

Base = declarative_base()


class Meduza(Base):
    __tablename__ = 'meduza'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    source = Column(String)
    link = Column(String, unique=True)
    title = Column(String)
    text = Column(String)
    locs = Column(ARRAY(String))
    pers = Column(ARRAY(String))
    orgs = Column(ARRAY(String))
    x = Column(REAL)
    y = Column(REAL)
    highlights = Column(String)

class Lenta(Base):
    __tablename__ = "lenta"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    link = Column(String, unique=True)
    title = Column(String)
    text = Column(String)
    locs = Column(ARRAY(String))
    pers = Column(ARRAY(String))
    orgs = Column(ARRAY(String))
    x = Column(REAL)
    y = Column(REAL)
    highlights = Column(String)


class Interfax(Base):
    __tablename__ = "interfax"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    link = Column(String, unique=True)
    title = Column(String)
    text = Column(String)
    locs = Column(ARRAY(String))
    pers = Column(ARRAY(String))
    orgs = Column(ARRAY(String))
    rubric = Column(ARRAY(String))
    x = Column(REAL)
    y = Column(REAL)
    highlights = Column(String)


class AllNews(Base):
    __tablename__ = 'all_news'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    rubric = Column(ARRAY(String))
    link = Column(String, unique=True)
    title = Column(String)
    text = Column(String)
    locs = Column(ARRAY(String))
    pers = Column(ARRAY(String))
    orgs = Column(ARRAY(String))
    x = Column(Float)
    y = Column(Float)
    highlights = Column(String)
    tokens = Column(ARRAY(String))
    recommendations = relationship("Recommendation", backref="about")


class Recommendation(Base):
    __tablename__ = 'recommendation'
    id = Column(Integer, primary_key=True)
    quote = Column(String)
    bos = Column(Float)
    bos_positive = Column(Float)
    bos_negative = Column(Float)
    datetime = Column(DateTime)
    news_id = Column(Integer, ForeignKey("all_news.id"))


class Ticker(Base):
	__tablename__ = 'tickers'
	id = Column(Integer, primary_key=True)
	sec_id = Column(String)
	shortname = Column(String)
	bos = Column(Float)


async_engine = create_async_engine(
    os.environ.get('PSQL_DB'), echo=True,
)
async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)




#Base.metadata.bind = engine
#Base.metadata.create_all(engine)

#DBSession = sessionmaker(bind=engine)
#session = DBSession()
