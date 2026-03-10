from fastapi import FastAPI
from app.routers import auth_router, payment_router, cbs_router
app = FastAPI(title="Fintech API Gateway")

app.include_router(auth_router.router, prefix="/auth")
app.include_router(payment_router.router, prefix="/payments")
app.include_router(cbs_router.router, prefix="/cbs")