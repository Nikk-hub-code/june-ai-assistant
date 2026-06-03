from sqlalchemy.orm import Session

from app.repositories.knowledge_repository import KnowledgeRepository


class KnowledgeService:

    def __init__(self, db: Session):
        self.repository = KnowledgeRepository(db)

    def create_from_research(
            self,
            topic: str,
            research_result: dict,
            domain: str = "Research"
    ):
        
        sources = research_result.get("sources", [])

        if not sources:
            return None
        
        best_source = sources[0]

        content = best_source.get("content", "")
        source_url = best_source.get("url", "")
        confidence_score = best_source.get("score", 0.80)

        existing_knowledge = (
            self.repository.get_knowledge_by_topic(
                topic
            )
        )

        if existing_knowledge:

            knowledge = self.repository.update_knowledge(
                knowledge_id = existing_knowledge.id,
                content = content,
                source_url = source_url,
                domain = domain,
                confidence_score = confidence_score
            )

            return {
                "knowledge": knowledge,
                "action": "updated"
            }

        knowledge = self.repository.create_knowledge(
            topic = topic,
            content = content,
            source_url = source_url,
            domain = domain,
            confidence_score = confidence_score
        )

        return {
            "knowledge": knowledge,
            "action": "created"
        }