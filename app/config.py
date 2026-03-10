from pydantic import BaseSettings


class Settings(BaseSettings):

    JWT_SECRET: str = "secret123"
    JWT_ALGORITHM: str = "HS256"

    RAZORPAY_KEY: str
    RAZORPAY_SECRET: str

    REDIS_URL: str = "redis://localhost:6379"

    ORACLE_DB: str
    DEFAULT_DB: str


settings = Settings()