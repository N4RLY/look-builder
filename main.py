import streamlit as st
import os
import sys
from pathlib import Path

# Add the project root to path
sys.path.append(str(Path(__file__).parent))

# Import screens
from screens import input_preferences, suggested_items, loading, suggested_look
from screens import clarify_feedback, final_look, feedback

# Import utilities
from utils.session_state import SessionState

def main():
    """Main function to run the Streamlit app"""
    # Set page config
    st.set_page_config(
        page_title="Look Builder",
        page_icon="👕",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    SessionState.initialize_session()
    
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display the appropriate screen based on session state
    if st.session_state.current_screen == "input_preferences":
        input_preferences.render()
    elif st.session_state.current_screen == "suggested_items":
        suggested_items.render()
    elif st.session_state.current_screen == "loading":
        loading.render()
    elif st.session_state.current_screen == "suggested_look":
        suggested_look.render()
    elif st.session_state.current_screen == "clarify_feedback":
        clarify_feedback.render()
    elif st.session_state.current_screen == "final_look":
        final_look.render()
    elif st.session_state.current_screen == "feedback":
        feedback.render()
    else:
        # Default to input preferences if there's an issue
        SessionState.navigate_to("input_preferences")
        st.rerun()

if __name__ == "__main__":
    main()
