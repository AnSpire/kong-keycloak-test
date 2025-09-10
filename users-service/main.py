from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
}

@app.get("/users")
def get_users():
    return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})
