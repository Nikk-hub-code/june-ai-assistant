from app.services.tavily_service import TavilyService


class ResearchEngine:

    def __init__(self):
        self.tavily_service = TavilyService()

    def research(
            self,
            topic: str,
            max_results: int = 5
    ) -> dict:
        
        search_results = self.tavily_service.search(
            query = topic,
            max_results = max_results
        )

        results = search_results.get(
            "results",
            []
        )

        research_found = len(results) > 0

        return {
            "topic": topic,
            "research_found": research_found,
            "results_count": len(results),
            "sources": results
        }