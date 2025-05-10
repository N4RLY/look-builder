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

    @staticmethod
    def get_feature_lists(items: List[Dict[str, Any]]):
        """Dynamically extract all possible values for each feature from the dataset."""
        feature_values = {}
        for item in items:
            for key, value in item.items():
                if key == "id":
                    continue
                if key not in feature_values:
                    feature_values[key] = set()
                feature_values[key].add(value)
        # Sort values for consistency
        for key in feature_values:
            feature_values[key] = sorted(list(feature_values[key]))
        return feature_values

    @staticmethod
    def embed_item(item: Dict[str, Any], feature_values: Dict[str, List[Any]]) -> List[int]:
        """Embed an item or preferences as a one-hot vector using dynamic feature values."""
        vector = []
        for feature, values in feature_values.items():
            value = item.get(feature, "")
            vector += [int(value == v) for v in values]
        return vector

    @staticmethod
    def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:
        """Compute cosine similarity between two vectors."""
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    @staticmethod
    def find_best_matches(preferences: Dict[str, str], items: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
        """Find top_k items closest to preferences in vector space using dynamic features."""
        feature_values = SessionState.get_feature_lists(items)
        pref_vec = SessionState.embed_item(preferences, feature_values)
        scored = [
            (item, SessionState.cosine_similarity(pref_vec, SessionState.embed_item(item, feature_values)))
            for item in items
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [item for item, score in scored[:top_k]]

    @staticmethod
    def recommend_outfit(selected_item: Dict[str, Any], items: List[Dict[str, Any]], outfits: List[list]) -> Dict[str, Any]:
        """Given a selected item, find a compatible outfit from the dataset."""
        # Find the outfit that contains the selected item's id
        for outfit in outfits:
            if selected_item["id"] in outfit:
                # Get all items in the outfit
                outfit_items = [item for item in items if item["id"] in outfit and item["id"] != selected_item["id"]]
                return {
                    "base_item": selected_item,
                    "recommended_items": outfit_items
                }
        # If no outfit found, just return the selected item
        return {
            "base_item": selected_item,
            "recommended_items": []
        } 