import streamlit as st
from utils.session_state import SessionState

def render():
    """Render the Feedback screen"""
    st.header("Feedback")
    
    st.write("We value your opinion!")
    st.write("Please leave your feedback:")
    
    # Text area for feedback
    feedback = st.text_area("Feedback", placeholder="Your feedback helps us improve...", label_visibility="collapsed")
    
    # Submit button
    if st.button("Submit", use_container_width=True):
        if feedback:
            st.success("Thank you for your feedback!")
            # In a real application, you would store this feedback
            # For now, just wait a moment and return to final look
            import time
            time.sleep(2)
            
        # Navigate back to final look
        SessionState.navigate_to("final_look")
        st.rerun()
    
    # Skip button
    if st.button("Skip", use_container_width=True):
        # Navigate back to final look
        SessionState.navigate_to("final_look")
        st.rerun() 