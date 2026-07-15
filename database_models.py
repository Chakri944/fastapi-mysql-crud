from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,Float,String

base=declarative_base()

class Items(base):

    __tablename__="products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    price=Column(Float)
    quantity=Column(Integer)
    description=Column(String(50))