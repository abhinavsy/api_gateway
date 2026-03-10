from fastapi import APIRouter, Depends
from app.services.payment_service import create_payment_order
from app.core.auth import verify_token

router = APIRouter()


@router.post("/create-order")
def create_order(amount: int, user=Depends(verify_token)):

    order = create_payment_order(amount)

    return order