# === config.py ===
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Model settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")  
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Embeddings model
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")


# Chunking params
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

# Retrieval
TOP_K = int(os.getenv("TOP_K", 5))
