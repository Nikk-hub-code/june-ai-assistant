from app.database.db import SessionLocal
from app.repositories.knowledge_repository import KnowledgeRepository
from app.engines.retrieval_engine import RetrievalEngine


def main():

    db = SessionLocal()

    try:
        repository = KnowledgeRepository(db)

        retrieval_engine = RetrievalEngine(repository)

        print("\n" + "=" * 50)
        print("TESTING RETRIEVAL ENGINE")
        print("=" * 50)

        # -----------------------------------
        # TEST 1
        # -----------------------------------
        print("\n[1] RETRIEVE PYTHON")

        results = retrieval_engine.retrieve("Python")

        print(f"Results Found: {len(results)}")

        for item in results:
            print(
                f"ID={item.id} | "
                f"Topic={item.topic} | "
                f"Domain={item.domain}"
            )

        # -----------------------------------
        # TEST 2
        # -----------------------------------
        print("\n[2] KNOWLEDGE EXISTS")

        exists = retrieval_engine.knowledge_exists(
            "Python"
        )

        print(f"Exists: {exists}")

        # -----------------------------------
        # TEST 3
        # -----------------------------------
        print("\n[3] UNKNOWN QUERY")

        exists = retrieval_engine.knowledge_exists(
            "Quantum Computing"
        )

        print(f"Exists: {exists}")

        print("\n" + "=" * 50)
        print("RETRIEVAL ENGINE TEST COMPLETE")
        print("=" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()