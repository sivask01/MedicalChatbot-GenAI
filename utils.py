import streamlit as st

# Dummy credentials for demonstration purposes
USER_CREDENTIALS = {
    "user1": "password123",
    "user2": "password456"
}

def login():
    st.title("Login to Access the Chatbot")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Button to log in
    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Refresh the page to show the chatbot
        else:
            st.error("Invalid username or password. Please try again.")
