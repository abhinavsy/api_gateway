from fastapi import APIRouter, Depends
from app.database.oracle_db import get_oracle_db
from app.services.cbs_data import get_user
from app.core.auth import verify_token

router = APIRouter()


@router.get("/user/{account_id}")
def fetch_user(account_id: str, db=Depends(get_oracle_db), user=Depends(verify_token)):

    return get_user(account_id, db)