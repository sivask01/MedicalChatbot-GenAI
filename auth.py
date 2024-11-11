import streamlit as st
from database import register_user, authenticate_user

def login():
    st.title("Login to Access the Chatbot")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.experimental_set_query_params(logged_in="true")
            st.rerun()
        else:
            st.error("Invalid username or password.")

def signup():
    st.title("Sign Up for the Healthcare Chatbot")

    name_disclosure = st.checkbox("I don't want to include my name")
    if not name_disclosure:
        name = st.text_input("Full Name")
    else:
        name = None

    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    st.subheader("Health Information")
    height = st.number_input("Height (in cm)", min_value=0.0, step=0.1)
    weight = st.number_input("Weight (in kg)", min_value=0.0, step=0.1)
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", ["Male", "Female", "Other", "Prefer not to say"])
    health_conditions = st.text_area("Any concerning health conditions?")
    smoking_status = st.checkbox("Do you smoke?")
    alcohol_consumption = st.checkbox("Do you consume alcohol?")

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        elif register_user(name or username, username, password, height, weight, age, sex, health_conditions, smoking_status, alcohol_consumption):
            st.success("Account created successfully! Please log in.")
        else:
            st.error("Username already exists. Please choose a different username.")
