from fastapi import FastAPI, HTTPException
from models import Product
from data import products

app = FastAPI(title="Product Service", version="1.0.0")


@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return product


@app.post("/products", status_code=201)
def create_product(product: Product):
    if any(p["id"] == product.id for p in products):
        raise HTTPException(status_code=400, detail=f"Product {product.id} already exists")
    products.append(product.dict())
    return product


@app.put("/products/{product_id}")
def update_product(product_id: int, updated: Product):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            products[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail=f"Product {product_id} not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products):
        if p["id"] == product_id:
            products.pop(i)
            return {"message": f"Product {product_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
