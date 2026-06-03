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

        # Step 1: Understanding
        understanding = self.understanding_engine.understand(
            user_query
        )

        topic = understanding["topic"]

        # Step 2: Retrieval
        retrieved_knowledge = self.retrieval_engine.retrieve(
            query=topic
        )

        knowledge_found = len(retrieved_knowledge) > 0

        # Step 3: Validation
        validation = self.validation_engine.validate(
            understanding=understanding,
            knowledge_found=knowledge_found
        )

        action = validation["action"]

        # --------------------------------------------------
        # CASE 1: Knowledge Missing
        # --------------------------------------------------
        if action == "research_required":

            research_result = self.research_engine.research(
                topic=topic
            )

            knowledge_result = (
                self.knowledge_service.create_from_research(
                    topic=topic,
                    research_result=research_result
                )
            )

            return {
                "user_query": user_query,
                "understanding": understanding,
                "validation": validation,
                "knowledge_found": False,
                "knowledge_action": knowledge_result["action"],
                "knowledge_record": knowledge_result["knowledge"],
                "research_result": research_result,
                "retrieved_knowledge": []
            }

        # --------------------------------------------------
        # CASE 2: Knowledge Exists But Needs Fresh Validation
        # --------------------------------------------------
        if action == "validate_existing_knowledge":

            research_result = self.research_engine.research(
                topic=topic
            )

            knowledge_result = (
                self.knowledge_service.create_from_research(
                    topic=topic,
                    research_result=research_result
                )
            )

            return {
                "user_query": user_query,
                "understanding": understanding,
                "validation": validation,
                "knowledge_found": True,
                "knowledge_action": knowledge_result["action"],
                "knowledge_record": knowledge_result["knowledge"],
                "research_result": research_result,
                "retrieved_knowledge": retrieved_knowledge
            }

        # --------------------------------------------------
        # CASE 3: Use Existing Knowledge
        # --------------------------------------------------
        return {
            "user_query": user_query,
            "understanding": understanding,
            "knowledge_found": knowledge_found,
            "validation": validation,
            "retrieved_knowledge": retrieved_knowledge
        }