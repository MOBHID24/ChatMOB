# Author - MOBHID

import streamlit as st
import google.generativeai as palm
from google.auth.exceptions import DefaultCredentialsError  # Import the DefaultCredentialsError
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.environ.get("PALM_API_KEY")

try:
    palm.configure(api_key=API_KEY)
except DefaultCredentialsError as e:
    st.error("Authentication error: Google Cloud credentials not found.")
    st.write("Please set up Application Default Credentials (ADC) or ensure the PALM_API_KEY is correctly set.")
    st.stop()

def greet_user():
    st.markdown(
        """
        <style>
            body {
                background-image: url('https://th.bing.com/th?id=OIP.IjRkXoJrXu-IHZUrg3X_BgAAAA&w=312&h=200&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2');
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
            .greet-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: rgba(255, 255, 255, 0.8); /* Add transparency to make text readable */
            }
            .greet-content {
                text-align: center;
            }
            .stTextInput>div>div>input {
                background-color: #fff;
                border-color: #007bff;
            }
            .stSlider>div>div>div {
                background-color: #007bff;
            }
            .stButton>button {
                background-color: #007bff;
                color: #fff;
                border-color: #007bff;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #0056b3;
            }
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
                color: #007bff;
                font-weight: bold;
            }
            .stMarkdown {
                font-family: "Arial", sans-serif;
                font-size: 16px;
                line-height: 1.6;
            }
            .response-container {
                margin-top: 20px;
                border-radius: 10px;
                background-color: #f9f9f9;
                padding: 20px;
            }
        </style>
        """
        , unsafe_allow_html=True
    )

    st.header("Welcome to ChatMOB")
    st.write("")
    st.write("How can I assist you today?")
    st.write("")

def main():
    greet_user()

    prompt = st.text_input("Enter your query here", placeholder="Your question", label_visibility="visible")
    temp = 0.7   # Hyper parameter - range[0-1]

    if st.button("SEND", use_container_width=True):
        model = "models/text-bison-001"  #	models/text-bison-001  # This is the only model currently available

        try:
            response = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=temp,
                max_output_tokens=1024
            )
        except DefaultCredentialsError as e:
            st.error("Authentication error: Google Cloud credentials not found.")
            st.write("Please set up Application Default Credentials (ADC) or ensure the PALM_API_KEY is correctly set.")
            st.stop()

        st.write("")
        st.header("Response", anchor="response")
        st.write("")

        st.markdown(f'<div class="response-container">{response.result}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
