from ddtrace.llmobs.decorators import llm

import google.generativeai as genai

from ddtrace.llmobs import LLMObs

LLMObs.enable(
        ml_app="adk",
        api_key="996c2de99a04c6f6b5ed8e05342e37f1",
        site="datadoghq.com",
        agentless_enabled=True,
    )





@llm(model_name="gemini", name="invoke_llm", model_provider="google")

def llm_call(question_prompt):

    genai.configure(api_key="AIzaSyCJk8tLiSf73HpmbnEz9-ozOFbsdcAFsWc")

    gemini_model=genai.GenerativeModel(
    "gemini-2.5-flash")



    LLMObs.annotate(

        input_data=question_prompt,

    )

    response=gemini_model.generate_content(question_prompt)

    print(response.candidates[0].content.parts)

    LLMObs.annotate(

    output_data=response.candidates[0].content.parts[0].text,

    )

    return response

print(llm_call("What is the capital of France?"))