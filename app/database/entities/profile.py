from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from app.database.connector import Base
from app.database.entities.country import Country


class Profile(Base):
    __tablename__ = "profile"

    id = Column(BigInteger, primary_key=True, index=True)
    login_id = Column(BigInteger, ForeignKey("login.id"))
    first_name = Column(String(100))
    middle_name = Column(String(100))
    last_name = Column(String(100))
    gender_code = Column(String(100), index=True)
    country_code = Column(String(100), ForeignKey("country.country_code"))
    created_at = Column(Date)
    created_by = Column(String(255))
    updated_at = Column(Date)
    updated_by = Column(String(255))
    login_parent = relationship("Login", back_populates="profile_child")
    country_parent = relationship(Country)
