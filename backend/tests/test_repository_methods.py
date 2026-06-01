from app.database.db import SessionLocal
from app.repositories.knowledge_repository import KnowledgeRepository


def main():
    db = SessionLocal()
    repository = KnowledgeRepository(db)

    try:
        print("\n" + "=" * 50)
        print("TESTING KNOWLEDGE REPOSITORY")
        print("=" * 50)

        # ----------------------------
        # CREATE
        # ----------------------------
        print("\n[1] CREATE KNOWLEDGE")

        knowledge = repository.create_knowledge(
            topic="Machine Learning",
            content="Machine Learning is a subset of AI.",
            source_url="https://example.com/ml",
            domain="AI",
            confidence_score=0.90
        )

        print(f"Created ID: {knowledge.id}")
        print(f"Topic: {knowledge.topic}")

        knowledge_id = knowledge.id

        # ----------------------------
        # GET BY ID
        # ----------------------------
        print("\n[2] GET KNOWLEDGE BY ID")

        result = repository.get_knowledge_by_id(knowledge_id)

        print(f"ID: {result.id}")
        print(f"Topic: {result.topic}")

        # ----------------------------
        # GET BY TOPIC
        # ----------------------------
        print("\n[3] GET KNOWLEDGE BY TOPIC")

        result = repository.get_knowledge_by_topic(
            "Machine Learning"
        )

        if result:
            print(f"Found: {result.topic}")
        else:
            print("No record found")

        # ----------------------------
        # SEARCH
        # ----------------------------
        print("\n[4] SEARCH KNOWLEDGE")

        results = repository.search_knowledge(
            query="Machine"
        )

        print(f"Records Found: {len(results)}")

        for item in results:
            print(
                f"ID={item.id} | "
                f"Topic={item.topic}"
            )

        # ----------------------------
        # LIST
        # ----------------------------
        print("\n[5] LIST KNOWLEDGE")

        results = repository.list_knowledge(
            limit=5
        )

        print(f"Total Returned: {len(results)}")

        for item in results:
            print(
                f"ID={item.id} | "
                f"Topic={item.topic}"
            )

        # ----------------------------
        # UPDATE
        # ----------------------------
        print("\n[6] UPDATE KNOWLEDGE")

        updated = repository.update_knowledge(
            knowledge_id,
            content="Machine Learning is a branch of Artificial Intelligence.",
            confidence_score=0.98
        )

        print("Updated Content:")
        print(updated.content)

        print("Updated Confidence:")
        print(updated.confidence_score)

        # ----------------------------
        # DELETE
        # ----------------------------
        print("\n[7] DELETE KNOWLEDGE")

        deleted = repository.delete_knowledge(
            knowledge_id
        )

        print(f"Deleted: {deleted}")

        # ----------------------------
        # VERIFY DELETE
        # ----------------------------
        print("\n[8] VERIFY DELETE")

        result = repository.get_knowledge_by_id(
            knowledge_id
        )

        print(f"Result: {result}")

        print("\n" + "=" * 50)
        print("ALL TESTS COMPLETED")
        print("=" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()