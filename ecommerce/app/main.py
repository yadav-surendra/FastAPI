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
        ),
    

    sort_by_price: bool = Query(
        default=False,
        description="Sort products by price"
    ),

    order: str = Query(
        default="asc",
        description="Sort order: 'asc' for ascending, 'desc' for descending"
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Limit the number of products returned"
    ),
    offset: int = Query(
        default=0,
        ge=0,
        description="Number of products to skip before starting to collect the result set" 
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
    
    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)
        # if reverse is true, it will sort in descending order, otherwise in ascending


    total = len(products)   
    products = products[offset:offset+limit]  # Apply the limit to the number of products returned

    return {
        "total": total,
        "items": products
        }

## working upto here