import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Page 1", page_icon="🩺")
# Add the main header
st.markdown('<h1 class="main-header">First Aid Guide</h1>', unsafe_allow_html=True)

# First Aid Guide with tabs for different categories
tabs = st.tabs(["CPR", "Choking", "Bleeding", "Burns", "Fractures", "Allergic Reactions"])

# CPR Tab
with tabs[0]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## CPR (Cardiopulmonary Resuscitation)
    
    ### Adult CPR - Basic Steps:
    1. **Check for responsiveness** - Tap and shout "Are you okay?"
    2. **Call 911** or ask someone else to call
    3. **Check for breathing** - Look, listen, and feel for breathing for 5-10 seconds
    4. **Begin chest compressions** - Place hands on center of chest and compress hard and fast (100-120 compressions/minute)
    5. **Give rescue breaths** (if trained) - Tilt head back, lift chin, pinch nose, and give 2 breaths
    6. **Continue CPR** - 30 compressions followed by 2 breaths
    
    ### Child/Infant CPR - Key Differences:
    - Use less force for compressions
    - For infants, use two fingers for compressions
    - Cover both mouth and nose when giving breaths to an infant
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=M4ACYp75mjU")
    st.markdown("[American Heart Association CPR Guidelines](https://cpr.heart.org/en/cpr-courses-and-kits/cpr-guidelines)")
    st.markdown('</div>', unsafe_allow_html=True)

# Choking Tab
with tabs[1]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Choking First Aid (Heimlich Maneuver)
    
    ### For Adults and Children:
    1. **Ask "Are you choking?"** - If they can speak, cough, or breathe, don't interfere
    2. **Stand behind** the person with one foot forward
    3. **Place arms around waist**
    4. **Make a fist** with one hand, place thumb side against middle of abdomen, just above the navel
    5. **Grasp fist** with other hand
    6. **Perform quick, upward thrusts** until object is expelled or person becomes unconscious
    
    ### For Infants (Under 1 Year):
    1. **Place infant face-down** on your forearm
    2. **Support the head** but allow it to be lower than the body
    3. **Deliver 5 back blows** between the shoulder blades
    4. **Turn infant face-up** and deliver 5 chest compressions
    5. **Repeat until object is expelled** or emergency help arrives
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=PA9hpOnvtCk")
    st.markdown("[Red Cross Choking Response Guidelines](https://www.redcross.org/take-a-class/cpr/performing-cpr/conscious-choking)")
    st.markdown('</div>', unsafe_allow_html=True)

# Bleeding Tab
with tabs[2]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Bleeding Control
    
    ### For External Bleeding:
    1. **Apply direct pressure** to the wound using a clean cloth or bandage
    2. **Elevate the injured area** above heart level if possible
    3. **Apply pressure to pressure points** if direct pressure isn't stopping the bleeding
    4. **Apply a tourniquet** only as a last resort for life-threatening limb bleeding
    
    ### For Nosebleeds:
    1. **Sit upright** and lean slightly forward
    2. **Pinch the soft part of the nose** for 10-15 minutes
    3. **Apply cold compress** to bridge of nose
    4. **Seek medical attention** if bleeding doesn't stop after 20 minutes
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=NxO5LvgqZe0")
    st.markdown("[Stop the Bleed Campaign Resources](https://www.stopthebleed.org/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Burns Tab
with tabs[3]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Burn Treatment
    
    ### First-Degree Burns (Redness, Pain):
    1. **Cool the burn** with cool (not cold) running water for 10-15 minutes
    2. **Do not apply ice** directly to the burn
    3. **Apply aloe vera** or moisturizer
    4. **Take over-the-counter pain relievers** if needed
    
    ### Second-Degree Burns (Blisters, Severe Redness):
    1. **Cool the burn** with running water for 15-20 minutes
    2. **Do not break blisters**
    3. **Apply antibiotic ointment** and cover with a sterile bandage
    4. **Seek medical attention** for large burns or burns on face, hands, feet, genitals
    
    ### Third-Degree Burns (Charred, Dry, Leathery Skin):
    1. **Call 911 immediately**
    2. **Do not remove clothing** stuck to the burn
    3. **Cover with a clean, dry cloth**
    4. **Check for signs of shock** and treat accordingly
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=EaJmzB8YgS0")
    st.markdown("[American Burn Association Resources](https://ameriburn.org/public-resources/burn-awareness-prevention/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Fractures Tab
with tabs[4]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Fracture & Sprain Management
    
    ### Suspected Fractures:
    1. **Keep the injured area immobile** and supported
    2. **Apply ice packs** wrapped in cloth for 20 minutes at a time
    3. **Create a splint** if needed using rigid material
    4. **Elevate the injured area** if possible
    5. **Seek immediate medical attention**
    
    ### Warning Signs of Fracture:
    - Deformity or abnormal alignment
    - Crepitus (grinding sensation)
    - Pain that intensifies with movement
    - Inability to bear weight or use limb
    - Significant swelling or bruising
    
    ### For Sprains:
    Remember **R.I.C.E**:
    - **Rest** the injured area
    - **Ice** for 20 minutes every 2-3 hours
    - **Compression** with elastic bandage
    - **Elevation** above heart level
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=PfNAuHuTT8g")
    st.markdown("[American Academy of Orthopaedic Surgeons - Fracture Care](https://orthoinfo.aaos.org/en/diseases--conditions/fractures-broken-bones/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Allergic Reactions Tab
with tabs[5]:
    st.markdown('<div class="med-card">', unsafe_allow_html=True)
    st.markdown("""
    ## Allergic Reaction Response
    
    ### Mild to Moderate Allergic Reactions:
    1. **Remove the allergen** if possible
    2. **Take antihistamine** if available and appropriate
    3. **Apply cold compress** to itchy areas
    4. **Monitor for worsening symptoms**
    5. **Seek medical attention** if symptoms don't improve
    
    ### Severe Allergic Reactions (Anaphylaxis):
    1. **Call 911 immediately**
    2. **Use epinephrine auto-injector** (EpiPen) if available
    3. **Help the person stay calm** and lay flat with legs elevated
    4. **Monitor breathing and circulation**
    5. **Be prepared to perform CPR** if needed
    
    ### Signs of Anaphylaxis:
    - Difficulty breathing or swallowing
    - Swelling of lips, tongue, throat
    - Widespread hives or flushing
    - Dizziness or feeling faint
    - Rapid pulse
    - Nausea, vomiting, abdominal pain
    """)
    st.subheader("Educational Resources")
    st.video("https://www.youtube.com/watch?v=CEgH16ZkHvk")
    st.markdown("[Food Allergy Research & Education (FARE)](https://www.foodallergy.org/resources/recognizing-responding-anaphylaxis)")
    st.markdown('</div>', unsafe_allow_html=True)

# Sidebar link
with st.sidebar:
    st.page_link("app.py", label="🏠 Back to Home")
