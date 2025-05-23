import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{encoded}");
             background-size: cover;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Call the function with your image file path
add_bg_from_local(r"C:\Users\HP\OneDrive\Desktop\dataset for project consumer protection\New folder\ChatGPT Image May 22, 2025, 12_21_53 AM.png")