import streamlit as st
from utils.session_state import SessionState

def render():
    """Render the Loading screen"""
    st.header("Screen 3: Loading")
    
    # Center the loading message and spinner
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.write("")
        st.write("")
        st.markdown("<h3 style='text-align: center;'>Finding the perfect look for you...</h3>", unsafe_allow_html=True)
        st.write("")
        
        # Display a spinner
        with st.spinner():
            st.write("")  # This is just to give some space for the spinner
        
        # The actual navigation happens in the suggested_items.py when the button is clicked
        # This is just a visual screen that will be shown briefly 