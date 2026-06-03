from app.database.db import SessionLocal
from app.engines.research_engine import ResearchEngine
from app.services.knowledge_service import KnowledgeService


def main():

    db = SessionLocal()

    try:
        topic = "Transformer Neural Networks Architecture"

        research_engine = ResearchEngine()
        knowledge_service = KnowledgeService(db)

        print("\n" + "=" * 50)
        print("TESTING KNOWLEDGE SERVICE")
        print("=" * 50)

        research_result = research_engine.research(topic)

        result = knowledge_service.create_from_research(
            topic=topic,
            research_result=research_result
        )

        if result:

            knowledge = result["knowledge"]

            print("Action:", result["action"])
            print("Knowledge Stored Successfully")
            print("ID:", knowledge.id)
            print("Topic:", knowledge.topic)
            print("Domain:", knowledge.domain)
            print("Source URL:", knowledge.source_url)
            print("Confidence:", knowledge.confidence_score)

        else:
            print("No knowledge was stored")

        print("\n" + "=" * 50)
        print("KNOWLEDGE SERVICE TEST COMPLETE")
        print("=" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()