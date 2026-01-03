# Step 1: Setup UI with Stremlit (model provider, model, system_prompt, web_search, query)
# StreamLit Run command -> streamlit run .\frontend.py
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("AI Chatbot Agent")
st.write("Create and Interact with AI Agents!")

system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Write your system prompt here...")

MODEL_NAME_GROQ = ["mixtral-8x7b-32768", "llama-3.3-70b-versatile", "llama-4-scout-17b-16e-instruct"]
MODEL_NAME_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider: ", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model: ", MODEL_NAME_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model: ", MODEL_NAME_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query ", height=70, placeholder="Ask Anything.")

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
    # Get response form backend and show here.
        # Step 2: Connect with backend via URL.
        import requests

        payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
                }

        response = requests.post(API_URL, json=payload)
        # response = "Hi, this is a fixed dummy response!"
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"]) 
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
