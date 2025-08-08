from google.adk.agents import Agent
from .sub_agents.funny_nerd.agent import funny_nerd
from google.adk.tools.agent_tool import AgentTool
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time
from dd_config import load_dd_config

load_dd_config()

root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="This is the root agent that manages all sub-agents.",
    instruction=""" 
    You are a manager agent that is responsible for overseeing the work of the other agents.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - stock_analyst
    - funny_nerd

    You also have access to the following tools:
    - news_analyst
    - get_current_time
    You can use these tools to assist you in your tasks.
    """,
    tools=[get_current_time,AgentTool(news_analyst)],
    sub_agents=[
        funny_nerd,
        stock_analyst,
    ]
)