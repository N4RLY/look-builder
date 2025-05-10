import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items
import time

def render():
    """Render the Input Preferences screen using the mock dataset"""
    st.header("Input Preferences")

    # Dynamically get feature lists from the dataset
    feature_values = SessionState.get_feature_lists(clothing_items)

    with st.container():
        st.subheader("Select your item's parameters:")

        # Item type selection
        item_types = feature_values.get("item_type", [])
        item_type = st.selectbox("Item type:", ["(any)"] + item_types)
        item_type = "" if item_type == "(any)" else item_type

        # Color selection
        colors = feature_values.get("color", [])
        color = st.selectbox("Color:", ["(any)"] + colors)
        color = "" if color == "(any)" else color

        # Material selection
        materials = feature_values.get("material", [])
        material = st.selectbox("Material:", ["(any)"] + materials)
        material = "" if material == "(any)" else material

        # Gender selection
        genders = feature_values.get("gender", [])
        gender = st.selectbox("Gender:", ["(any)"] + genders)
        gender = "" if gender == "(any)" else gender

        # Style selection (optional)
        styles = feature_values.get("style", [])
        style = st.selectbox("Style:", ["(any)"] + styles)
        style = "" if style == "(any)" else style

        # Update preferences in session state
        preferences = {
            "item_type": item_type,
            "color": color,
            "material": material,
            "gender": gender,
            "style": style
        }

        if st.button("🔍 Find outfit", use_container_width=True):
            SessionState.update_preferences(preferences)
            SessionState.navigate_to("suggested_items")
            st.rerun() 