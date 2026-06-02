from app.database.db import SessionLocal
from app.rag.pipeline import JunePipeline


def main():
    db = SessionLocal()

    try:
        pipeline = JunePipeline(db)

        test_queries = [
            "What is Python?",
            "Explain Python",
            "Latest version of Python",
            "What is Quantum Computing?"
        ]

        print("\n" + "=" * 50)
        print("TESTING JUNE PIPELINE V1")
        print("=" * 50)

        for query in test_queries:
            result = pipeline.process_query(query)

            print("\nUser Query:", result["user_query"])
            print("Topic:", result["understanding"]["topic"])
            print("Intent:", result["understanding"]["intent"])
            print(
                "Requires Freshness:",
                result["understanding"]["requires_freshness"]
            )
            print("Knowledge Found:", result["knowledge_found"])

            print("Action:",
                    result["validation"]["action"])
            
            print("Reason:",
                    result["validation"]["reason"])

            if result["knowledge_found"]:
                print("Retrieved Knowledge:")

                for item in result["retrieved_knowledge"]:
                    print(
                        f"  ID={item.id} | "
                        f"Topic={item.topic} | "
                        f"Domain={item.domain}"
                    )

        print("\n" + "=" * 50)
        print("JUNE PIPELINE V1 TEST COMPLETE")
        print("=" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()