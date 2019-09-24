from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
conection_string = 'postgresql://{user}:{pwd}@{host}:{port}/{db}'.format(
                    user = 'admin',
                    pwd  = 'admin',
                    host = 'localhost',
                    port = '5432',
                    db   = 'customerdata'
)

engine = create_engine(f'{conection_string}')

class User(Base):
    __tablename__ = 'customers'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    birth = Column(Date)
    address = Column(String)
    phone = Column(String)


Session = sessionmaker(bind=engine)
session = Session()

for data in session.query(User):
    print([data.name])