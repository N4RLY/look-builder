import streamlit as st
from utils.session_state import SessionState
import time

def render():
    """Render the Loading screen with a mock delay, then go to suggested_items."""
    st.header("")
    
    # Center the loading message and spinner
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.write("")

        # Display a spinner
        with st.spinner("Finding the perfect look for you..."):
            time.sleep(2)
        
        # After loading, go to suggested_items
        SessionState.navigate_to("suggested_items")
        st.rerun()
        
        # The actual navigation happens in the suggested_items.py when the button is clicked
        # This is just a visual screen that will be shown briefly 