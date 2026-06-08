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
        print("\n[2] BEST MATCH")

        best_match = retrieval_engine.retrieve_best_match(
            "Python"
        )

        if best_match:
            print(
                f"ID={best_match.id} | "
                f"Topic={best_match.topic} | "
                f"Domain={best_match.domain}"
            )
        else:
            print("No exact match found")
        # -----------------------------------
        # TEST 3
        # -----------------------------------
        print("\n[3] KNOWLEDGE EXISTS")

        exists = retrieval_engine.knowledge_exists(
            "Python"
        )

        print(f"Exists: {exists}")

        # -----------------------------------
        # TEST 4
        # -----------------------------------
        print("\n[4] UNKNOWN QUERY")

        exists = retrieval_engine.knowledge_exists(
            "Alien Quantum Banana Theory"
        )

        print(f"Exists: {exists}")

        print("\n" + "=" * 50)
        print("RETRIEVAL ENGINE TEST COMPLETE")
        print("=" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()