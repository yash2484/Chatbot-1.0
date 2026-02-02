# chatbot/chatbot.py

from config import (
    LLM_PROVIDER,
    OLLAMA_MODEL,
    OPENAI_MODEL,
    FAISS_INDEX_PATH,
    EMBEDDING_MODEL,
    TOP_K
)

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


def get_qa_chain():
    #LLM
    if LLM_PROVIDER == "ollama":
        from langchain_community.llms import Ollama
        llm = Ollama(model=OLLAMA_MODEL)

    elif LLM_PROVIDER == "openai":
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model=OPENAI_MODEL)

    else:
        raise ValueError("Invalid LLM_PROVIDER")

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # Vector Store
    vectorstore = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    # Memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful assistant.
Answer ONLY using the context below.
If the answer is not present, say:
"This is not part of the documents."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # Chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return chain
