from pydantic import BaseModel


class PaymentCreate(BaseModel):

    amount: int
    currency: str


class PaymentResponse(BaseModel):

    order_id: str
    amount: int
    currency: str
    status: str

    class Config:
        orm_mode = True



# import inspect

# inspect.iscoroutinefunction(my_function)