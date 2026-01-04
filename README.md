# 🤖 LangGraph AI Agent (FastAPI + Streamlit)

A **full-stack AI chatbot application** built using **LangChain/LangGraph**, **FastAPI**, and **Streamlit**. This project demonstrates how to dynamically create AI agents using **Groq** and **OpenAI** models, optionally enhanced with **web search (Tavily)**, and expose them via a REST API with a simple interactive UI.

---

## 🚀 Features

* 🔁 **Dynamic LLM selection** (Groq / OpenAI)
* 🧠 **Agent-based architecture** using LangGraph
* 🌐 **Optional Web Search** with Tavily
* ⚡ **FastAPI backend** for scalable API access
* 🎨 **Streamlit frontend** for interactive UI
* 🔐 Environment-based API key management
* 📜 Swagger UI support for API testing

---

## 🧩 Tech Stack

* **Python 3.9+**
* **LangChain / LangGraph**
* **FastAPI**
* **Streamlit**
* **Groq LLMs** (LLaMA / Mixtral)
* **OpenAI GPT Models**
* **Tavily Search API**

---

## 📁 Project Structure

```text
├── ai_agent.py        # Core AI agent logic using LangGraph
├── backend.py         # FastAPI backend exposing /chat endpoint
├── frontend.py        # Streamlit-based UI
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/langgraph-ai-agent.git
cd langgraph-ai-agent
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file or export variables directly:

```bash
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Running the Application

### 🧠 Start Backend (FastAPI)

```bash
python backend.py
```

* API will run at: `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`

---

### 🎨 Start Frontend (Streamlit)

```bash
streamlit run frontend.py
```

* UI will open at: `http://localhost:8501`

---

## 🔌 API Usage

### **POST** `/chat`

Interact with the AI Agent via REST API.

#### Request Body

```json
{
  "model_name": "gpt-4o-mini",
  "model_provider": "OpenAI",
  "system_prompt": "You are a helpful AI assistant",
  "messages": ["Explain FastAPI in simple terms"],
  "allow_search": true
}
```

#### Response

```json
"FastAPI is a modern Python web framework designed for building APIs quickly and efficiently..."
```

---

## 🤖 Supported Models

### Groq

* `mixtral-8x7b-32768`
* `llama-3.3-70b-versatile`
* `llama-4-scout-17b-16e-instruct`

### OpenAI

* `gpt-4o-mini`

---

## 🧠 How It Works

1. **Frontend (Streamlit)** collects user input
2. Request is sent to **FastAPI backend**
3. Backend validates request using **Pydantic**
4. **LangGraph agent** is created dynamically
5. Optional **Tavily web search** is added as a tool
6. Agent invokes selected LLM
7. Final response is returned to UI

---

## 📌 Use Cases

* AI Chatbot platforms
* LLM experimentation playground
* Learning LangGraph & agent tooling
* Backend + Frontend AI integration demo

---

## 🧑‍💻 Author

**Nitesh Kumar**
Python Developer | AI & Backend Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub and feel free to contribute!

---

Happy Coding 🚀
