# 🦜️🔗LangChain Climate Co-Pilot

LangChain Climate Co-Pilot is a Python-based chatbot project that helps users interact with PDF documents from the Climate Control Committee. It processes PDFs and stores them in a Pinecone vector database. Additionally, it provides a command-line chatbot interface powered by the OpenAI API.

## Prerequisites

Before using this project, make sure you have the following Python modules installed:

- [openai](https://pypi.org/project/openai/)
- [tiktoken](https://pypi.org/project/tiktoken/)
- [pinecone-client](https://pypi.org/project/pinecone-client/)
- [langchain](https://pypi.org/project/langchain/)

You can install these modules using pip:

pip install openai tiktoken pinecone-client langchain

## Getting Started

1. **Clone the LangChain Climate Co-Pilot repository to your local machine:**
   git clone https://github.com/oar04/LangChain-PDF-query-chatbot.git
   
2. **Edit the "pdfs" directory in the project folder and place the PDFs you want to process in it.**
   This has already been pre-populated with relavent documents

3. **Configure your Pinecone API key.**
   You can obtain your API key by signing up for Pinecone at https://www.pinecone.io/.

4. **Configure your OpenAI API key.**
   You can obtain your API key by signing up for OpenAI at https://openai.com/product.

5. **Add the keys and other relavent details into env.py**

6. **Run the script to process the PDFs and store them in Pinecone:**
   python injest_text.py

7. **Run the script to start the chat:**
   python main.py

The chatbot will prompt you for commands and respond to your queries based on the content of the processed PDFs.
You can interact with the chatbot to retrieve information from the PDF documents and ask questions related to climate control topics.
   
