from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from chatbot.loader import load_documents

def build_chain(data_path, memory):
    documents = load_documents(data_path)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    custom_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a helpful assistant. Use ONLY the following context to answer the question.
If the answer is not contained in the context, respond with \"I'm sorry, I can't answer that based on the documents provided.\"

Context: {context}
Question: {question}
Answer:"""
    )

    return ConversationalRetrievalChain.from_llm(
        ChatOpenAI(temperature=0),
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": custom_prompt}
    )