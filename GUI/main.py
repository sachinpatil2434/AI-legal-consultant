import streamlit as st
import base64

# Page Configuration
st.set_page_config(page_title="LegalAID - Legal Assistant", page_icon="⚖️", layout="centered")

# Background with fade and responsiveness
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)),
                              url("data:image/png;base64,{encoded}");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center top;
            background-attachment: fixed;
        }}
        @media (max-width: 768px) {{
            .stApp {{
                background-size: cover;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set your local image path
add_bg_from_local(r"C:\Users\HP\OneDrive\Desktop\dataset for project consumer protection\New folder\ChatGPT Image May 22, 2025, 12_21_53 AM.png")

# Header
st.title("⚖️ LegalAID")
st.markdown("Welcome to **LegalAID**, your AI assistant for consumer protection laws.")
st.markdown("_Please note: This tool provides informational guidance, not legal advice._")
st.divider()

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages (top to bottom)
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.chat_message("user", avatar="🧑").markdown(msg)
    else:
        st.chat_message("assistant", avatar="🤖").markdown(msg)

# Input box and submit button at the bottom
user_input = st.text_input("Ask your legal question:", key="input_text")
if st.button("Send") and user_input:
    st.session_state.messages.append(("user", user_input))
    bot_reply = "Thank you for your question. LegalAID will answer here once connected to the API."
    st.session_state.messages.append(("bot", bot_reply))
    st.session_state.input_text = ""  # Clear input box after send

# Footer
st.divider()
st.markdown("🔒 LegalAID does not store your questions. | © 2025 LegalAID | AI for Legal Empowerment")
