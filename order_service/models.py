from typing import List, Optional

from pydantic import BaseModel


class Order(BaseModel):
    id: Optional[int] = None
    customer_id: int
    items: List[str]
    total_price: float
    status: str