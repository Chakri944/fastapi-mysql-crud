from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="mysql+pymysql://root:pass123@localhost:3306/products"
engine=create_engine(db_url)
session=sessionmaker(bind=engine, autoflush=False, autocommit=False)

