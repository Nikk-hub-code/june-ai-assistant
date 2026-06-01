from app.database.db import SessionLocal

from app.repositories.knowledge_repository import (
    KnowledgeRepository
)


db = SessionLocal()

repository = KnowledgeRepository(db)

knowledge = repository.create_knowledge(
    topic = "Python",
    content = "Python is a high-level programming language.",
    source_url = "https://python.org",
    domain = "Programming",
    confidence_score = 0.95
)

print(knowledge.id)
print(knowledge.topic)

db.close()