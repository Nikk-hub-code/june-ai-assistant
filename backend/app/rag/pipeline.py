from sqlalchemy.orm import Session

from app.engines.understanding_engine import UnderstandingEngine
from app.engines.retrieval_engine import RetrievalEngine
from app.engines.validation_engine import ValidationEngine
from app.engines.research_engine import ResearchEngine

from app.services.knowledge_service import KnowledgeService
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

        self.research_engine = ResearchEngine()

        self.knowledge_service = KnowledgeService(db)
    
    def process_query(self, user_query: str) -> dict:
        #Step 1
        understanding = self.understanding_engine.understand(
            user_query
        )

        topic = understanding["topic"]

        #Step 2
        retrieved_knowledge = self.retrieval_engine.retrieve(
            query= topic
        )

        knowledge_found = len(retrieved_knowledge) > 0

        #Step 3
        validation = self.validation_engine.validate(
            understanding = understanding,
            knowledge_found = knowledge_found
        )

        action = validation["action"]

        #Step 4
        if action == "research_required":

            research_result = self.research_engine.research(
                topic = topic
            )

            knowledge = self.knowledge_service.create_from_research(
                topic = topic,
                research_result = research_result
            )

            return {
                "user_query": user_query,
                "understanding": understanding,
                "validation": validation,
                "knowledge_found": False,
                "knowledge_created": knowledge,
                "research_result": research_result
            }

        return {
            "user_query": user_query,
            "understanding": understanding,
            "knowledge_found": knowledge_found,
            "validation": validation,
            "retrieved_knowledge": retrieved_knowledge
        }