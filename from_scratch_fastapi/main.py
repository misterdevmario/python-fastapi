from fastapi import FastAPI

from routers import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
def home():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"name": "Mario", "learning": "FastAPI"}
