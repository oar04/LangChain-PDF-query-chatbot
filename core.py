from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain #retrievalqa
import streamlit as st

import pinecone

import os
if os.path.exists("env.py"):
    import env

pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION")
              )
def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    human_prompt = st.session_state.human_prompt
    st.session_state.history.append(human_prompt)

initialize_session_state()

st.title("LangChain Climate Co-Pilot")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with chat_placeholder:
    for chat in st.session_state.history:
        st.markdown(chat)

with prompt_placeholder:
    st.markdown("Lets Chat!")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat", value = "Hi", label_visibility="collapsed", key="human_prompt"
    )
    cols[1].form_submit_button(
        "Submit", type="primary", on_click=on_click_callback
    )

def run_llm():
    embeddings = OpenAIEmbeddings()

    doc_search = Pinecone.from_existing_index(
        index_name = "ccc-publications",
        embedding = embeddings
    )

    chat_model = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 1, verbose = True)

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=doc_search.as_retriever()
    )

    chat_history = []

    print("Start a conversation with me about climate change!")

    while True:
        query = input("You: ")
        if query == "quit":
            break
        response = qa({"question": query, "chat_history": chat_history})
        print(f"Response: {response.get('answer')}")
        chat_history.append((query, str(response)))
    #return qa({"query": query})