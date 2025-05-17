import streamlit as st
from agent import agent

st.title("🤖 Customer Support Agent")

query = st.text_input("Ask a question:")

if query:
    response = agent.run(query)
    st.write(response)
