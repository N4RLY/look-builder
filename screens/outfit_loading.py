import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items, outfits
import time

def render():
    """Render the Outfit Loading screen with a delay, then go to suggested_outfits."""
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
            <h2 style="color: white; margin-bottom: 20px;">Creating Your Outfit Options</h2>
            <div style="color: #4CAF50; font-size: 16px;">Finding the perfect outfit combinations...</div>
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
    
    # Perform necessary operations without showing UI elements
    if 'outfit_options' in st.session_state:
        del st.session_state.outfit_options
        
    # Loading delay
    time.sleep(2.5)
    
    # Make sure there's a selected item before proceeding
    if st.session_state.selected_item is None:
        SessionState.navigate_to("suggested_items")
        st.rerun()
    
    # Navigate to suggested outfits after loading is complete
    SessionState.navigate_to("suggested_outfits")
    st.rerun() 