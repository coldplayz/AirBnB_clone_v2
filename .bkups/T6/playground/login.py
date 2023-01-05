#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://Bel2:44384439@localhost/hbnb_0e_6_usa', pool_pre_ping=True)

b = declarative_base()

class A(b):
    __tablename__ = 'tableA'
    id = Column(Integer, primary_key=True)

class B(b):
    __tablename__ = 'tableB'
    id = Column(Integer, primary_key=True)

Session = sessionmaker(bind=engine)
sess = Session()
