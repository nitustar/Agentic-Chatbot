# Step 1: Setup UI with Stremlit (model provider, model, system_prompt, web_search, query)
# StreamLit Run command -> streamlit run .\frontend.py

import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="wide")
st.title("AI Chatbot Agent")
st.write("Create and Interact with AI Agents!")

MODEL_NAMES = {
    "Groq": {
        "text": ["mistral-saba-24b", "llama-3.3-70b-versatile", "llama-3.1-8b-instant", "groq/compound-mini"],
    },
    "OpenAI": {
        "text": ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo",],
    }
}

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    
    system_prompt = st.text_area(
        "Define your AI Agent:", 
        height=100, 
        placeholder="Write your system prompt here...",
        value="Act as an AI chatbot who is smart and friendly. Analyze images when provided and answer questions accurately."
    )
    
    provider = st.radio("Select Provider:", ("Groq", "OpenAI"))
    
    available_models = MODEL_NAMES[provider]["text"]
    
    selected_model = st.selectbox(f"Select {provider} Model:", available_models)
    
    allow_web_search = st.checkbox("Allow Web Search")
    
    # if allow_web_search:
    #     st.warning("⚠️ Web search disabled when using images")

# Main content area
col1, col2 = st.columns([1, 1])


with col1:
    st.subheader("Your Query")
    user_query = st.text_area(
        "Enter your query:", 
        height=100, 
        placeholder="Ask anything. If you upload images, you can ask questions about them!"
    )
    

API_URL = "http://127.0.0.1:8000/chat"

with col2:
    st.subheader("Agent Response")
    
    if st.button("Ask Agent!", use_container_width=True):
        if user_query.strip():
            with st.spinner("🔄 Processing your request..."):
                
                payload = {
                    "model_name": selected_model,
                    "model_provider": provider,
                    "system_prompt": system_prompt,
                    "messages": [user_query],
                    "allow_search": allow_web_search,
                }
                
                try:
                    response = requests.post(API_URL, json=payload, timeout=120)
                    
                    if response.status_code == 200:
                        response_data = response.json()
                        st.success("Response received!")
                        print(response_data)
                        st.markdown(str(response_data))
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                
                except requests.exceptions.Timeout:
                    st.error("Request timed out. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("Could not connect to backend. Make sure server is running.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a query before submitting.")

