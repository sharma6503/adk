from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


def get_current_time()-> dict:
    """
    Returns the current time in ISO format.
    """
    return {
        "current_time": datetime.now().isoformat()
    }


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="An agent that uses tools to assist users with various tasks.",
    instruction="You are a helpful agent that can use tools to assist users with their tasks. Use the available tools to provide accurate and helpful responses.",
    # tools=[google_search],
    # tools=[google_search, get_current_time] # adk wont support this yet`
    tools=[get_current_time]
)