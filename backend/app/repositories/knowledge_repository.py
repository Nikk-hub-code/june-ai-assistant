from typing import Optional, List

from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.models.knowledge import Knowledge


class KnowledgeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_knowledge(
            self,
            topic: str,
            content: str,
            source_url: Optional[str] = None,
            domain: Optional[str] = None,
            confidence_score: float = 0.0
    ) -> Knowledge:

        try:
            knowledge = Knowledge(
                topic=topic,
                content=content,
                source_url=source_url,
                domain=domain,
                confidence_score=confidence_score
            )

            self.db.add(knowledge)
            self.db.commit()
            self.db.refresh(knowledge)

            return knowledge

        except SQLAlchemyError as error:
            self.db.rollback()
            raise error

    def get_knowledge_by_id(
            self,
            knowledge_id: int
    ) -> Optional[Knowledge]:

        return (
            self.db.query(Knowledge)
            .filter(Knowledge.id == knowledge_id)
            .first()
        )

    def get_knowledge_by_topic(
            self,
            topic: str
    ) -> Optional[Knowledge]:

        return (
            self.db.query(Knowledge)
            .filter(Knowledge.topic == topic)
            .first()
        )

    # --------------------------------------------------
    # NEW: Canonical Topic Match
    # --------------------------------------------------
    def get_best_topic_match(
            self,
            topic: str
    ) -> Optional[Knowledge]:

        return (
            self.db.query(Knowledge)
            .filter(
                func.lower(Knowledge.topic)
                == topic.lower()
            )
            .order_by(
                Knowledge.confidence_score.desc()
            )
            .first()
        )

    def search_knowledge(
            self,
            query: str,
            limit: int = 10,
            offset: int = 0
    ) -> List[Knowledge]:

        return (
            self.db.query(Knowledge)
            .filter(
                Knowledge.topic.ilike(f"%{query}%")
                | Knowledge.content.ilike(f"%{query}%")
                | Knowledge.domain.ilike(f"%{query}%")
            )
            .order_by(
                Knowledge.confidence_score.desc()
            )
            .offset(offset)
            .limit(limit)
            .all()
        )

    def list_knowledge(
            self,
            limit: int = 20,
            offset: int = 0
    ) -> List[Knowledge]:

        return (
            self.db.query(Knowledge)
            .order_by(
                Knowledge.created_at.desc()
            )
            .offset(offset)
            .limit(limit)
            .all()
        )

    def update_knowledge(
            self,
            knowledge_id: int,
            topic: Optional[str] = None,
            content: Optional[str] = None,
            source_url: Optional[str] = None,
            domain: Optional[str] = None,
            confidence_score: Optional[float] = None
    ) -> Optional[Knowledge]:

        try:
            knowledge = self.get_knowledge_by_id(
                knowledge_id
            )

            if not knowledge:
                return None

            if topic is not None:
                knowledge.topic = topic

            if content is not None:
                knowledge.content = content

            if source_url is not None:
                knowledge.source_url = source_url

            if domain is not None:
                knowledge.domain = domain

            if confidence_score is not None:
                knowledge.confidence_score = confidence_score

            self.db.commit()
            self.db.refresh(knowledge)

            return knowledge

        except SQLAlchemyError as error:
            self.db.rollback()
            raise error

    def delete_knowledge(
            self,
            knowledge_id: int
    ) -> bool:

        try:
            knowledge = self.get_knowledge_by_id(
                knowledge_id
            )

            if not knowledge:
                return False

            self.db.delete(knowledge)
            self.db.commit()

            return True

        except SQLAlchemyError as error:
            self.db.rollback()
            raise error