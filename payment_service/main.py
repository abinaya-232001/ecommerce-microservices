from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Payment
from data import payments

app = FastAPI(title="Payment Service", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health_check():
    return {"service": "Payment Service", "status": "healthy", "port": 8005}

@app.get("/payments")
def get_all_payments():
    return payments

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    payment = next((p for p in payments if p["id"] == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.post("/payments", status_code=201)
def create_payment(payment: Payment):
    if any(p["id"] == payment.id for p in payments):
        raise HTTPException(status_code=400, detail="Payment already exists")
    payments.append(payment.dict())
    return payment

@app.put("/payments/{payment_id}")
def update_payment(payment_id: int, updated: Payment):
    for i, p in enumerate(payments):
        if p["id"] == payment_id:
            payments[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail="Payment not found")

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    for i, p in enumerate(payments):
        if p["id"] == payment_id:
            payments.pop(i)
            return {"message": f"Payment {payment_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Payment not found")