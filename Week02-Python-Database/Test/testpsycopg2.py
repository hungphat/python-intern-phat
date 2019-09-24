from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import psycopg2
import sys

con = psycopg2.connect(database = 'customerdata', user = 'admin', password = 'admin', host = 'localhost', port = '5432')
cur = con.cursor()
cur.execute("SELECT * "
            "From customers ")

version = cur.fetchall()
print(version)