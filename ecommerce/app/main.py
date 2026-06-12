from fastapi import FastAPI , HTTPException, Query
from service.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the E-commerce API!"}


# @app.get("/products")
# def read_products(): 
#     return get_all_products()

# how to use query in search

@app.get("/products")

def list_products(

    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Filter products by name"
        )
    ):
    
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name","").lower()]

        if not products:
            raise HTTPException(
                status_code=404, detail=f"No products found matching the name={name}"
                )
        
    total = len(products)   

    return {
        "total": total,
        "items": products
        }