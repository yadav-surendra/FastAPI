from fastapi import FastAPI
from service.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the E-commerce API!"}

@app.get("/products")
def read_products(): 
    return get_all_products()