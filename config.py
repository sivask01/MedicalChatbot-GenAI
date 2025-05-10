# Configurations for the Medical Chatbot App

# App Title
APP_TITLE = "GenAI Driven Medical Chatbot"

# UI Texts
LOGIN_TITLE = "Access the Chatbot"
USERNAME_PLACEHOLDER = "Username"
PASSWORD_PLACEHOLDER = "Password"
LOGIN_BUTTON_TEXT = "Access Chatbot"
LOGOUT_BUTTON_TEXT = "Logout"
SEND_BUTTON_TEXT = "Send"
QUESTION_PLACEHOLDER = "Type your message here..."

# === API Configuration ===

# Choose the environment: "local", "ngrok", "prod"
ENV = "ngrok"

# Define the base URLs for each environment
BASE_API_URLS = {
    "local": "http://127.0.0.1:8050",
    "ngrok": "https://3a5a-35-225-63-245.ngrok-free.app/"
    
}

# Use the current environment's base URL
BASE_API_URL = BASE_API_URLS[ENV]

# API endpoints for each feature
API_URLS = {
    "Q/A": f"{BASE_API_URL}/qa",
    "Medical Document Summarization": f"{BASE_API_URL}/summarize",
    "Conversation Interpretation": f"{BASE_API_URL}/conv_interpretation"
}
