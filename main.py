from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Items
from database import session, engine
import database_models
from sqlalchemy.orm import Session
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*']
)

database_models.base.metadata.create_all(bind=engine)

# products=[
#     Items(id=1,name="milk",price=25,quantity=10),
#     Items(id=3,name="curd",price=20,quantity=110),
#     Items(id=6,name="ghee",price=5,quantity=12),
#     Items(id=24,name="butter",price=15,quantity=30),
#     Items(id=4,name="honey",price=22,quantity=43)
# ]

def db_get():
    db=session()
    try:
        yield db
    finally:
        db.close()
        

def db_inti():
    db=session()
    count = db.query(database_models.Items).count()
    print(count)
    if count==0:
        for product in products:
            db.add(database_models.Items(**product.model_dump()))
        db.commit()

db_inti()

@app.get("/products")
def All_products(db:Session=Depends(db_get)):
    db_product=db.query(database_models.Items).all()
    return db_product

@app.get("/products/{id}")
def product_by_id(id:int, db:Session=Depends(db_get)):
    db_product=db.query(database_models.Items).filter(database_models.Items.id==id).first()
    if db_product:
        return db_product
    return f"not found id:{id}"

@app.post("/products")
def Add_products(product:Items,db:Session=Depends(db_get)):
    db.add(database_models.Items(**product.model_dump()))
    db.commit()
    return products

@app.put("/products/{id}")
def update_products(id:int,product:Items,db:Session=Depends(db_get)):
    product_db=db.query(database_models.Items).filter(database_models.Items.id==id).first()
    if product_db:
        product_db.name=product.name
        product_db.price=product.price
        product_db.quantity=product.quantity
        product_db.description=product.description
        db.commit()  
        return "added"
    return "not found"

@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(db_get)):
    db_product=db.query(database_models.Items).filter(database_models.Items.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "deleted"
    return "not found"