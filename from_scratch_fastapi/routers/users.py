from fastapi import APIRouter

from models import User

router = APIRouter(tags=["Users"])


@router.get("/users/{username}")
def get_user(username: str):
    return {"message": f"Hello, {username}!"}


@router.post("/users", status_code=201)
def create_user(user: User):
    return {"message": f"User {user.username} created successfully!", "user": user.model_dump()}
