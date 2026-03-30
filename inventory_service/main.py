from fastapi import FastAPI, HTTPException
from models import InventoryItem
from data import inventory

app = FastAPI()

@app.get("/inventory")
def get_all():
    return inventory

@app.get("/inventory/{item_id}")
def get_one(item_id: int):
    for item in inventory:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Not found")

@app.post("/inventory")
def create(item: InventoryItem):
    inventory.append(item.dict())
    return item

@app.put("/inventory/{item_id}")
def update(item_id: int, updated: InventoryItem):
    for i in range(len(inventory)):
        if inventory[i]["id"] == item_id:
            inventory[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404)

@app.delete("/inventory/{item_id}")
def delete(item_id: int):
    for i in range(len(inventory)):
        if inventory[i]["id"] == item_id:
            return inventory.pop(i)
    raise HTTPException(status_code=404)