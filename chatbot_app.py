import streamlit as st
from chatbot import qa_interface, summarization_interface, interpret_interface


def chatbot():
    # Sidebar for feature selection
    st.sidebar.title("Features")
    selected_feature = st.sidebar.selectbox(
        "Select a feature:",
        ["Q/A", "Medical Document Summarization", "Conversation Interpretation"]
    )

   
  

    # Route to respective module
    if selected_feature == "Q/A":
        qa_interface()
    elif selected_feature == "Medical Document Summarization":
        summarization_interface()
    elif selected_feature == "Conversation Interpretation":
        interpret_interface()
