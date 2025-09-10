from fastapi import FastAPI

app = FastAPI()

items = {
    1: {"id": 1, "title": "Laptop", "price": 1200},
    2: {"id": 2, "title": "Phone", "price": 800},
}

@app.get("/items")
def get_items():
    return list(items.values())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})
