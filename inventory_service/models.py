from pydantic import BaseModel

class InventoryItem(BaseModel):
    id: int
    product_id: int
    name: str
    quantity: int
    price: float
    warehouse_location: str