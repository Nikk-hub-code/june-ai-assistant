#understanding_engine.py
import re


class UnderstandingEngine:

    def understand(self, user_query: str) -> dict:
        cleaned_query = self._clean_query(user_query)

        intent = self._detect_intent(cleaned_query)

        requires_freshness = self._requires_freshness(cleaned_query)

        topic = self._extract_topic(cleaned_query, intent)

        return {
            "original_query": user_query,
            "cleaned_query": cleaned_query,
            "topic": topic,
            "intent": intent,
            "requires_freshness": requires_freshness
        }
    
    def _clean_query(self, query: str) -> str:
        query = query.strip()
        query = re.sub(r"\s+", " ", query)
        return query
    
    def _detect_intent(self, query: str) -> str:
        query_lower = query.lower()

        if any(word in query_lower for word in ["compare", "difference between", "vs", "versus"]):
            return "comparison"
        
        if any(word in query_lower for word in ["latest", "current", "today", "recent", "new", "updated"]):
            return "latest_information"
        
        if any(word in query_lower for word in ["list", "types", "examples"]):
            return "listing"
        
        if any(word in query_lower for word in ["how to", "steps", "guide", "roadmap"]):
            return "guidance"
        
        if any(word in query_lower for word in ["explain", "describe"]):
            return "explanation"
        
        if any(word in query_lower for word in ["what is", "who is", "define", "meaning of"]):
            return "definition"
        
        return "general"
    
    def _requires_freshness(self, query: str) -> bool:
        query_lower = query.lower()

        freshness_keywords = [
            "latest",
            "current",
            "today",
            "recent",
            "new",
            "updated",
            "now",
            "this year",
            "this month",
            "this week",
            "live",
            "price",
            "version",
            "news"
        ]

        return any(keyword in query_lower for keyword in freshness_keywords)
    
    def _extract_topic(self, query: str, intent: str) -> str:
        query_lower = query.lower()

        removable_phrases = [
            "what is",
            "who is",
            "define",
            "meaning of",
            "explain",
            "describe",
            "compare",
            "difference between",
            "latest",
            "current",
            "today",
            "recent",
            "new",
            "updated",
            "list",
            "types of",
            "examples of",
            "how to",
            "steps to",
            "guide to",
            "roadmap for",
            "version of",
            "price of",
        ]

        topic = query

        topic = topic.strip()

        for phrase in removable_phrases:
            topic = re.sub(
                re.escape(phrase),
                "",
                topic,
                flags=re.IGNORECASE
            )
        
        topic = re.sub(
            r"^\s*learn\s+",
            "",
            topic,
            flags = re.IGNORECASE
        )

        topic = re.sub(r"[?.!,]", "", topic)

        stop_words = {
            "the",
            "a",
            "an",
            "of",
            "for"
        }

        words = topic.split()

        words = [
            word
            for word in words
            if word.lower() not in stop_words
        ]

        topic = " ".join(words)

        topic = re.sub(
            r"\s+",
            " ",
            topic
        ).strip()

        if not topic:
            topic = query

        return topic