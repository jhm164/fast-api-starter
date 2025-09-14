from fastapi import FastAPI
import json
import os

app = FastAPI()
print("Current working directory:", os.getcwd())
user_db = []
product_db = []
with open(
    os.path.join(
        os.getcwd(),
        "src",
        "fast_api_complete",
        "supportive_functions",
        "data",
        "user.json",
    ),
    "r",
) as f:
    user_db = json.load(f)
    print("user_db:", user_db)

with open(
    os.path.join(
        os.getcwd(),
        "src",
        "fast_api_complete",
        "supportive_functions",
        "data",
        "product.json",
    ),
    "r",
) as f:
    product_db = json.load(f)


@app.post("/login")
async def login_user(username: str, password: str):
    for value in user_db:
        if value["username"] == username and value["password"] == password:
            return {"message": "Login successful", "user": value}
    return {"message": "Invalid credentials"}


@app.get("/products")
async def get_products(price: float):
    for p in product_db:
        if price >= p.price:
            return {p}
    return {"message": "no match found"}
