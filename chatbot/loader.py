from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from pathlib import Path

def load_documents(folder_path):
    docs = []
    for file in Path(folder_path).glob("*"):
        if file.suffix == ".pdf":
            docs.extend(PyPDFLoader(str(file)).load())
        elif file.suffix == ".txt":
            docs.extend(TextLoader(str(file)).load())
        elif file.suffix == ".docx":
            docs.extend(Docx2txtLoader(str(file)).load())
    return docs