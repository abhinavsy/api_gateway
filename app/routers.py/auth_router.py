from fastapi import APIRouter, HTTPException
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login")
def login(username: str, password: str):

    # example authentication
    if username != "admin" or password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"username": username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }