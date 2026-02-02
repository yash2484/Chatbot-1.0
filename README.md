# RAG-based Chatbot using LangChain

## 🚀 Overview
This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that answers user queries using custom documents.  
It combines **document retrieval** with **LLM-based response generation** to produce grounded, context-aware answers.

The codebase is modular and structured to reflect **real-world GenAI system design** rather than a simple demo.

---

## 🧠 Problem Statement
Standard chatbots rely only on pretrained knowledge, which leads to hallucinations and outdated responses.  
This project addresses that limitation by:
- Retrieving relevant information from provided documents
- Injecting that context into the LLM prompt
- Generating responses strictly grounded in retrieved data

---

## 🏗️ High-Level Architecture
1. User submits a query
2. Documents are loaded and preprocessed
3. Text chunks are embedded and stored
4. Relevant chunks are retrieved using vector similarity
5. Retrieved context is passed to the LLM
6. Final response is generated and returned

---

## 🛠️ Tech Stack
- Python
- LangChain
- Large Language Models (LLMs)
- Vector Embeddings & Vector Stores
- Environment-based configuration

---

## 📂 Project Structure
2-Chatbot/
│
├── chatbot/
│ ├── loader.py # Document loading and preprocessing
│ ├── ragchain.py # Core RAG pipeline (retrieval + generation)
│ └── memory.py # Conversation memory management
│
├── documents/ # Source documents (structure tracked, contents ignored)
├── data/ # Processed data / embeddings (ignored in Git)
│
├── app.py # Application entry point
├── config.py # Centralized configuration
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md


---

## ⚙️ Setup & Execution

### 1️⃣ Clone the repository

git clone https://github.com/yash2484/Chatbot-1.0.git
cd Chatbot-1.0

### 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Configure environment variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here

### 5️⃣ Run the application
python app.py

## 📌 Key Features

End-to-end RAG pipeline using LangChain

Clean separation of retrieval, memory, and generation logic

Modular and extensible architecture

Production-style folder organization and Git hygiene

## 📈 Learnings & Outcomes

Built a complete Retrieval-Augmented Generation pipeline

Worked with document ingestion, chunking, embeddings, and retrieval

Designed a scalable GenAI system architecture

Applied professional Git and project structuring practices

## 🔮 Future Enhancements

Implement hybrid search (keyword + vector)

Add evaluation metrics for response quality
