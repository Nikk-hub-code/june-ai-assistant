from app.services.tavily_service import TavilyService


def main():

    service = TavilyService()

    result = service.search(
        query="What is Quantum Computing?"
    )

    print("\n" + "=" * 50)
    print("TAVILY TEST")
    print("=" * 50)

    print(result)

    print("\n" + "=" * 50)
    print("TEST COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()