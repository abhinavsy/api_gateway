from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(settings.ORACLE_DB)

OracleSession = sessionmaker(bind=engine)


def get_oracle_db():
    db = OracleSession()
    try:
        yield db
    finally:
        db.close()