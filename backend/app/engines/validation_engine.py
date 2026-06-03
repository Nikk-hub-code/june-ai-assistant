#validation_engine.py
class ValidationEngine:

    def validate(
            self,
            understanding: dict,
            knowledge_found: bool
    ) -> dict:
        
        requires_freshness = understanding[
            "requires_freshness"
        ]

        if not knowledge_found:
            return {
                "action": "research_required",
                "reason": "knowledge_not_found"
            }
        
        if requires_freshness:
            return {
                "action": "validate_existing_knowledge",
                "reason": "knowledge_exists_but_requires_freshness_check"
            }
        
        return {
            "action": "use_existing_knowledge",
            "reason": "knowledge_exists_and_is_not_time_sensitive"
        }
        
