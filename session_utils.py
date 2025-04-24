import streamlit as st

# ------------- session-state helpers -------------
def init_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content})

def render_chat():
    """A minimal ‘agentic’ transcript – not chat bubbles."""
    for m in st.session_state.messages:
        prefix = "👤" if m["role"] == "user" else "🤖"
        st.markdown(f"**{prefix} {m['role'].capitalize()}:** {m['content']}")