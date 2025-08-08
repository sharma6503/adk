from ddtrace.llmobs import LLMObs
from ddtrace import patch_all

def load_dd_config():
    """Load the dd_config module to configure LLMObs."""
    LLMObs.enable(
        ml_app="adk",
        api_key="996c2de99a04c6f6b5ed8e05342e37f1",
        site="datadoghq.com",
        agentless_enabled=True,
    )
    patch_all(llmobs=True)