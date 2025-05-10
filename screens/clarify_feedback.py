import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items, outfits
import time

def render():
    """Render the Clarify Feedback screen"""
    st.header("Clarify Feedback")
    
    st.write("Sorry the outfit didn't match your style.")
    st.write("Tell us what exactly didn't work — I'll find a better one right away!")
    
    # Text area for detailed feedback
    feedback = st.text_area("Clarify Feedback", placeholder="Please provide specific feedback...", label_visibility="collapsed")
    
    # Regenerate outfit button
    if st.button("Regenerate Outfit", use_container_width=True):
        # Store the feedback
        SessionState.set_feedback(liked=False, feedback_text=feedback)
        
        # Navigate to loading screen
        SessionState.navigate_to("loading")
        
        # Generate a new outfit based on the base item
        base_item = st.session_state.outfit["base_item"]
        new_outfit = SessionState.recommend_outfit(base_item, clothing_items, outfits)
        
        # Replace old outfit with new one
        SessionState.set_outfit(new_outfit)
        
        # Brief pause for loading screen
        time.sleep(2)
        
        # Navigate to suggested look
        SessionState.navigate_to("suggested_look")
        st.rerun()
    
    # Start over button
    if st.button("Start over", use_container_width=True):
        st.caption("This will reset all your selections")
        # Reset the session and go back to input preferences
        SessionState.reset()
        SessionState.navigate_to("input_preferences")
        st.rerun() 