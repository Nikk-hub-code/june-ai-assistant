from app.engines.validation_engine import ValidationEngine


def main():

    engine = ValidationEngine()

    test_cases = [
        {
            "query": "What is Python?",
            "understanding": {
                "requires_freshness": False
            },
            "knowledge_found": True
        },
        {
            "query": "Latest version of Python",
            "understanding": {
                "requires_freshness": True
            },
            "knowledge_found": True
        },
        {
            "query": "What is Quantum Computing?",
            "understanding": {
                "requires_freshness": False
            },
            "knowledge_found": False
        }
    ]

    print("\n" + "=" * 50)
    print("TESTING VALIDATION ENGINE")
    print("=" * 50)

    for case in test_cases:

        result = engine.validate(
            understanding=case["understanding"],
            knowledge_found=case["knowledge_found"]
        )

        print("\nQuery:", case["query"])
        print("Action:", result["action"])
        print("Reason:", result["reason"])

    print("\n" + "=" * 50)
    print("VALIDATION ENGINE TEST COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()