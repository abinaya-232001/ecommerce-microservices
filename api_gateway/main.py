from fastapi import FastAPI, HTTPException, Request
import httpx

app = FastAPI(title="E-Commerce API Gateway", version="1.0.0")

PRODUCT_SERVICE_URL      = "http://localhost:8001"
CUSTOMER_SERVICE_URL     = "http://localhost:8002"
ORDER_SERVICE_URL        = "http://localhost:8003"
INVENTORY_SERVICE_URL    = "http://localhost:8004"
PAYMENT_SERVICE_URL      = "http://localhost:8005"
NOTIFICATION_SERVICE_URL = "http://localhost:8006"


@app.get("/products")
async def gateway_get_products():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PRODUCT_SERVICE_URL}/products")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Product Service error")

@app.get("/products/{product_id}")
async def gateway_get_product(product_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Product Service error")

@app.post("/products", status_code=201)
async def gateway_create_product(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{PRODUCT_SERVICE_URL}/products", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Product Service error")

@app.put("/products/{product_id}")
async def gateway_update_product(product_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{PRODUCT_SERVICE_URL}/products/{product_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Product Service error")

@app.delete("/products/{product_id}")
async def gateway_delete_product(product_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Product Service error")


@app.get("/customers")
async def gateway_get_customers():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMER_SERVICE_URL}/customers")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Customer Service error")

@app.get("/customers/{customer_id}")
async def gateway_get_customer(customer_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Customer Service error")

@app.post("/customers", status_code=201)
async def gateway_create_customer(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{CUSTOMER_SERVICE_URL}/customers", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Customer Service error")

@app.put("/customers/{customer_id}")
async def gateway_update_customer(customer_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Customer Service error")

@app.delete("/customers/{customer_id}")
async def gateway_delete_customer(customer_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{CUSTOMER_SERVICE_URL}/customers/{customer_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Customer Service error")


@app.get("/orders")
async def gateway_get_orders():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{ORDER_SERVICE_URL}/orders")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Order Service error")

@app.get("/orders/{order_id}")
async def gateway_get_order(order_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{ORDER_SERVICE_URL}/orders/{order_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Order Service error")

@app.post("/orders", status_code=201)
async def gateway_create_order(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{ORDER_SERVICE_URL}/orders", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Order Service error")

@app.put("/orders/{order_id}")
async def gateway_update_order(order_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{ORDER_SERVICE_URL}/orders/{order_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Order Service error")

@app.delete("/orders/{order_id}")
async def gateway_delete_order(order_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{ORDER_SERVICE_URL}/orders/{order_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Order Service error")


@app.get("/inventory")
async def gateway_get_inventory():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{INVENTORY_SERVICE_URL}/inventory")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Inventory Service error")

@app.get("/inventory/{item_id}")
async def gateway_get_inventory_item(item_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{INVENTORY_SERVICE_URL}/inventory/{item_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Inventory Service error")

@app.post("/inventory", status_code=201)
async def gateway_create_inventory_item(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{INVENTORY_SERVICE_URL}/inventory", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Inventory Service error")

@app.put("/inventory/{item_id}")
async def gateway_update_inventory_item(item_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{INVENTORY_SERVICE_URL}/inventory/{item_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Inventory Service error")

@app.delete("/inventory/{item_id}")
async def gateway_delete_inventory_item(item_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{INVENTORY_SERVICE_URL}/inventory/{item_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Inventory Service error")


@app.get("/payments")
async def gateway_get_payments():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PAYMENT_SERVICE_URL}/payments")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Payment Service error")

@app.get("/payments/{payment_id}")
async def gateway_get_payment(payment_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PAYMENT_SERVICE_URL}/payments/{payment_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Payment Service error")

@app.post("/payments", status_code=201)
async def gateway_create_payment(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{PAYMENT_SERVICE_URL}/payments", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Payment Service error")

@app.put("/payments/{payment_id}")
async def gateway_update_payment(payment_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{PAYMENT_SERVICE_URL}/payments/{payment_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Payment Service error")

@app.delete("/payments/{payment_id}")
async def gateway_delete_payment(payment_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{PAYMENT_SERVICE_URL}/payments/{payment_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Payment Service error")


@app.get("/notifications")
async def gateway_get_notifications():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{NOTIFICATION_SERVICE_URL}/notifications")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Notification Service error")

@app.get("/notifications/{notification_id}")
async def gateway_get_notification(notification_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{NOTIFICATION_SERVICE_URL}/notifications/{notification_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Notification Service error")

@app.post("/notifications", status_code=201)
async def gateway_create_notification(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{NOTIFICATION_SERVICE_URL}/notifications", json=body)
    if r.status_code in (200, 201):
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Notification Service error")

@app.put("/notifications/{notification_id}")
async def gateway_update_notification(notification_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{NOTIFICATION_SERVICE_URL}/notifications/{notification_id}", json=body)
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Notification Service error")

@app.delete("/notifications/{notification_id}")
async def gateway_delete_notification(notification_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{NOTIFICATION_SERVICE_URL}/notifications/{notification_id}")
    if r.status_code == 200:
        return r.json()
    raise HTTPException(status_code=r.status_code, detail="Notification Service error")
