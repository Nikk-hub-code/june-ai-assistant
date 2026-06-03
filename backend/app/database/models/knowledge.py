#knowledge.py
from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class Knowledge(Base):
    __tablename__ = "knowledge"

    id = Column(Integer, primary_key = True, index = True)

    topic = Column(String(255), nullable = False)

    content = Column(Text, nullable = False)

    source_url = Column(Text)

    domain = Column(String(100))

    confidence_score = Column(Float, default = 0.0)

    created_at = Column(DateTime(timezone = True),
                        server_default = func.now())
    
    updated_at = Column(DateTime(timezone = True),
                        onupdate = func.now())