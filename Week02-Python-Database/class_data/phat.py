from Database import data_base  # TODO: em bi bao do khi import nhung van chay dc
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

testuser = User(id = 6,
                name = 'Phat Dep Trai',
                address = 'Ha Noi',
                birth = date(1993, 11, 5), #todo : em muon insert vao ma cu bi loi int
                phone = '0764222993',
                update_at = datetime.utcnow()
                )
dataq.add(testuser)
dataq.commit()

#--Update User

x = dataq.query(User).get(2)
x.address = 'Hoang Sa'
x.update_at = datetime.now()
dataq.commit()

#-- delete User
x = dataq.query(User).get(1)
dataq.delete(x)
dataq.commit()