import streamlit as st
from login import login
from chatbot import chatbot

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Check if the user is authenticated
if not st.session_state.authenticated:
    login()  # Show the login page
else:
    chatbot()  # Show the chatbot page
