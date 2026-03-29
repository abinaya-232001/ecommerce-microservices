from pydantic import BaseModel, Field
from typing import Literal, Optional


class Payment(BaseModel):
    id: int = Field(..., description="Unique payment identifier")
    order_id: int = Field(..., description="ID of the order being paid for")
    customer_id: int = Field(..., description="ID of the customer making the payment")
    amount: float = Field(..., gt=0, description="Payment amount must be greater than zero")
    method: Literal["credit_card", "debit_card", "cash_on_delivery", "bank_transfer"] = Field(
        ..., description="Payment method used"
    )
    status: Literal["pending", "completed", "failed", "refunded"] = Field(
        ..., description="Current status of the payment"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": 4,
                "order_id": 4,
                "customer_id": 2,
                "amount": 800.00,
                "method": "debit_card",
                "status": "pending"
            }
        }


class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_id: Optional[int] = None
    amount: Optional[float] = Field(None, gt=0, description="Payment amount must be greater than zero")
    method: Optional[Literal["credit_card", "debit_card", "cash_on_delivery", "bank_transfer"]] = None
    status: Optional[Literal["pending", "completed", "failed", "refunded"]] = None