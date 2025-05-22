from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model (free version)
model = genai.GenerativeModel('gemini-2.0-flash')

# Function to get Gemini response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Page config
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🤖 Q&A Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ask me anything. Powered by Gemini 2.0 Flash</p>", unsafe_allow_html=True)
st.markdown("---")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form (auto-submit on Enter)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your message 👇", key="input", placeholder="Type your question...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat_history.append(("🧑 You", user_input))
    with st.spinner("Thinking..."):
        answer = get_gemini_response(user_input)
    st.session_state.chat_history.append(("🤖 BOT", answer))

# Chat history
st.markdown("---")
st.markdown("### 📜 Chat History")
for role, msg in st.session_state.chat_history[::-1]:
    st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 10px 15px; border-radius: 10px; margin-bottom: 10px;'>
        <strong>{role}</strong><br>{msg}
    </div>
    """, unsafe_allow_html=True)
