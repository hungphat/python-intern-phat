from Database import data_base
from datetime import datetime,date
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

dt   = datetime.now()
Base = declarative_base()
datasess = data_base.session

class User(Base):
    __tablename__ = 'customers'
    id            = Column(Integer,    primary_key=True)
    name          = Column(String)
    birth         = Column(Date)
    address       = Column(String)
    phone         = Column(String)
    update_at     = Column(DateTime)

    def __init__(self,  id,  name,   birth,  address,    phone,    update_at):
        self.id      = id
        self.name    = name
        self.birth   = birth
        self.address = address
        self.phone   = phone
        self.update_at  = update_at

#CRUD alchemy
dataquery = datasess.query(User)
# #--Create
#
# adduser = User(id         =  7,
#                 name      = 'Alexander',
#                 address   = 'Ha Noi',
#                 birth     = date(1967, 5, 9),
#                 phone     = '07642212334',
#                 update_at = datetime.utcnow())
# datasess.add(adduser)
# datasess.commit()
#
#
#--Read

for read in dataquery:
    a = f'{read.id}   {read.name}  {read.birth} {read.address}   {read.phone}'
    print(a)


# #--Update User
#
# x = dataquery.get(3)
# x.address = 'Hoang Sa'
# x.update_at = datetime.now()
# datasess.commit()
#
# #-- Delete User
# x = dataquery.get(4)
# datasess.delete(x)
# datasess.commit()
