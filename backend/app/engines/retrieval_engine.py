from typing import List, Optional

from app.repositories.knowledge_repository import (
    KnowledgeRepository
)
from app.database.models.knowledge import Knowledge


class RetrievalEngine:

    def __init__(
            self,
            repository: KnowledgeRepository
    ):
        self.repository = repository

    def retrieve(
            self,
            query: str,
            limit: int = 5
    ) -> List[Knowledge]:

        results = self.repository.search_knowledge(
            query=query,
            limit=limit
        )

        return results

    def retrieve_best_match(
            self,
            topic: str
    ) -> Optional[Knowledge]:

        return (
            self.repository.get_best_topic_match(
                topic
            )
        )

    def knowledge_exists(
            self,
            topic: str
    ) -> bool:

        knowledge = (
            self.retrieve_best_match(topic)
        )

        return knowledge is not None