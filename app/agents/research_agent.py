from openai import OpenAI
from app.tools.web_search import web_search
from openai.types.chat import ChatCompletionUserMessageParam
import json

client = OpenAI()


def research(query: str):

    search_results = web_search(query)

    if not search_results:
        return {
            "summary": "No relevant sources found",
            "key_insights": [],
            "sources": [],
        }

    context = "\n".join([f"{r['title']}: {r['snippet']}" for r in search_results])

    prompt = f"""
    You are a research assistant.

    Question:
    {query}

    Sources:
    {context}


    Provide:
    1. Summary
    2. Key insights
    3. Sources referenced
    """

    messages: list[ChatCompletionUserMessageParam] = [
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content or "{}"

    return json.loads(content)
