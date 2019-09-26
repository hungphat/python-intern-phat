from Database import data_base  # TODO: you should set Week02 as a Source root
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

#TODO perform CRUD operation and comment in each case below this line
for test in dataq.query(User):
    a = [test.name]
    print(a)

#TODO it would be look better when queuing the equal "=" in vertical
testuser = User(id = 6,
                name = 'Phat Dep Trai',
                address = 'Ha Noi',
                birth = date(1993, 11, 5), #TODO : using String in this case e.g '19931105'
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
x = dataq.query(User).get(1) #TODO should name a meaning variable instead of meaningless one
dataq.delete(x)
dataq.commit()
#TODO should add one empty line at the end of the script