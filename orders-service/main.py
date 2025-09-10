from fastapi import FastAPI

app = FastAPI()

orders = {
    1: {"id": 1, "user_id": 1, "item_id": 2},
    2: {"id": 2, "user_id": 2, "item_id": 1},
}

@app.get("/orders")
def get_orders():
    return list(orders.values())

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return orders.get(order_id, {"error": "Order not found"})
