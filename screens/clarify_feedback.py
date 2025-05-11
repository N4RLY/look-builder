import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items, outfits
import time

def render():
    """Render the Clarify Feedback screen"""
    st.header("Add More Context")
    
    st.write("Help us understand your style preferences better.")
    st.write("What specific details should we consider for your outfit?")
    
    # Text area for detailed feedback
    feedback = st.text_area("Additional Context", placeholder="Tell us about your style preferences, event, or specific needs...", label_visibility="collapsed")
    
    # Regenerate outfit button
    if st.button("Generate Outfit", use_container_width=True):
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
        
        # Navigate back to suggested outfits with the context
        SessionState.navigate_to("suggested_outfits")
        st.rerun()
    
    # Start over button
    if st.button("Start over", use_container_width=True):
        st.caption("This will reset all your selections")
        # Reset the session and go back to input preferences
        SessionState.reset()
        SessionState.navigate_to("input_preferences")
        st.rerun() 