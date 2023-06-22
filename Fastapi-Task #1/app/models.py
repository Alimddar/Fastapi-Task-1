from pydantic import BaseModel,Field

class User(BaseModel):
    id: int 
    name: str
    surname: str
    age: int    

class Reviews(BaseModel):
    id: int
    user_id: int
    post_id: int

class Products(BaseModel):
    id: int 
    user_id: int
    name: str
    description: str
    img: str
    price: float
    review_count: int

class Orders(BaseModel):
    id: int
    used_id: int
    product_id: int
    adress: str 