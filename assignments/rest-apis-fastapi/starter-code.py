from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

items: Dict[int, Item] = {
    1: Item(name="Notebook", price=3.99),
    2: Item(name="Pen", price=1.49),
}

next_id = 3

@app.get("/items")
def list_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    global next_id
    items[next_id] = Item(**item.dict())
    response = {"id": next_id, **items[next_id].dict()}
    next_id += 1
    return response

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = Item(**item.dict())
    return {"id": item_id, **items[item_id].dict()}
