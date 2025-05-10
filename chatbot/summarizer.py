import streamlit as st
import requests
import fitz  # PyMuPDF
import config

def summarization_interface():

    st.markdown("### 🗂️ Conversation History")
    chat_container = st.container()
    for entry in st.session_state.conversation_history:
        with chat_container:
            if entry["role"] == "user":
                st.markdown(f"**🧑 You:** {entry['content']}")
            else:
                st.markdown(f"**🤖 Bot:** {entry['content']}")
        st.subheader("Upload a document or paste text to summarize:")

    uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])
    input_text = st.text_area("Or paste medical text here")

    text_to_summarize = ""

    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            for page in doc:
                text_to_summarize += page.get_text()
        elif uploaded_file.type == "text/plain":
            text_to_summarize = uploaded_file.read().decode("utf-8")
    elif input_text.strip():
        text_to_summarize = input_text.strip()

    if text_to_summarize:
        if st.button("Summarize"):
            response = requests.post(config.API_URLS["Medical Document Summarization"], json={"text": text_to_summarize})
            if response.status_code == 200:
                summary = response.json().get("summary", "No summary generated.")
                st.markdown(f"📝 **Summary:**\n\n{summary}")
            else:
                st.error(f"Backend Error: {response.status_code}")
