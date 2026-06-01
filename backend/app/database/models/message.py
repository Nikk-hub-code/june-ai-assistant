from sqlalchemy import (Column,
                        Integer,
                        Text,
                        DateTime,
                        ForeignKey)


from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.db import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key = True, index = True)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )

    role = Column(Text, nullable = False)

    content = Column(Text, nullable = False)

    created_at = Column(
        DateTime(timezone = True),
        server_default = func.now()
    )

    conversation = relationship(
        "Conversation",
        backref = "messages"
    )