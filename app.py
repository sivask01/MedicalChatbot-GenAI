import streamlit as st
from auth import login, signup
from chatbot import chatbot

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Add a navigation option for Login and Sign-Up
if not st.session_state.authenticated:
    page = st.sidebar.radio("Select Page", ["Login", "Sign-Up"])

    if page == "Login":
        login()
    elif page == "Sign-Up":
        signup()
else:
    chatbot()  # Show the chatbot page
