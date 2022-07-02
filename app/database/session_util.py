from .connector import SessionLocal

def getDbSession():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()