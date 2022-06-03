from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = 'master'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String)


class Detail(Base):
    __tablename__ = 'detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Integer, ForeignKey('master.user'))
    zip_code = Column(String)
    city = Column(String)
