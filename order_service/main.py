from fastapi import FastAPI, HTTPException

from .data import orders
from .models import Order

app = FastAPI(title="Order Service")


# Convert Pydantic model → dict (supports v1 & v2)
def _dump_order(order: Order):
    if hasattr(order, "model_dump"):
        return order.model_dump()
    return order.dict()


# Generate next ID safely
def _next_id() -> int:
    max_id = 0
    for o in orders:
        if isinstance(o, dict):
            v = o.get("id")
            if isinstance(v, int) and v > max_id:
                max_id = v
    return max_id + 1


# 🔹 Root route (so you don’t get "Not Found")
@app.get("/")
def root():
    return {"message": "Order Service is running 🚀"}


# 🔹 Get all orders
@app.get("/orders")
def get_orders():
    return orders


# 🔹 Get order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


# 🔹 Create order
@app.post("/orders")
def create_order(order: Order):
    order.id = _next_id()
    orders.append(_dump_order(order))
    return order


# 🔹 Update order
@app.put("/orders/{order_id}")
def update_order(order_id: int, updated: Order):
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            updated.id = order_id
            orders[i] = _dump_order(updated)
            return updated
    raise HTTPException(status_code=404, detail="Order not found")


# 🔹 Delete order
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            return orders.pop(i)
    raise HTTPException(status_code=404, detail="Order not found")