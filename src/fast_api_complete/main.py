from unittest import case
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/get_user")
async def grabuserdata(user_type: str):
    response = {}
    if user_type == "admin":
        response = {"data": "Admin data"}
    elif user_type == "user":
        response = {"data": "User data"}
    else:
        response = {"data": "Unknown user type"}
    return response
