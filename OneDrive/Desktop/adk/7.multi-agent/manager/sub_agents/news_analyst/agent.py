from google.adk.agents import Agent
from google.adk.tools import google_search
from ddtrace.llmobs.decorators import agent
from ddtrace.llmobs import LLMObs
from dd_config import load_dd_config

load_dd_config()
@agent(name="news_analyst", ml_app="adk")
def news_analyst_agent(tool_context):
    """News analyst agent that analyzes news articles and provides summaries."""
    print("--- Tool: news_analyst_agent called ---")

    # Example implementation of news analysis
    query = tool_context.state.get("news_query", "latest news")
    print(f"Searching for news on: {query}")

    LLMObs.annotate(
        input_data={
            'role': 'user',
            'content': query
        },
        model_name=tool_context.agent.model,
    )

    # Use the google_search tool to find relevant news articles
    search_results = google_search(query=query, tool_context=tool_context)

    if search_results.get("status") == "success":

        articles = search_results.get("articles", [])
        summaries = [f"{article['title']}: {article['summary']}" for article in articles]

        LLMObs.annotate(
            output_data=[{
                "role": "assistant",
                "content": search_results.get("articles", [])
            }],
            metadata= {
                "source": articles[0].get("source", "Unknown"),
                "published_at": articles[0].get("published_at", "Unknown")
            },
            metrics= {
                "relevance_score": articles[0].get("relevance_score", 0.0),
                "sentiment_score": articles[0].get("sentiment_score", 0.0),
                "summary_length": len(articles[0].get("summary", "")),
            },
            tags={
                "status": search_results.get("status")
            })
        return {
            "status": "success", "summaries": summaries
        }
    else:
        LLMObs.annotate(
            output_data=search_results,
            model_name=tool_context.agent.model,
            tags={"search_query": query,
                  "status": search_results.get("status")},
        )
        return {"status": "error", "error_message": "Failed to fetch news articles."}

news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
    tools=[google_search],
)