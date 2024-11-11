import streamlit as st
import config

# Dummy credentials for demonstration purposes
USER_CREDENTIALS = {
    "user1": "password123",
    "user2": "password456"
}

def login():
    st.title(config.LOGIN_TITLE)

    # Input fields for username and password with placeholders from config
    username = st.text_input(config.USERNAME_PLACEHOLDER)
    password = st.text_input(config.PASSWORD_PLACEHOLDER, type="password")

    # Button to log in
    if st.button(config.LOGIN_BUTTON_TEXT):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            # Instead of a page redirect, we conditionally render the chatbot in app.py
            st.set_query_params(logged_in="true")  # This refreshes the app to show the chatbot interface
        else:
            st.error("Invalid username or password. Please try again.")
