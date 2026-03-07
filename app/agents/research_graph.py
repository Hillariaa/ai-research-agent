from langgraph.graph import StateGraph, END
from typing import TypedDict
from app.tools.web_search import web_search
from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AgentState(TypedDict):
    query: str
    search_results: list
    answer: str


# Search Tool
def search(state: AgentState):

    results = web_search(state["query"])

    return {"search_results": results}


# LLM Analysis
def analyze(state: AgentState):

    # Security
    if not state["search_results"]:
        return {
            "answer": {
                "summary": "No relevant sources were found.",
                "key_insights": [],
                "sources": [],
            }
        }

    context = "\n".join(
        [
            f"{r['title']} - {r['snippet']} ({r['link']})"
            for r in state["search_results"]
        ]
    )

    prompt = f"""
    You are an AI research assistant.

    Question:
    {state["query"]}

    Sources:
    {context}

    Return your answer as JSON with this structure:

    {{
        "summary": "short explanation",
        "key_insights": ["insight1", "insight2", "insight3"],
        "sources": ["source1", "source2", "source3"]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )

    content = response.choices[0].message.content or "{}"
    analysis = json.loads(content)

    return {"answer": analysis}


# Build Graph
builder = StateGraph(AgentState)

builder.add_node("search", search)
builder.add_node("analyze", analyze)

builder.set_entry_point("search")

builder.add_edge("search", "analyze")
builder.add_edge("analyze", END)

research_graph = builder.compile()
