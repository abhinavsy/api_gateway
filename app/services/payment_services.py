import razorpay
from app.config import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))


def create_payment_order(amount):

    data = {
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    }

    return client.order.create(data=data)