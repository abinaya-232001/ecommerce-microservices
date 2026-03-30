from fastapi import FastAPI, HTTPException

from .data import orders
from .models import Order

app = FastAPI(title="Order Service")


def _next_id() -> int:
    existing_ids = [o["id"] for o in orders if isinstance(o.get("id"), int)]
    return (max(existing_ids) + 1) if existing_ids else 1


@app.get("/orders")
def get_orders():
    return orders


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.post("/orders")
def create_order(order: Order):
    order.id = _next_id()
    orders.append(order.model_dump())
    return order


@app.put("/orders/{order_id}")
def update_order(order_id: int, updated: Order):
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            updated.id = order_id
            orders[i] = updated.model_dump()
            return updated
    raise HTTPException(status_code=404, detail="Order not found")


@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            return orders.pop(i)
    raise HTTPException(status_code=404, detail="Order not found")