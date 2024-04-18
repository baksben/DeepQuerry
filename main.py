import os
import streamlit as st
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import SeleniumURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from secret_key import openapi_key

from dotenv import load_dotenv
load_dotenv()

st.title("News Research Tool 👩🏻‍💻")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)
chain = None
file_path = "vectorstore.pkl"  # Define the file path for the FAISS index

if process_url_clicked:
    loader = SeleniumURLLoader(urls=urls)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter....Started....✅✅✅")
    docs = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building....✅✅✅")
    
    # Save the vectorstore to a local file
    vectorstore_openai.save_local(file_path)

    # Load the vectorstore from local file
    vectorstore = FAISS.load_local(file_path, embeddings, allow_dangerous_deserialization=True)
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

query = main_placeholder.text_input("Question: ")
if query and chain:
    result = chain({"question": query}, return_only_outputs=True)
    st.header("Answer")
    st.write(result["answer"])

    # Display sources, if available
    sources = result.get("sources", "")
    if sources:
        st.subheader("Sources:")
        sources_list = sources.split("\n")
        for source in sources_list:
            st.write(source)
else:
    st.write("Please process URLs first to initialize the system.")
