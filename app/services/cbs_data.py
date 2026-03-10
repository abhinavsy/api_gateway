from sqlalchemy import text


def get_user(account_id, db):

    query = text("SELECT * FROM USERS WHERE ACCOUNT_ID = :id")

    result = db.execute(query, {"id": account_id})

    return result.fetchone()