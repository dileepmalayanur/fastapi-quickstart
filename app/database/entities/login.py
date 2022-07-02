from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from app.database.connector import Base


class Login(Base):
    __tablename__ = "login"

    id = Column(BigInteger, primary_key=True, index=True)
    email_address = Column(String(255), index=True)
    password_hash = Column(String)
    status = Column(String(5))
    created_at = Column(Date)
    created_by = Column(String(255))
    updated_at = Column(Date)
    updated_by = Column(String(255))
    profile_child = relationship("Profile", back_populates="login_parent", uselist=False)
