# import streamlit as st
# from login import login
# from chatbot import chatbot

# # Initialize session state
# if "authenticated" not in st.session_state:
#     st.session_state.authenticated = False
# if "conversation_history" not in st.session_state:
#     st.session_state.conversation_history = []

# # Check if the user is authenticated
# if not st.session_state.authenticated:
#     login()  # Show the login page
# else:
#     chatbot()  # Show the chatbot page


import streamlit as st
from login import login
from chatbot_app import chatbot
import pandas as pd
import time
from utils import add_header, add_footer
from login import signup

add_header()
# -------- Session State Initialization --------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------- Navigation Sidebar --------
st.sidebar.title("Navigation")
page_choice = st.sidebar.radio("Go to", ["Home", "About", "Features", "Contact", "Sign Up", "Need My Access?"])
st.session_state.page = page_choice.lower().replace(" ", "_")

# Login / Logout toggle
if st.session_state.authenticated:
    current_time = time.time()
    login_time = st.session_state.get("login_time", current_time)
    elapsed = current_time - login_time

    if elapsed >= 60:
        if st.sidebar.button("Give me rest!!"):
            st.session_state.authenticated = False
            st.session_state.page = "need_my_access?"
            st.session_state.conversation_history = []
            st.rerun()

# -------- Page Routing --------
if st.session_state.page == "home":
   
    st.subheader("Empowering patients with understandable healthcare information")

    st.markdown("""
    🩺 **What is this project?**  
    This is an AI-powered chatbot designed to help patients understand complex medical documents, ask health-related questions, and interpret conversations with their doctors — even audio recordings.

    💡 **Why it matters**  
    Patients are often overwhelmed by medical jargon. This tool makes that information **clear, concise, and accessible** using cutting-edge AI models fine-tuned for real healthcare use cases.

    🔒 **Can you trust it?**  
    Yes. We built this system using:
    - Open-source models specialized for medicine
    - Post-processing filters to avoid hallucinated (fake) facts
    - Benchmarks against ChatGPT on 200+ medical questions
    - Usability and trust evaluation using the QUEST framework

    ⚡ **How fast is it?**  
    Most responses are returned in **under 1 minute** with high accuracy and readability.

    🧠 Built with: `MedQ-Llama3`, `MedSumm-BART`, `ConvInt-BART + Whisper`
                """)
    with st.expander("👤 Meet Krish — Our Test Persona"):           
   
        st.markdown("""
    - **Age:** 26  
    - **Role:** Graduate student in mechanical engineering
    - **Background:** Recently diagnosed with a chronic condition  
    - **Need:** Wants help understanding complex medical terms and reports  
    - **Challenge:** Often leaves the doctor’s office unsure of what was said  
    - **How he uses the chatbot:**
        1. Uploads his discharge report for simplification  
        2. Asks: *“What is CRP and why is mine high?”*  
        3. Pastes doctor notes for interpretation

    This persona helps us validate how well the chatbot works in a real-world scenario.

    """)
    with st.expander("Example Tests:"):    
        st.markdown("### 🩺 Document Summarization Example")
        st.code( '''
                Discharge Summary:

    The patient was admitted for evaluation of shortness of breath, fatigue, and elevated inflammatory markers. Notably, her CRP level was measured at 38 mg/L. A CT scan of the chest was unremarkable for pulmonary embolism, but mild bronchial thickening was observed. She was afebrile throughout her stay, and oxygen saturation remained above 96% on room air. Cardiology was consulted due to a family history of coronary artery disease. The ECG showed non-specific ST changes, but troponin levels remained within normal range.

    The patient was managed conservatively with hydration, monitoring, and supportive care. No antibiotics were administered due to the absence of clear infectious etiology. She was discharged in stable condition with outpatient follow-up scheduled with pulmonology and cardiology. Patient education included red flag signs and when to return to the ED.
                ''', language='text')

        st.markdown("### ❓ Medical Q&A Example")
        st.code("What does a high CRP level mean? Should I be worried?", language='text')

        st.markdown("### 🎙️ Conversation Interpretation Example")
        st.code('''
                Patient: I’ve had a sore throat for three days.  
    Doctor: Do you have any fever or trouble swallowing?  
    Patient: Yes, I have a mild fever, and it hurts when I swallow.  
    Doctor: Sounds like pharyngitis. I’ll prescribe a 5-day course of antibiotics and suggest rest and fluids.

                ''', language='text')
                

elif st.session_state.page == "about":
   

    st.markdown("""
    ### 🤖 MedQ-Llama3 (Q&A Model)
    - **Purpose:** Answer health-related questions like symptoms, medications, diagnosis  
    - **Tech:** Built on Bio-Medical-MultiModal-Llama-3-8B-V1 with structured prompt engineering  
    - **How to use:** Type your health question in the chat — e.g., “What is CRP and what does it indicate?”  
   

    ---

    ### 🧾 MedSumm-BART (Summarization Model)
    - **Purpose:** Summarizes medical reports into readable insights  
    - **Tech:** Based on facebook/bart-large-cnn, enhanced with NLI-based confab filtering and sentence enrichment  
    - **How to use:** Upload a medical document PDF or paste text  
  

    ---

    ### 🎧 ConvInt-BART (Conversation Interpretation)
    - **Purpose:** Upload audio of a doctor-patient talk and get a text summary  
    - **Tech:** Whisper for transcription + BART summarization + prompt tuning  
    - **How to use:** Upload .mp3 or .wav doctor-patient audio conversation  
   
    """)

elif st.session_state.page == "features":
   

    st.markdown("### 🔑 Core Capabilities of the Chatbot")
    st.markdown("""
    - 📄 **Document Summarization**: Converts complex medical documents into readable summaries
    - ❓ **Medical Q&A**: Users can ask questions about symptoms, conditions, medications, and more
    - 🎙️ **Conversation Interpretation**: Transcribes and summarizes doctor-patient conversations from audio
    - 🧠 **Domain-Specific Models**: Fine-tuned and structured prompts ensure contextual accuracy
    - 🔍 **Factual Filtering**: Confabulation detection ensures trustworthy outputs
    - ⚡ **Real-Time Performance**: Most responses are returned in under 1 second
    """)

    st.markdown("---")
    st.markdown("### 📊 Performance Comparison (vs ChatGPT-3.5)")

    

    data = {
        "Use Case": [
            "Document Summarization", "Document Summarization", "Document Summarization",
            "Question Answering", "Question Answering",
            "Conversation Interpretation", "Conversation Interpretation", "Conversation Interpretation"
        ],
        "Metric": [
            "BLEU", "ROUGE-L", "GLEU",
            "BLEU", "ROUGE",
            "BLEU", "ROUGE-L", "GLEU"
        ],
        "Our Model Score": [
            0.63, 0.75, 0.61,
            0.78, 0.66,
            0.79, 0.76, 0.68
        ],
        "ChatGPT-3.5 Score": [
            0.82, 0.81, 0.67,
            0.82, 0.75,
            0.80, 0.79, 0.72
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

elif st.session_state.page == "contact":
    # st.title("Contact Us")
    st.markdown("""
    **Team Members:**  
    - Aditya Pandey  
    - Hrithik Puppala  
    - Sivakrishna Yaganti
    - Yongen Chen
                
    **Advisor:**
    - Prof. Magdalini Eirinaki

    Department of Computer Engineering  
    San José State University  
    📧 Email: sjsu.healthbot.project@gmail.com
    
    **Test User Credentials:**
    - Username: `user1`
    - Password: `password123`
    """)
elif st.session_state.page == "sign_up":
    signup()

elif st.session_state.page == "need_my_access?":
    
    if not st.session_state.authenticated:
        login()
    else:
        chatbot()




add_footer()

# # Then your footer
# st.markdown("""---""")
# st.markdown(
#    """
#     <div style='text-align: center; font-size: 0.9em; color: gray;'>
#         Made with ❤️ using Streamlit · San José State University · CMPE 295<br>
#         Advised by Prof. Magdalini Eirinaki · 
#         <a href='https://github.com/sivask01/MedicalChatbot-GenAI' target='_blank' style='text-decoration: none;'>
#             <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='20' style='vertical-align: middle; margin-right: 5px;' />
#             Source Code
#         </a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )