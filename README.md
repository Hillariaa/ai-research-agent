# AI Research Agent

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)

An **AI-powered research assistant** that autonomously searches the web and synthesizes structured insights using a **tool-using LLM agent built with LangGraph**.

The system performs real-time research by combining **web search tools with large language model reasoning**, producing structured summaries, key insights, and cited sources.

---

# Overview

This project demonstrates how to build a **tool-using AI agent architecture** that integrates:

- LLM reasoning
- external tools
- structured outputs
- API deployment

The agent autonomously:

1. Receives a research query
2. Searches the web for relevant information
3. Synthesizes insights using an LLM
4. Returns structured research results

---

# Architecture

```
User Query
   ↓
FastAPI API
   ↓
LangGraph Agent
   ↓
Web Search Tool (DDGS)
   ↓
LLM Analysis (OpenAI)
   ↓
Structured Research Output
```

---

# Example Output

```
{
  "summary": "Recent breakthroughs in AI agents focus on improving reasoning capabilities, memory management, and multi-agent collaboration.",
  "key_insights": [
    "New reasoning models are being optimized for agent-based workflows.",
    "AI agents are gaining longer context windows and persistent memory.",
    "Multi-agent architectures are enabling more complex autonomous systems."
  ],
  "sources": [
    "Latest AI breakthroughs 2026",
    "AI Agents: Evolution and Architecture",
    "Research on Autonomous AI Systems"
  ]
}
```

---

# Tech Stack

- **Python**
- **FastAPI** – API layer
- **LangGraph** – AI agent workflow orchestration
- **OpenAI API** – LLM reasoning
- **DuckDuckGo Search (DDGS)** – web search tool
- **Docker** – containerized deployment
- **uv** – dependency and environment management

---

# Project Structure

```
ai-research-agent
│
├── app
│   ├── api
│   │   └── routes.py
│   │
│   ├── agents
│   │   └── research_graph.py
│   │
│   ├── tools
│   │   └── web_search.py
│   │
│   └── main.py
│
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

# Running Locally

Install dependencies:

```
uv sync
```

Run the API server:

```
uv run uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

# Running with Docker

Build the container:

```
docker build -t ai-research-agent .
```

Run the container:

```
docker run -p 8000:8000 -e OPENAI_API_KEY=your_api_key ai-research-agent
```

Open the API:

```
http://localhost:8000/docs
```

---

# API Endpoint

### POST `/research`

Performs autonomous research on a given topic.

Example query:

```
latest breakthroughs in AI agents
```

Returns structured research results including:

- summary
- key insights
- sources

---

# Key AI Engineering Concepts Demonstrated

This project demonstrates several **core applied AI engineering patterns**:

- Tool-using LLM agents
- External knowledge retrieval
- Structured LLM outputs
- Agent workflow orchestration
- API-based AI system deployment
- Containerized AI services

---

# Author

Hilary Azimoh
