from pydantic import BaseModel

class Items(BaseModel):
    id:int
    name:str
    price:int
    quantity:int
    description:str
