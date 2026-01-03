# Step 1: Setup Pydentic model (Schema Validation)
# FastAPI Run Command -> python backend.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool = False

# Step 2: Setup AI Agent for Frontend Request(Integration with FastAPI)

ALLOWED_MODEL_NAME = ["llama3-70b-8192", "mixtral-8x7b-32768", "gpt-4o-mini", "llama-3.3-70b-versatile", "llama-4-scout-17b-16e-instruct"]

app = FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot with LangGraph and search tools.
    It dynamically selects the model specified in the request
    """

    if request.model_name not in ALLOWED_MODEL_NAME:
        return {"error": "Invalid model name. Kindly choose a valid AI model."}
    
    llm_id = request.model_name
    provider = request.model_provider
    system_prompt = request.system_prompt
    query = request.messages
    allow_search = request.allow_search

    # Create AI Agent and get response from it.

    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)

    return response

# Step 3: Run app and explore Swagger UI Docs

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)