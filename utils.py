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


import streamlit as st

def add_header():
    st.markdown("""
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-top: 10px;
    }

    .subheader {
        font-size: 16px;
        font-weight: normal;
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }

    </style>
    <div class="header">🩺 Medical Assistant using Generative AI 🤖</div>
    <div class="subheader">Simplifying Medical Information through Summarization, Q&A, and Interpretation</div>
    """, unsafe_allow_html=True)

def add_footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #6c757d;
        text-align: center;
        padding: 10px 0;
        font-size: 13px;
        z-index: 9999;
    }
    </style>
    <div class="footer">
        Developed by G37 Team, CMPE 295 · San José State University ·
        <a href='https://github.com/sivask01/MedicalChatbot-GenAI' target='_blank'>🐙 Source Code</a> · Advised by Prof. Magdalini Eirinaki
    </div>
    """, unsafe_allow_html=True)

   