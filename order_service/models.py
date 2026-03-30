from pydantic import BaseModel


class Order(BaseModel):
    id: int | None = None
    customer_id: int
    items: list[str]
    total_price: float
    status: str