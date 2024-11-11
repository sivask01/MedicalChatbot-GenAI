import streamlit as st
import requests
import config

def chatbot():
    # Sidebar for feature selection
    st.sidebar.title("Features")
    selected_feature = st.sidebar.selectbox(
        "Select a feature:", 
        ["Q/A", "Medical Document Summarization", "Conversation Interpretation"]
    )

    # Get the API URL from config based on the selected feature
    api_url = config.API_URLS[selected_feature]

    # Streamlit UI for the chatbot
    st.title(config.APP_TITLE)

    # Display the conversation history at the top
    st.subheader("Conversation:")
    chat_container = st.container()  # Container to hold the conversation

    with chat_container:
        for entry in st.session_state.conversation_history:
            if entry["role"] == "user":
                st.markdown(f"**You:** {entry['content']}")
            else:
                st.markdown(f"**Bot:** {entry['content']}")

    # Divider for better separation
    st.write("---")

    # Static input area with the "Send" button
    col1, col2 = st.columns([4, 1])
    with col1:
        question = st.text_input(config.QUESTION_PLACEHOLDER, key="question_input")
    with col2:
        send_button = st.button(config.SEND_BUTTON_TEXT)

    # Process the input when the "Send" button is clicked
    if send_button and question:
        # Add the question to the conversation history
        st.session_state.conversation_history.append({"role": "user", "content": question})

        # Prepare the input for the API, including the conversation history
        conversation_text = "\n".join(
            [f"{entry['role']}: {entry['content']}" for entry in st.session_state.conversation_history]
        )

        # Send the request to the selected API
        if selected_feature == "Q/A":
            response = requests.post(api_url, json={"conversation": conversation_text})
        elif selected_feature == "Medical Document Summarization":
            response = requests.post(api_url, json={"text": question})  # Assuming summarization expects "text"
        elif selected_feature == "Conversation Interpretation":
            response = requests.post(api_url, json={"conversation": conversation_text})

        # Handle the response
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer generated.")  # Update key based on API response
            # Add the answer to the conversation history
            st.session_state.conversation_history.append({"role": "bot", "content": answer})
        else:
            st.error(f"Error in generating the answer. Status Code: {response.status_code}")
