from fastapi import APIRouter, HTTPException

from data import fake_items
from models import Item

router = APIRouter(tags=["Items"])


@router.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return fake_items[skip : skip + limit]


@router.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_items):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items[item_id]


@router.get("/search")
def search_items(q: str):
    results = [item for item in fake_items if q.lower() in item["name"].lower()]
    if not results:
        raise HTTPException(status_code=404, detail="No items match your search")
    return {"results": results}


@router.post("/items", status_code=201)
def create_item(item: Item):
    if any(existing_item["name"].lower() == item.name.lower() for existing_item in fake_items):
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_items.append(item.model_dump())
    return item
