# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain import HuggingFaceHub
import streamlit as st

st.title("🦜🔗")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.2", model_kwargs={"temperature":0.8, "max_length":200})

    response = llm(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})