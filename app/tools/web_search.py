from ddgs import DDGS


def web_search(query: str, max_results: int = 5):

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(
                {"title": r["title"], "snippet": r["body"], "link": r["href"]}
            )

    return results
