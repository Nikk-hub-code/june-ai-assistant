from typing import List

from app.repositories.knowledge_repository import KnowledgeRepository
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
            query = query,
            limit = limit
        )

        return results
    
    def knowledge_exists(
            self,
            query: str
    ) -> bool:
        
        results = self.retrieve(
            query = query,
            limit = 1
        )

        return len(results) > 0