from Database import data_base
from datetime import datetime,date
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

dt   = datetime.now()
Base = declarative_base()
dataq = data_base.session

class User(Base):
    __tablename__ = 'customers'
    id        = Column(Integer,    primary_key=True)
    name      = Column(String)
    birth     = Column(Date)
    address   = Column(String)
    phone     = Column(String)
    update_at = Column(DateTime)


for test in dataq.query(User):
    a = [test.name]
    print(a)