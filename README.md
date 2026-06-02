# 🧠 JUNE AI Assistant

> **JUNE (Just Unified Neural Engine)** is being developed as a **Persistent Knowledge Intelligence System**, not a traditional chatbot.

Unlike conventional AI assistants that depend entirely on Large Language Models (LLMs) for knowledge, JUNE is designed around a different philosophy:

```text
Knowledge + Retrieval + Validation = Intelligence
AI = Explanation Layer
```

The goal is to build an AI system that can continuously acquire, store, retrieve, validate, and improve knowledge over time while maintaining a persistent knowledge base.

---

# 🚀 Vision

Most AI systems work as:

```text
User Query
    ↓
LLM
    ↓
Response
```

JUNE is being built to work as:

```text
User Query
    ↓
Understanding Engine
    ↓
Knowledge Retrieval
    ↓
Internet Validation
    ↓
Knowledge Update
    ↓
AI Response Generation
    ↓
Response
```

This architecture allows JUNE to:

* Store knowledge permanently
* Reuse previously acquired knowledge
* Validate information against the internet
* Continuously improve its knowledge base
* Reduce dependence on AI hallucinations
* Support any domain instead of being domain restricted

---

# 🏗️ Current Architecture

```text
User Query
    ↓
Understanding Engine
    ↓
Retrieval Engine
    ↓
Knowledge Repository
    ↓
Neon PostgreSQL Database
```

---

# ⚙️ Technology Stack

## Frontend

* Next.js

## Backend

* FastAPI

## Database

* Neon PostgreSQL

## ORM

* SQLAlchemy

## Migration Management

* Alembic

## Future AI Layer

* Gemini API

## Future Research Layer

* Tavily API

## Future Knowledge Layer

* pgvector
* Embeddings
* Semantic Search
* RAG Pipeline

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── base.py
│   │   └── models/
│   │       ├── knowledge.py
│   │       ├── conversation.py
│   │       └── message.py
│   │
│   ├── engines/
│   │   ├── understanding_engine.py
│   │   └── retrieval_engine.py
│   │
│   ├── repositories/
│   │   └── knowledge_repository.py
│   │
│   ├── rag/
│   │   └── pipeline.py
│   │
│   └── utils/
│
├── tests/
│
├── alembic/
│
├── requirements.txt
├── alembic.ini
└── Dockerfile
```

---

# 🗄️ Database Design

## Knowledge Table

Stores validated knowledge used by JUNE.

| Field            | Description           |
| ---------------- | --------------------- |
| id               | Unique identifier     |
| topic            | Knowledge topic       |
| content          | Stored knowledge      |
| source_url       | Source reference      |
| domain           | Knowledge domain      |
| confidence_score | Confidence score      |
| created_at       | Creation timestamp    |
| updated_at       | Last update timestamp |

---

## Conversation Table

Stores conversation sessions.

| Field      | Description        |
| ---------- | ------------------ |
| id         | Conversation ID    |
| created_at | Creation timestamp |

---

## Message Table

Stores conversation messages.

| Field           | Description          |
| --------------- | -------------------- |
| id              | Message ID           |
| conversation_id | Related conversation |
| role            | User or Assistant    |
| content         | Message content      |
| created_at      | Creation timestamp   |

---

# 🧠 Implemented Components

## Understanding Engine

Responsible for converting natural language into structured machine-understandable information.

Example:

Input:

```text
What is Python?
```

Output:

```json
{
    "topic": "Python",
    "intent": "definition",
    "requires_freshness": false
}
```

Supported Intents:

* Definition
* Explanation
* Comparison
* Guidance
* Listing
* Latest Information

---

## Retrieval Engine

Responsible for retrieving relevant knowledge from the knowledge base.

Example:

```text
Topic: Python
```

↓

```text
Search Database
```

↓

```text
Return Knowledge Records
```

---

## Knowledge Repository

Production-grade repository layer implementing:

* Create Knowledge
* Retrieve Knowledge
* Search Knowledge
* Update Knowledge
* Delete Knowledge
* Pagination Support
* Exception Handling
* Rollback Support

---

## JUNE Pipeline v1

Current pipeline implementation:

```text
User Query
    ↓
Understanding Engine
    ↓
Retrieval Engine
    ↓
Knowledge Repository
    ↓
Database
```

---

# ✅ Completed Milestones

### Foundation Layer

* [x] FastAPI Backend Structure
* [x] Neon PostgreSQL Integration
* [x] SQLAlchemy Setup
* [x] Alembic Configuration
* [x] Database Models
* [x] Database Migrations

### Knowledge Layer

* [x] Knowledge Repository
* [x] CRUD Operations
* [x] Search Functionality
* [x] Repository Testing

### Intelligence Layer

* [x] Understanding Engine v2
* [x] Retrieval Engine v1
* [x] JUNE Pipeline v1

---

# 🧪 Testing

Implemented test modules:

```text
tests/
├── test_repository.py
├── test_repository_methods.py
├── test_understanding_engine.py
├── test_retrieval_engine.py
└── test_june_pipeline.py
```

Current pipeline tests successfully validate:

* Understanding Engine
* Retrieval Engine
* Knowledge Repository
* Database Connectivity
* End-to-End Pipeline Flow

---

# 🔮 Future Roadmap

## Phase 1 — Validation Layer

* Validation Engine
* Freshness Detection
* Internet Verification
* Knowledge Confidence Scoring

---

## Phase 2 — Research Layer

* Tavily Integration
* Knowledge Discovery
* Source Ranking
* Source Validation

---

## Phase 3 — Response Layer

* Gemini Integration
* Response Engine
* Context-Aware Responses
* Knowledge-Grounded Generation

---

## Phase 4 — Semantic Intelligence

* Embedding Engine
* pgvector Integration
* Vector Search
* Semantic Retrieval

---

## Phase 5 — RAG Architecture

* Context Builder
* Retriever
* RAG Pipeline
* Multi-Source Context Generation

---

## Phase 6 — Memory System

* Long-Term Memory
* User Preference Learning
* Persistent Context Management

---

## Phase 7 — Agentic Intelligence

* Autonomous Knowledge Updates
* Continuous Learning
* Self-Improving Knowledge Base
* Multi-Agent Workflows

---

# 🎯 Long-Term Goal

JUNE is not being built as another chatbot.

The long-term goal is to create a **Persistent Knowledge Intelligence System** capable of:

* Understanding user intent
* Managing its own knowledge
* Validating information autonomously
* Learning continuously
* Providing grounded and trustworthy responses

---

# 👨‍💻 Developer

**Kaushal Kumar Jha**

B.Tech Computer Science Engineering

Building intelligent systems focused on AI, Knowledge Engineering, Retrieval Systems, RAG, and Autonomous AI Assistants.

---

⭐ If you find this project interesting, consider starring the repository and following the development journey of JUNE AI Assistant.
