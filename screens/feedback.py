import streamlit as st
import os
import pandas as pd
import csv
from datetime import datetime
from utils.session_state import SessionState

def save_feedback_to_csv(feedback_data):
    """Save feedback data to a CSV file"""
    # Define the CSV file path
    csv_path = "feedback_data.csv"
    file_exists = os.path.isfile(csv_path)
    
    # Open file in append mode
    with open(csv_path, mode='a', newline='') as file:
        fieldnames = feedback_data.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header only if file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(feedback_data)
    
    return csv_path

def render():
    """Render the Feedback screen"""
    st.header("Feedback")
    
    st.write("We value your opinion!")
    st.write("Please leave your feedback:")
    
    # Text area for feedback
    feedback_text = st.text_area("Feedback", placeholder="Your feedback helps us improve...", label_visibility="collapsed")
    
    # Rating for the outfit
    rating = st.slider("Rate your experience (1-5)", min_value=1, max_value=5, value=3)
    
    # Submit button
    if st.button("Submit", use_container_width=True):
        if feedback_text:
            # Prepare feedback data with all relevant information
            feedback_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "rating": rating,
                "feedback_text": feedback_text,
                "liked": st.session_state.feedback.get("liked"),
                "item_type": st.session_state.user_preferences.get("item_type", ""),
                "color": st.session_state.user_preferences.get("color", ""),
                "material": st.session_state.user_preferences.get("material", ""),
                "gender": st.session_state.user_preferences.get("gender", "")
            }
            
            # Add selected item info if available
            if st.session_state.selected_item:
                feedback_data["selected_item_id"] = st.session_state.selected_item.get("id", "")
                feedback_data["selected_item_type"] = st.session_state.selected_item.get("item_type", "")
            
            # Save feedback to CSV
            csv_path = save_feedback_to_csv(feedback_data)
            
            st.success(f"Thank you for your feedback!")
            # Wait a moment before returning to final look
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