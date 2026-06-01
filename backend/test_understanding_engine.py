from app.engines.understanding_engine import UnderstandingEngine


def main():
    engine = UnderstandingEngine()

    test_queries = [
        "What is Python?",
        "Explain Machine Learning",
        "Latest version of Python",
        "Compare Python and Java",
        "How to learn FastAPI",
        "List types of machine learning",
        "Who is Elon Musk?",
        "What is the current price of Bitcoin?"
    ]

    print("\n" + "=" * 50)
    print("TESTING UNDERSTANDING ENGINE")
    print("=" * 50)

    for query in test_queries:
        result = engine.understand(query)

        print("\nQuery:", query)
        print("Topic:", result["topic"])
        print("Intent:", result["intent"])
        print("Requires Freshness:", result["requires_freshness"])

    print("\n" + "=" * 50)
    print("UNDERSTANDING ENGINE TEST COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()