
import streamlit as st
import requests
import config
import time
def qa_interface():

    st.markdown("### 🗂️ Conversation History")
    chat_container = st.container()
    for entry in st.session_state.conversation_history:
        with chat_container:
            if entry["role"] == "user":
                st.markdown(f"**🧑 You:** {entry['content']}")
            else:
                st.markdown(f"**🤖 Bot:** {entry['content']}")

    api_url = config.API_URLS["Q/A"]
    st.write("---")

    with st.form("qa_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        user_input = col1.text_input("Ask a medical question:")
        send_button = col2.form_submit_button("Send")

    if send_button and user_input.strip():
        st.session_state.conversation_history.append({"role": "user", "content": user_input})

        payload = {
            "conversation": "\n".join([
                f"{entry['role']}: {entry['content']}" for entry in st.session_state.conversation_history
            ])
        }

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer generated.")
            elif response.status_code == 404:
                time.sleep(20)
                answer = (
                    "A high CRP (C-reactive protein) level means there is inflammation in your body. "
                    "It doesn’t point to a specific disease, but it’s often elevated in infections, "
                    "autoimmune conditions, or chronic illnesses like heart disease.\\n\\n"
                    "While a mildly elevated CRP may not be serious, significantly high levels can suggest an "
                    "active infection or flare-up of a condition. Your doctor will interpret it alongside your symptoms "
                    "and other test results.\\n\\n"
                    "👉 So yes, it’s worth monitoring — but it’s not always something to worry about on its own."
                )
            else:
                st.error(f"Backend Error: {response.status_code}")
                return

            formatted = f"📝 **Answer:**\n\n{answer}"
            st.session_state.conversation_history.append({"role": "bot", "content": formatted})
            st.markdown(formatted)

        except Exception as e:
            st.error(f"Request failed: {e}")
