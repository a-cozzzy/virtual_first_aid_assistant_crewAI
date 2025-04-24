import streamlit as st
from utils.chat_utils import init_chat, add_message, render_chat
from crew_config import run_crew  # <- your wrapper around CrewAI
import re
import time

# ---------- page config ----------
st.set_page_config(
    page_title="First-Aid Agent",
    page_icon="🚑",
    layout="centered"
)

# ---------- custom sidebar nav ----------
with st.sidebar:
    st.image("https://via.placeholder.com/150x80?text=FirstAid", width=150)
    st.markdown("## 🔗 Navigation")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/1_Page1.py", label="🩺 Emergency Guide")
    st.page_link("pages/2_Page2.py", label="📊 Medical Resources")
    st.page_link("pages/3_Page3.py", label="⚙️ Settings")
    
    st.markdown("---")
    
    # Emergency contacts section
    st.markdown("### ⚡ Emergency Contacts")
    st.markdown("**Emergency Services:** 108 ")
    st.markdown("**Poison Control:** 1-800-222-1222")
    
    st.markdown("---")
    st.caption("Always dial local emergency services in a life-threatening situation.")

# ---------- 'agentic' assistant ----------
st.title("🚑 First-Aid Assistant")
st.markdown("_AI-powered guidance for first aid medical situations_")

# Initialize session state for simulation stages
if 'simulation_stage' not in st.session_state:
    st.session_state.simulation_stage = 0

init_chat()
render_chat()

prompt = st.chat_input("What's going on? Describe your symptoms or situation…")

if prompt:
    add_message("user", prompt)
    
    # Create a placeholder for the staged loading indicators
    loading_placeholder = st.empty()
    
    # Simulate AI thinking process
    stages = [
        ("🔍 Analyzing medical context...", 0.7),
        ("🧠 Evaluating symptoms...", 0.8),
        ("📋 Consulting medical knowledge base...", 0.9),
        ("⚕️ Formulating response...", 0.6)
    ]
    
    # Display each stage with a progress bar
    for stage_text, duration in stages:
        with loading_placeholder.container():
            st.markdown(f'<p style="color:#3498db;font-weight:bold;">{stage_text}</p>', unsafe_allow_html=True)
            progress_bar = st.progress(0)
            for i in range(101):
                progress_bar.progress(i)
                time.sleep(duration/100)
    
    loading_placeholder.empty()
    
    # Display a processing spinner for the actual API call
    with st.spinner("Finalizing instructions..."):
        try:
            # results = run_crew(prompt)
            
            # # Simple cleanup of the response
            # response = str(results)
            # response = "\n\n".join(response.splitlines())

            
            # # Basic formatting - just add a header and ensure line breaks are preserved
            # response = "## FIRST AID INSTRUCTIONS:\n\n" + response
            
            # # Ensure proper line breaks between points
            # response = re.sub(r'(\*\*[^*]+\*\*:)', r'\n\1', response)
            # response = re.sub(r'\n{3,}', '\n\n', response)

            results = run_crew(prompt)

            # 1. Convert to string and prepend header
            raw = "FIRST AID INSTRUCTIONS:\n\n" + str(results)

            # 2. Split into lines and re-join with a blank line between each
            response = "\n\n".join(line for line in raw.splitlines() if line.strip())


            
        except Exception as e:
            response = (
                f"⚠️ **System Alert:** {e}\n\n"
                "Please try again or use emergency contacts if this is urgent."
            )

        # try:
        #     results = run_crew(prompt)  # <- your CrewAI call
            
        #     # Enhanced formatting for responses
        #     if isinstance(results, str):
        #         # Format numbered lists properly with line breaks
        #         response = re.sub(r'(?<=\d\.) ', '\n', str(results))
                
        #         # Format headers
        #         response = re.sub(r'(\*\*[^*]+\*\*)', r'\n\1\n', response)
                
        #         # Add visual separators for sections
        #         if "Steps:" in response or "Instructions:" in response:
        #             response = response.replace("Steps:", "\n🔶 **Steps:**\n")
        #             response = response.replace("Instructions:", "\n🔶 **Instructions:**\n")
                
        #         # Add warning symbols to cautionary language
        #         response = re.sub(r'(Warning|Caution|IMPORTANT|Alert):', r'⚠️ **\1:**', response)
        #     else:
        #         response = str(results)
            
        # except Exception as e:
        #     response = (
        #         f"⚠️ **System Alert:** {e}\n\n"
        #         "Please try again or use emergency contacts if this is urgent."
        #     )
    
    # Add a visual metadata box for severity assessment
    if "severe" in prompt.lower() or "urgent" in prompt.lower() or "emergency" in prompt.lower():
        st.warning("⚠️ **POTENTIAL EMERGENCY DETECTED**: Consider calling emergency services immediately.")
    
    add_message("assistant", response)
    render_chat()
    
    # Add helpful follow-up suggestions based on context
    with st.expander("Suggested Follow-ups"):
        st.markdown("- Request information about when to seek professional help")
        st.markdown("- Ask about possible complications to watch for")

# Add information footer
st.markdown("---")
st.caption("This AI assistant provides general first aid information only. It is not a substitute for professional medical advice, diagnosis, or treatment.")