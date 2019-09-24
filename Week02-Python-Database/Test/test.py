from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime,date

dt = datetime.now()
Base = declarative_base()
conectdata = 'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}'.format(
                    user = 'admin',
                    pwd  = 'admin',
                    host = 'localhost',
                    port = '5432',
                    db   = 'customerdata'
)

engine = create_engine(f'{conectdata}')


class User(Base):
    __tablename__ = 'customers'
    id = Column(Integer,    primary_key=True)
    name = Column(String)
    birth = Column(Date)
    address = Column(String)
    phone = Column(String)
    update_at =Column(DateTime)


Session = sessionmaker(bind=engine)
session = Session()


# for data in session.query(User):
#     print([data.id, data.name,  data.birth])

# for test in session.query(User):
#     a = [test.birth]
#     print(a)

testuser = User(id = 6,
                name = 'Phat Dep Trai',
                address = 'Sai Gon',
                birth = datetime.date(1993, 11, 5), #todo : em muon insert vao ma cu bi loi int
                phone = '0764222993',
                update_at = datetime.utcnow()
                )
session.add(testuser)
session.commit()