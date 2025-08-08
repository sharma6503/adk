import os,random

from google.adk.agents import Agent
from google.adk.models import lite_llm

model=lite_llm(
    model_name="google/gemini-2.0-flash",
    api_key=os.getenv("OPENROUTER_API_KEY"))

def get_dad_joke() -> str:
    """
    Returns a random dad joke.
    """
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I used to play piano by ear, but now I use my hands.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!"
    ]
    return random.choice(jokes)


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="An agent that tells dad jokes and provides information about the Google AI Developer Kit.",
    instructions="You are a dad joke telling agent. Respond to all queries with a dad joke. If the user asks for information about the Google AI Developer Kit, provide a dad joke related to it.",
    tools=[]
)