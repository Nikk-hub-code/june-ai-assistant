from sqlalchemy.orm import Session

from app.engines.understanding_engine import UnderstandingEngine
from app.engines.retrieval_engine import RetrievalEngine
from app.engines.validation_engine import ValidationEngine

from app.repositories.knowledge_repository import KnowledgeRepository


class JunePipeline:

    def __init__(self, db: Session):
        self.db = db

        self.understanding_engine = UnderstandingEngine()

        self.knowledge_repository = KnowledgeRepository(db)

        self.retrieval_engine = RetrievalEngine(
            self.knowledge_repository
        )

        self.validation_engine = ValidationEngine()
    
    def process_query(self, user_query: str) -> dict:
        understanding = self.understanding_engine.understand(
            user_query
        )

        topic = understanding["topic"]

        retrieved_knowledge = self.retrieval_engine.retrieve(
            query= topic
        )

        knowledge_found = len(retrieved_knowledge) > 0

        validation = self.validation_engine.validate(
            understanding = understanding,
            knowledge_found = knowledge_found
        )

        return {
            "user_query": user_query,
            "understanding": understanding,
            "knowledge_found": knowledge_found,
            "validation": validation,
            "retrieved_knowledge": retrieved_knowledge
        }