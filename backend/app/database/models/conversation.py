from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

from app.database.db import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key = True, index = True)

    created_at = Column(DateTime(timezone = True),
                        server_default = func.now())