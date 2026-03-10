from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(credentials=Depends(security)):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Token")