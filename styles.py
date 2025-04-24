import streamlit as st
from crew_config import run_crew
from session_utils import init_chat, add_message, render_chat

# Page configuration with clean medical theme
st.set_page_config(
    page_title="🩺 MediAssist Pro | Emergency First Aid",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar branding and contacts
with st.sidebar:
    st.markdown('<h1 style="font-size: 1.8rem; color: #2c3e50;">🩺 MediAssist Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #555; margin-top: -10px;">Your advanced digital health assistant</p>', unsafe_allow_html=True)
    
    st.markdown('<hr style="border-top: 1px solid #bbb;">', unsafe_allow_html=True)
    st.markdown('<h3 style="margin-bottom: 10px;">Emergency Contacts</h3>', unsafe_allow_html=True)
    st.markdown(
        '<ul style="padding-left: 20px;">'
        '<li><b>Emergency:</b> 911</li>'
        '<li><b>Poison Control:</b> 800-222-1222</li>'
        '<li><b>Suicide Prevention:</b> 988</li>'
        '</ul>',
        unsafe_allow_html=True
    )
    st.markdown('<a href="tel:911" style="display: block; text-align: center; background-color: #e74c3c; color: white; padding: 10px; border-radius: 8px; margin-top: 10px; text-decoration: none;">🚨 CALL 911</a>', unsafe_allow_html=True)
    
    st.markdown("<hr style='border-top: 1px solid #bbb;'>", unsafe_allow_html=True)
    st.caption("MediAssist Pro v1.0.2")
    st.caption("⚠️ Not a substitute for professional medical care")

# Main Home Page Content
st.markdown('<h1 style="color: #2c3e50;">Welcome to MediAssist Pro</h1>', unsafe_allow_html=True)

st.markdown('<div style="background-color: #f9f9f9; border-left: 6px solid #3498db; padding: 1.2rem 1.5rem; border-radius: 10px; margin-bottom: 20px;">', unsafe_allow_html=True)
st.markdown("""
This is your AI-powered medical first aid assistant.

- Get instant assessment of symptoms or situations
- Follow trusted, step-by-step emergency protocols
- Make informed decisions quickly with intelligent guidance

In a life-threatening emergency, always dial 911.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Chat Interface Section
st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
st.markdown('<h2 style="color: #2c3e50;">Medical AI Assistant</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #444;">Describe symptoms or ask for first aid instructions below.</p>', unsafe_allow_html=True)

init_chat()
render_chat()

prompt = st.chat_input("What's going on? Describe your symptoms or situation...")

if prompt:
    add_message("user", prompt)
    with st.spinner(""):
        st.markdown('<p style="color: #3498db; font-weight: bold;">Analyzing medical context...</p>', unsafe_allow_html=True)
        try:
            results = run_crew(prompt)
            response = str(results)
        except Exception as e:
            response = f"⚠ System Alert: {e}\n\nPlease try again or use the emergency contacts if this is urgent."
    add_message("assistant", response)
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)