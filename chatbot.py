import streamlit as st
from database import save_chat_history, get_chat_history
import requests
import config

def chatbot():
    st.title("Medical Chatbot")

    username = st.session_state.get("username", "unknown_user")
    
    # Sidebar for model selection
    st.sidebar.title("Model Selection")
    selected_model = st.sidebar.selectbox(
        "Select a Model:",
        ["Q/A", "Medical Document Summarization", "Conversation Interpretation"]
    )

    # Get the appropriate API URL
    api_url = config.API_URLS[selected_model]

    st.subheader("Chat")
    user_input = st.text_input("Type your message here...")

    if st.button("Send"):
        # Save user input to chat history
        save_chat_history(username, user_input)
        st.session_state.conversation_history.append({"role": "user", "content": user_input})

        # Prepare the correct payload
        payload = {"question": user_input}  # Adjust to match API needs
        
        try:
            # Send the request
            response = requests.post(api_url, json=payload)
            
            # Debugging: Check if response is empty
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    bot_response = response_data.get("answer", "No response generated.")
                except ValueError:
                    bot_response = "Error: Received non-JSON response from the server."
            else:
                bot_response = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            bot_response = f"Error: {str(e)}"

        # Save and display bot response
        save_chat_history(username, bot_response)
        st.session_state.conversation_history.append({"role": "bot", "content": bot_response})

        # Display conversation
        for entry in st.session_state.conversation_history:
            st.write(f"{entry['role']}: {entry['content']}")

    if st.button("Show Chat History"):
        chat_history = get_chat_history(username)
        st.subheader("Chat History")
        for message, timestamp in chat_history:
            st.write(f"{timestamp}: {message}")
