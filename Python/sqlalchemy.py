# SQLAlchemy

# provide helpers, tools and components to assits with database development at every level
# consistent and fully featured facade over python DBAPI


# Philosophies
# - different databases and adapters to consistent interface
# - available features of each db
# - developers must continue thinking in sql


# Architecture

# - Core
#   - Engine - provides connection to a particular db
#   - Dialect - intrprets generic SQL and db commands in specific DBAPI 
#   - Connection Pool - holds a collection of database connections in memory for fast reuse
#   - SQL Expression Language - Allows to write SQL as python expressions
#   - Schema/Types - uses python objects to represent tables, column and datatypes

# - ORM
#   - build on top of the core
#   - maps python objects to relation database tables
#   - provides query system

# Level 1
# Engine


# instalation
pip install sqlalchemy


# connection to database
# whenever we want to interact with database, we need to create an engine
from sqlalchemy import create_engine

engine = create_engine('dialect+driver://username:password@host:port/database')
# 'postgresql+psycopg2://scott:tiger@localhost/mydatabase'


# creating Tables
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData

metadata = MetaData()
table = Table('table_name', metadata,
              Column('name', Integer, primary_key=True),
              Column('name', None, ForeignKey('table_name.id')),
              Column('name', String),
              Column('name', String(120)),
              )

# insert expressions
ins = table_name.insert().values(column_name1='', column_name2='')


# table declarative base class
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SomeTable(Base):
    __tablename__ = 'table_name'

    id = Column('id', Integer, primary_key=True)
    

Reference:
----------
create_engine(url)
    echo=False # activates logging system

# column data types
Integer - 
BigInteger
Boolean
Interval
Date
Time
Enum  - представляет набор возможных значений, которыми ограничен выбор
Float
Text
String






