from app.engines.research_engine import ResearchEngine


def main():

    engine = ResearchEngine()

    result = engine.research(
        topic="Quantum Computing"
    )

    print("\n" + "=" * 50)
    print("TESTING RESEARCH ENGINE")
    print("=" * 50)

    print("Topic:", result["topic"])
    print("Research Found:", result["research_found"])
    print("Results Count:", result["results_count"])

    print("\nTop Sources:\n")

    for source in result["sources"][:3]:

        print("Title:", source["title"])
        print("URL:", source["url"])
        print()

    print("=" * 50)
    print("RESEARCH ENGINE TEST COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()