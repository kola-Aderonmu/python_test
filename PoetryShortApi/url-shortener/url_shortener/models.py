from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(String, primary_key=True, index=True)
    original_url = Column(String, index=True)
    created_at = Column(DateTime(timezone=True),
    server_default=func.now())

