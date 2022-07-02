from sqlalchemy import Column, String, BigInteger, Integer
from sqlalchemy.types import Date
from app.database.connector import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(BigInteger, primary_key=True, index=True)
    country_code = Column(String(100), index=True)
    country_name = Column(String(100), index=True)
    country_flag = Column(String)
    time_zone = Column(Integer, index=True)
    created_at = Column(Date)
    created_by = Column(String(255))
    updated_at = Column(Date)
    updated_by = Column(String(255))

