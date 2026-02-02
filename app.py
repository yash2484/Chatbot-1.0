import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Try importing with error handling
from chatbot.ragchain import build_chain
from chatbot.memory import get_memory

load_dotenv()  # Load environment variables from .env

st.set_page_config(page_title="Doc Chatbot", layout="wide")
st.title("📄 Document Chatbot")

# Backend documents directory 
DATA_PATH = "documents"  

# Check for existing documents
def get_document_files():
    """Get all supported document files from the documents directory"""
    supported_extensions = ['.pdf', '.txt', '.docx']
    files = []
    if os.path.exists(DATA_PATH):
        for file in os.listdir(DATA_PATH):
            if any(file.lower().endswith(ext) for ext in supported_extensions):
                files.append(file)
    return files

# Display available documents in sidebar
document_files = get_document_files()
if document_files:
    st.sidebar.header("📚 Available Documents")
    st.sidebar.write(f"Found {len(document_files)} document(s):")
    for file in document_files:
        st.sidebar.write(f"• {file}")
else:
    st.sidebar.header("📚 No Documents Found")
    st.sidebar.warning(f"Please add PDF, TXT, or DOCX files to the '{DATA_PATH}' directory.")
    st.sidebar.info("Supported formats: PDF, TXT, DOCX")

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = None

# Initialize chat chain if documents are available
if document_files and st.session_state.chat_chain is None:
    try:
        with st.spinner("Initializing chat system with documents..."):
            memory = get_memory()
            st.session_state.chat_chain = build_chain(DATA_PATH, memory)
        st.success(f"Chat system initialized with {len(document_files)} document(s)!")
    except Exception as e:
        st.error(f"Error initializing chat system: {str(e)}")

# Chat Interface
if st.session_state.chat_chain is not None and document_files:
    st.subheader("💬 Chat with Your Documents")
    
    # Use a form to handle input properly
    with st.form(key="chat_form", clear_on_submit=True):
        query = st.text_input("Ask a question about your documents:", placeholder="What would you like to know?")
        submit_button = st.form_submit_button("Send")
    
    if submit_button and query and query.strip():
        try:
            # Add user query to history first
            st.session_state.chat_history.append(("user", query))
            
            # Get response from chain
            with st.spinner("Searching through documents..."):
                result = st.session_state.chat_chain.run(query)
            
            # Add bot response to history
            st.session_state.chat_history.append(("assistant", result))
            
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")
            st.session_state.chat_history.append(("assistant", f"Sorry, I encountered an error: {str(e)}"))

elif not document_files:
    st.info(f"📄 Please add documents to the '{DATA_PATH}' directory to start chatting!")
    st.markdown("""
    **Instructions:**
    1. Create a folder named `documents` in your project directory
    2. Add your PDF, TXT, or DOCX files to this folder
    3. Restart the application
    4. Start asking questions about your documents!
    """)
else:
    st.info("Initializing chat system... Please wait.")

# Display chat history
if st.session_state.chat_history:
    st.subheader("📝 Chat History")
    for role, message in st.session_state.chat_history:
        st.chat_message(role).markdown(message)

# Sidebar controls
st.sidebar.markdown("---")
st.sidebar.header("🔧 Controls")

# Add a button to clear chat history
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()

# Add a button to refresh documents and reset system
if st.sidebar.button("🔄 Refresh Documents"):
    st.session_state.chat_chain = None
    st.session_state.chat_history = []
    st.rerun()

# Add information section
st.sidebar.markdown("---")
st.sidebar.header("ℹ️ How to Use")
st.sidebar.markdown("""
1. **Add Documents**: Place PDF, TXT, or DOCX files in the `documents` folder
2. **Refresh**: Click 'Refresh Documents' if you add new files
3. **Ask Questions**: Type your questions in the chat input
4. **Clear History**: Use the clear button to start fresh
""")
