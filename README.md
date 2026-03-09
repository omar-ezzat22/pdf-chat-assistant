# 📄 PDF Chat Assistant (Modular RAG System)

A robust Retrieval-Augmented Generation (RAG) web application built with Streamlit and LangChain. This tool allows users to upload any PDF document and interactively ask questions about its content. The project is structured modularly to separate the frontend UI from the backend AI logic.

## 🚀 Features
* **PDF Document Processing:** Extracts text from uploaded PDF files securely and efficiently.
* **Intelligent Chunking:** Utilizes Recursive Character Text Splitting with overlap to maintain contextual integrity.
* **Vector Search Engine:** Employs FAISS for rapid and accurate similarity search.
* **Powered by Gemini:** Integrates Google's `gemini-2.5-flash` for generation and `gemini-embedding-001` for vector embeddings.
* **Modular Architecture:** Clean separation of concerns between the Streamlit UI and the LangChain processing logic.

## 🛠️ Tech Stack
* Python
* Streamlit
* LangChain
* FAISS
* PyPDF
* Google Gemini API

## ⚙️ Installation & Setup

1. Clone the repository:
git clone https://github.com/omar-ezzat22/pdf-chat-assistant.git
cd pdf-chat-assistant

2. Install the required dependencies:
pip install -r requirements.txt

3. Configure environment variables:
Create a .env file in the root directory and add your Google API key:
GOOGLE_API_KEY="your_api_key_here"

💻 Usage
Run the Streamlit application:
streamlit run main_app.py

1.Upload a PDF document using the sidebar.
2.Click the process button to build the vector database.
3.Ask questions about the document in the main chat interface.
