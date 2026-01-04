# STEP 1: Setup API key for Groq, OpenAI and Tavily

import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# STEP 2: Setup LLM and Tools

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# Define model names
MODEL_NAMES = {
    "groq": [
        "llama-3.3-70b-versatile",
        "mistral-saba-24b",
        "llama-3.1-8b-instant",
        "groq/compound-mini"
    ],
    "openai": [
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-3.5-turbo"
    ]
}

# Create instances

openai_llm = [ChatOpenAI(model=name) for name in MODEL_NAMES["openai"]]
groq_llm = [ChatGroq(model = name) for name in MODEL_NAMES['groq']]

search_tool = TavilySearchResults(max_result=3)

# STEP 3: Create AI Agent with Search tool functionality

from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly. Use the tools given to you to answer user queries."


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model = llm_id)

    tools = [TavilySearchResults(max_result=3)] if allow_search else []

    agent = create_agent(
        model = llm,
        tools = tools,
        system_prompt = system_prompt
    )

    # STEP 4: Test the AI Agent with a user query

    # query = "What are the latest advancements in AI technology?"

    state = {"messages": query}
    response = agent.invoke(state)

    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]