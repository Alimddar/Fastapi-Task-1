from typing import Union
from fastapi import FastAPI
from models import User,Products,Reviews,Orders
app = FastAPI()

users = []
orders = []
reviews = []
products = []

user_id = 0
@app.post("/user", tags=['User'])
async def post_user(user: User):
    global user_id
    user.id = user_id
    user_id += 1
    users.append(user)
    return "User has been successfully added to Db"
    

@app.get("/user", tags=['User'])
async def return_user(id: int):
    for user in users:
        if user.id == id:
            return user

@app.get('/users',tags=['User'])
async def return_users():
    return users

product_id = 0
@app.post("/product",tags=['Product'])
async def post_product(product: Products): 
    global product_id
    product.id = product_id
    product_id += 1
    products.append(product)
    return 'Your product has been successfully added to Db'
    
@app.get("/product",tags=['Product'])
async def return_product(id: int):
    for product in products:
        if products.id == id:
            return product

@app.get('/products',tags=['Product'])
async def return_products():
    return products

order_id = 0
@app.post("/order",tags=['Order'])
async def post_order(order: Orders): 
    global order_id
    order.id = order_id
    order_id += 1
    orders.append(order)
    return 'Your order has been successfully added to Db'

@app.get("/order",tags=['Order'])
async def return_order(id: int):
    for order in orders:    
        if order.id == id:
            return order

review_id = 0
@app.post("/review", tags=['Review'])
async def review_post(review: Reviews):
    global review_id
    review.id = review_id
    review_id += 1
    reviews.append(review)  
    return 'Worked Successfully'

@app.get("/review", tags=['Review'])
async def return_review(id: int):
    for review in reviews:
        if review.id == id:
            return review
