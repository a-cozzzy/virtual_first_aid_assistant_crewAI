import streamlit as st

# Page configuration
st.set_page_config(page_title="Page 3", page_icon="🩺")

# Personal Notes section
st.markdown('<div class="med-card">', unsafe_allow_html=True)
st.markdown("""
## Personal Medical Information

Use this section to record important personal medical information for quick reference during emergencies.
""")

# Load existing notes from session state
if 'medical_notes' not in st.session_state:
    st.session_state.medical_notes = {
        'personal': '',
        'conditions': '',
        'medications': '',
        'allergies': '',
        'contacts': ''
    }

# Personal info section
st.subheader("Personal Information")
st.session_state.medical_notes['personal'] = st.text_area(
    "Name, Blood Type, Date of Birth, etc.",
    value=st.session_state.medical_notes['personal'],
    height=100
)

# Medical conditions section
st.subheader("Medical Conditions")
st.session_state.medical_notes['conditions'] = st.text_area(
    "List any relevant medical conditions",
    value=st.session_state.medical_notes['conditions'],
    height=100
)

# Medications section
st.subheader("Current Medications")
st.session_state.medical_notes['medications'] = st.text_area(
    "List medications, dosages, and schedule",
    value=st.session_state.medical_notes['medications'],
    height=100
)

# Allergies section
st.subheader("Allergies")
st.session_state.medical_notes['allergies'] = st.text_area(
    "List allergies and reactions",
    value=st.session_state.medical_notes['allergies'],
    height=100
)

# Emergency contacts section
st.subheader("Emergency Contacts")
st.session_state.medical_notes['contacts'] = st.text_area(
    "List emergency contacts and their phone numbers",
    value=st.session_state.medical_notes['contacts'],
    height=100
)

# Save and Clear functionality
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("📝 Save Notes", key="save_notes"):
        st.success("Your medical notes have been saved!")

with col2:
    if st.button("🗑️ Clear All", key="clear_notes"):
        st.session_state.medical_notes = {
            'personal': '',
            'conditions': '',
            'medications': '',
            'allergies': '',
            'contacts': ''
        }
        st.success("All notes have been cleared.")

# Export functionality
st.subheader("Export Your Notes")
if st.button("📄 Export as PDF", key="export_pdf"):
    st.info("PDF export functionality will be available in the full application.")

# Medical information privacy notice
st.markdown("""
---
**Privacy Notice**: Information stored in this notes section is saved only on your device and is not transmitted elsewhere. For security, avoid including sensitive information like Social Security numbers.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Additional Medical ID Card Section
st.markdown('<div class="med-card">', unsafe_allow_html=True)
st.subheader("Medical ID Card")

# Two-column layout for medical ID creation
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Upload Photo")
    st.file_uploader("Upload a photo for your medical ID", type=["jpg", "jpeg", "png"])

with col2:
    st.markdown("### Medical ID Information")
    full_name = st.text_input("Full Name")
    emergency_contact = st.text_input("Emergency Contact")
    phone_number = st.text_input("Phone Number")

    # Blood type selection
    blood_types = ["Select Blood Type", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"]
    selected_blood = st.selectbox("Blood Type", blood_types)

    # Medical alert checkboxes
    st.markdown("### Medical Alerts")
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Diabetes")
        st.checkbox("Heart Condition")
        st.checkbox("Asthma")
    with col2:
        st.checkbox("Epilepsy")
        st.checkbox("Allergies")
        st.checkbox("Other")

# Button to generate medical ID card
if st.button("Generate Medical ID Card", key="gen_id"):
    st.info("In the full application, this would generate a printable medical ID card.")
    # Placeholder for where the card would be displayed
    st.markdown("""
    ```
    --------------------------------
    |  MEDICAL ALERT ID            |
    |                              |
    |  [Photo]   Name: ___         |
    |            Blood Type: ___   |
    |            Alerts: ___       |
    |                              |
    |  Emergency Contact: ___      |
    |  Phone: ___                  |
    --------------------------------
    ```
    """)

st.markdown('</div>', unsafe_allow_html=True)

# Footer section for privacy and terms
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 20px; border-radius: 8px;">
    <p>MediAssist Pro provides basic first aid information for educational purposes only.</p>
    <p><strong>Always call emergency services (911) for serious medical emergencies.</strong></p>
    <p>© 2025 MediAssist Pro | <a href="#">Terms of Use</a> | <a href="#">Privacy Policy</a></p>
</div>
""", unsafe_allow_html=True)

# Sidebar link for navigation
with st.sidebar:
    st.page_link("app.py", label="🏠 Back to Home")
