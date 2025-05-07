from typing import Dict, Any, List, Optional
import streamlit as st

class SessionState:
    """Utility for managing state across screens in Streamlit app"""
    
    @staticmethod
    def initialize_session():
        """Initialize session state variables if they don't exist"""
        if 'current_screen' not in st.session_state:
            st.session_state.current_screen = 'input_preferences'
            
        if 'user_preferences' not in st.session_state:
            st.session_state.user_preferences = {
                'item_type': '',
                'color': '',
                'material': '',
                'gender': ''
            }
            
        if 'selected_item' not in st.session_state:
            st.session_state.selected_item = None
            
        if 'suggested_items' not in st.session_state:
            st.session_state.suggested_items = []
            
        if 'outfit' not in st.session_state:
            st.session_state.outfit = None
            
        if 'feedback' not in st.session_state:
            st.session_state.feedback = {
                'liked': None,
                'feedback_text': ''
            }
            
    @staticmethod
    def navigate_to(screen: str):
        """Navigate to a specific screen"""
        st.session_state.current_screen = screen
        
    @staticmethod
    def update_preferences(preferences: Dict[str, str]):
        """Update user preferences"""
        for key, value in preferences.items():
            if key in st.session_state.user_preferences:
                st.session_state.user_preferences[key] = value
                
    @staticmethod
    def set_suggested_items(items: List[Dict[str, Any]]):
        """Set the suggested items"""
        st.session_state.suggested_items = items
        
    @staticmethod
    def select_item(item: Dict[str, Any]):
        """Select an item from the suggestions"""
        st.session_state.selected_item = item
        
    @staticmethod
    def set_outfit(outfit: Dict[str, Any]):
        """Set the outfit recommendation"""
        st.session_state.outfit = outfit
        
    @staticmethod
    def set_feedback(liked: bool, feedback_text: str = ''):
        """Set user feedback"""
        st.session_state.feedback = {
            'liked': liked,
            'feedback_text': feedback_text
        }
        
    @staticmethod
    def reset():
        """Reset the session to start over"""
        st.session_state.current_screen = 'input_preferences'
        st.session_state.user_preferences = {
            'item_type': '',
            'color': '',
            'material': '',
            'gender': ''
        }
        st.session_state.selected_item = None
        st.session_state.suggested_items = []
        st.session_state.outfit = None
        st.session_state.feedback = {
            'liked': None,
            'feedback_text': ''
        } 