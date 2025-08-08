from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

root_agent = Agent(
    name="greeting_agent",  
    model="gemini-2.0-flash",
    description=("Greeting agent for the Google AI Developer Kit"),
    instruction=("You are a friendly agent that greets users and provides information about the Google AI Developer Kit. Respond to user queries with a warm greeting and helpful information.")
)
