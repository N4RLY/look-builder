import streamlit as st
from utils.session_state import SessionState
import time

def render():
    """Render the Loading screen with a mock delay, then go to suggested_items."""
    # Clear the entire screen first by setting a fullscreen container
    st.markdown("""
        <style>
        .fullscreen-container {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #0E1117;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-bottom: 100px;
        }
        </style>
        <div class="fullscreen-container">
            <h2 style="color: white; margin-bottom: 20px;">Finding Items For You</h2>
            <div style="color: #4CAF50; font-size: 16px;">Searching for the perfect items that match your style...</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Hide the sidebar to prevent UI artifacts
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Loading delay
    time.sleep(2.5)
    
    # After loading, go to suggested_items
    SessionState.navigate_to("suggested_items")
    st.rerun()
        
    # The actual navigation happens in the suggested_items.py when the button is clicked
    # This is just a visual screen that will be shown briefly 