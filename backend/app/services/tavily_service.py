#tavily_service.py
from tavily import TavilyClient

from app.core.config import settings


class TavilyService:

    def __init__(self):
        self.client = TavilyClient(
            api_key = settings.TAVILY_API_KEY
        )
    
    def search(
            self,
            query: str,
            max_results: int = 5
    ) -> dict:
        
        response = self.client.search(
            query = query,
            search_depth = "advanced",
            max_results = max_results
        )

        return response