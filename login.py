import streamlit as st
import config

# Dummy credentials for demonstration purposes
USER_CREDENTIALS = {
    "user1": "password123",
    "user2": "password456"
}

def login():
    # st.title(config.LOGIN_TITLE)

    # Input fields for username and password with placeholders from config
    username = st.text_input(config.USERNAME_PLACEHOLDER)
    password = st.text_input(config.PASSWORD_PLACEHOLDER, type="password")

    # Button to log in
    if st.button(config.LOGIN_BUTTON_TEXT):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            # Instead of a page redirect, we conditionally render the chatbot in app.py
            # st.set_query_params(logged_in="true")  # This refreshes the app to show the chatbot interface
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")


def signup():
   

    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    st.markdown("### 👤 Demographic Information")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Prefer not to say", "Female", "Male", "Other"])
    medical_history = st.multiselect(
        "Medical History (Optional)", 
        ["Hypertension", "Diabetes", "Asthma", "Heart Disease", "None"]
    )

    if st.button("Sign Up"):
        if new_password != confirm_password:
            st.warning("🚫 Passwords do not match.")
        elif new_username in st.session_state.USER_CREDENTIALS:
            st.warning("🚫 Username already exists.")
        else:
            # Save user credentials
            st.session_state.USER_CREDENTIALS[new_username] = new_password

            # Store demographics in session (or later save to file/db)
            st.session_state[f"user_meta_{new_username}"] = {
                "age": age,
                "gender": gender,
                "history": medical_history
            }

            st.success("🎉 Account created! You can now log in.")
