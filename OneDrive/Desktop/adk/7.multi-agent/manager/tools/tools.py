from datetime import datetime
from ddtrace.llmobs.decorators import tool
from ddtrace.llmobs import LLMObs
from dd_config import load_dd_config

load_dd_config()


@tool(name="get_current_time", ml_app="adk")
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    LLMObs.annotate(
        input_data={
            'role': 'user',
            'content': "Get the current time"
        },
        output_data={
            'role': 'assistant',
            'content': {
                "status": "success",
                "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }}

    )
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }