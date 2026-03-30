from fastapi import FastAPI, HTTPException
from model import Customer
from data import customers

app = FastAPI(title="Customer Service", version="1.0.0")


@app.get("/customers")
def get_all_customers():
    return customers


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = next((c for c in customers if c["id"] == customer_id), None)
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    return customer


@app.post("/customers", status_code=201)
def create_customer(customer: Customer):
    if any(c["id"] == customer.id for c in customers):
        raise HTTPException(status_code=400, detail=f"Customer {customer.id} already exists")
    customers.append(customer.dict())
    return customer


@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated: Customer):
    for i, c in enumerate(customers):
        if c["id"] == customer_id:
            customers[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    for i, c in enumerate(customers):
        if c["id"] == customer_id:
            customers.pop(i)
            return {"message": f"Customer {customer_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
