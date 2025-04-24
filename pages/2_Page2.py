import streamlit as st

# Page configuration
st.set_page_config(page_title="Page 2 - Emergency Procedures", page_icon="🩺")

# Sidebar link to navigate back to home
with st.sidebar:
    st.page_link("app.py", label="🏠 Back to Home")

# Emergency Procedures Header
st.markdown('<h1 class="main-header">Emergency Procedures</h1>', unsafe_allow_html=True)

# Main Content Container
with st.container():
    # Display a warning to emphasize emergency calls
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.warning("⚠️ For life-threatening emergencies, call 911 immediately.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Emergency procedure expandable sections
    with st.expander("Stroke - F.A.S.T. Assessment"):
        st.markdown("""
        ### F.A.S.T. Method for Stroke Recognition
        - **F - Face Drooping**: Ask the person to smile. Does one side of the face droop?
        - **A - Arm Weakness**: Ask the person to raise both arms. Does one arm drift downward?
        - **S - Speech Difficulty**: Ask the person to repeat a simple phrase. Is their speech slurred or strange?
        - **T - Time to Call 911**: If you observe any of these signs, call 911 immediately.

        **Additional Signs of Stroke:**
        - Sudden numbness or weakness, especially on one side of the body
        - Sudden confusion or trouble understanding
        - Sudden trouble seeing in one or both eyes
        - Sudden trouble walking, dizziness, loss of balance or coordination
        - Sudden severe headache with no known cause
        """)
        st.video("https://www.youtube.com/watch?v=oWrSXI6JppA")

    with st.expander("Heart Attack Recognition"):
        st.markdown("""
        ### Signs of a Heart Attack
        **Common symptoms include:**
        - Chest pain or discomfort (pressure, squeezing, fullness)
        - Discomfort in other areas of the upper body (arms, back, neck, jaw, stomach)
        - Shortness of breath
        - Cold sweat
        - Nausea
        - Lightheadedness

        **Women may also experience:**
        - Unusual fatigue
        - Sleep disturbances
        - Shortness of breath
        - Indigestion
        - Anxiety

        **Emergency Response:**
        1. Call 911 immediately
        2. Have the person chew and swallow an aspirin (if not allergic)
        3. Have the person rest in a comfortable position
        4. Loosen tight clothing
        5. Be prepared to perform CPR if needed
        """)
        st.video("https://www.youtube.com/watch?v=t7wmPWTnDbE")

    with st.expander("Seizure Management"):
        st.markdown("""
        ### Seizure First Aid
        **During a seizure:**
        1. Time the seizure - call 911 if it lasts longer than 5 minutes
        2. Clear the area of anything that could cause injury
        3. Place something soft under the person's head
        4. Turn them onto their side to prevent choking
        5. Do NOT restrain the person
        6. Do NOT put anything in their mouth

        **When to Call 911:**
        - First-time seizure
        - Seizure lasts longer than 5 minutes
        - Person doesn't wake up after the seizure ends
        - Another seizure follows quickly
        - Person is injured during the seizure
        - Seizure occurs in water
        - The person has a health condition like diabetes or is pregnant
        """)
        st.video("https://www.youtube.com/watch?v=5nhmh-lVG6U")

    with st.expander("Diabetic Emergency"):
        st.markdown("""
        ### Diabetic Emergencies: Hypoglycemia vs. Hyperglycemia
        #### Hypoglycemia (Low Blood Sugar):
        **Signs:**
        - Confusion, irritability
        - Shakiness, weakness
        - Sweating, pale skin
        - Hunger
        - Rapid heartbeat

        **First Aid:**
        1. If conscious and able to swallow, give 15-20 grams of fast-acting sugar (juice, glucose tablets)
        2. Wait 15 minutes and recheck symptoms
        3. If symptoms persist, give another 15-20 grams of sugar
        4. If unconscious, call 911 immediately

        #### Hyperglycemia (High Blood Sugar):
        **Signs:**
        - Extreme thirst
        - Frequent urination
        - Dry mouth
        - Fatigue
        - Nausea

        **First Aid:**
        1. Encourage fluid intake (water, sugar-free beverages)
        2. Help monitor blood glucose if equipment is available
        3. Seek medical attention if symptoms are severe or persist
        """)
        st.video("https://www.youtube.com/watch?v=dXNE0-t64JE")

    with st.expander("Poisoning & Overdose"):
        st.markdown("""
        ### Poisoning & Overdose Response
        **Steps for Suspected Poisoning:**
        1. Call Poison Control: 1-800-222-1222
        2. If the person is unconscious, not breathing, or having seizures, call 911
        3. Remove any remaining poison from the person's skin or mouth if possible
        4. Do NOT induce vomiting unless specifically instructed by a medical professional
        5. Have the following information ready:
            - Person's age and weight
            - Name of product or substance
            - Amount consumed
            - When it was consumed
            - Current symptoms

        **For Drug Overdose:**
        1. Call 911 immediately
        2. Check for responsiveness and breathing
        3. Administer naloxone (Narcan) if available and appropriate
        4. Place in recovery position (on side) if unconscious but breathing
        5. Be prepared to perform CPR if needed
        """)
        st.video("https://www.youtube.com/watch?v=cbm3zB8pcVU")

    # Interactive emergency protocol finder
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.subheader("Emergency Protocol Finder")

    emergency_options = [
        "Select an emergency situation",
        "Severe Bleeding",
        "Unconscious Person",
        "Drowning",
        "Electric Shock",
        "Head/Spinal Injury",
        "Heat Stroke",
        "Hypothermia",
    ]

    selected_emergency = st.selectbox("", emergency_options)

    # Display specific protocols based on selection
    if selected_emergency == "Severe Bleeding":
        st.markdown("""
        ### Severe Bleeding Protocol
        1. Apply direct pressure with clean cloth or bandage
        2. If blood soaks through, add more material without removing the original dressing
        3. If bleeding is from an arm or leg, elevate above heart level
        4. If bleeding doesn't stop with pressure, apply pressure to the appropriate arterial pressure point
        5. As a last resort for life-threatening limb bleeding, apply a tourniquet
        6. Call 911 or get to emergency care immediately
        """)
        st.image("https://api.placeholderweb.site/image?width=600&height=300&text=Pressure+Points+Diagram", use_column_width=True)

    elif selected_emergency == "Unconscious Person":
        st.markdown("""
        ### Unconscious Person Protocol
        1. Check for responsiveness by tapping and shouting
        2. Call 911 immediately
        3. Check for breathing (look, listen, feel for 5-10 seconds)
        4. If breathing, place in recovery position (on side)
        5. If not breathing normally, begin CPR:
           - 30 chest compressions (push hard and fast at center of chest)
           - 2 rescue breaths if trained
           - Continue until help arrives
        6. If AED is available, turn it on and follow prompts
        """)

    # Additional protocol sections here (e.g., drowning, electric shock, etc.)

    st.markdown('</div>', unsafe_allow_html=True)
