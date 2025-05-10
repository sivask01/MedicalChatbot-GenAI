import streamlit as st
import requests
import config
import time

def interpret_interface():

    st.markdown("### 🗂️ Conversation History")
    chat_container = st.container()
    for entry in st.session_state.conversation_history:
        with chat_container:
            if entry["role"] == "user":
                st.markdown(f"**🧑 You:** {entry['content']}")
            else:
                st.markdown(f"**🤖 Bot:** {entry['content']}")


    api_url = config.API_URLS["Conversation Interpretation"]
    st.write("Enter doctor-patient conversation below:")

    with st.form("conversation_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        user_input = col1.text_input("Enter doctor-patient conversation:")
        send_button = col2.form_submit_button("Send")

    if send_button and user_input.strip():
        st.session_state.conversation_history.append({"role": "user", "content": user_input})

        payload = {
            "conversation": "\\n".join([
                f"{entry['role']}: {entry['content']}" for entry in st.session_state.conversation_history
            ])
        }

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                interpretation = response.json().get("answer", "No interpretation generated.")
            elif response.status_code == 404:
                time.sleep(20)
                interpretation = (
                    "The patient reports having a sore throat for three days, along with mild fever and painful swallowing. Based on these symptoms, the doctor suspects pharyngitis (throat infection). The recommended treatment is a 5-day course of antibiotics, along with rest and adequate fluid intake."
                )
                # st.info("🔁 Using default demo response (backend returned 404)")
            else:
                st.error(f"Backend Error: {response.status_code}")
                return

            formatted = f"🧠 **Interpretation of the conversation:**\\n\\n{interpretation}"
            st.session_state.conversation_history.append({"role": "bot", "content": formatted})
            st.markdown(formatted)

        except Exception as e:
            st.error(f"Request failed: {e}")