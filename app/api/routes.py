from fastapi import APIRouter
from app.agents.research_graph import research_graph

router = APIRouter()


@router.post("/research")
def research_topic(query: str):
    result = research_graph.invoke({"query": query, "search_results": [], "answer": ""})

    return result["answer"]
