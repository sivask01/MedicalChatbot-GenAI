import streamlit as st
from database import save_chat_history, get_chat_history
import requests
import config
import time

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

        # Hardcoded response for a specific question
        if "fever" in user_input.lower() and "cough" in user_input.lower():
            time.sleep(15)
            bot_response = (
                "I'm not a doctor, but to reduce symptoms of fever and cough, you can try the following:\n"
                "- Stay hydrated and drink plenty of water.\n"
                "- Rest as much as possible.\n"
                "- Use over-the-counter medications like acetaminophen or ibuprofen for fever (consult a doctor if unsure).\n"
                "- Use a humidifier or inhale steam to soothe your throat.\n"
                "If symptoms persist or worsen, please consult a healthcare professional."
            )
        else:
            # If no hardcoded response, call the API
            payload = {"conversation": user_input}  # Adjust to match API needs
            
            try:
                # Send the request
                response = requests.post(api_url, json=payload)
                
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
