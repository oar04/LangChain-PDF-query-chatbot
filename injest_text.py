#from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

import os
if os.path.exists("env.py"):
    import env

pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION")
              )

def injest_text():
    loader = PyPDFDirectoryLoader("pdfs")
    documents = loader.load()
    print("Loaded text.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    document = text_splitter.split_documents(documents)
    print(f"Split documents into {len(document)} chunks.")

    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(
        documents = document,
        embedding = embeddings,
        index_name = "ccc-publications"
    )

    print("Successfully loaded documents into Pinecone.")

if __name__ == "__main__":
    injest_text()

