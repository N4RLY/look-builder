import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items
import time

def render():
    """Render the Input Preferences screen using the mock dataset"""
    st.markdown("""
        <div style='text-align: center; margin-bottom: 1.5rem;'>
            <span style='font-size: 2rem; font-weight: bold;'>Screen 1: Input Preferences</span>
        </div>
    """, unsafe_allow_html=True)

    # Dynamically get feature lists from the dataset
    feature_values = SessionState.get_feature_lists(clothing_items)

    with st.container():
        st.markdown("<div style='font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;'>Select your item's parameters:</div>", unsafe_allow_html=True)

        # Item type selection
        item_types = feature_values.get("item_type", [])
        item_type = st.selectbox("Item type:", ["(any)"] + item_types, key="item_type")
        item_type = "" if item_type == "(any)" else item_type

        # Color selection
        colors = feature_values.get("color", [])
        color = st.selectbox("Color:", ["(any)"] + colors, key="color")
        color = "" if color == "(any)" else color

        # Material selection
        materials = feature_values.get("material", [])
        material = st.selectbox("Material:", ["(any)"] + materials, key="material")
        material = "" if material == "(any)" else material

        st.markdown("<div style='font-size: 0.9rem; color: #888; margin: 0.5rem 0 0.5rem 0;'>Specifying one or multiple parameters is optional</div>", unsafe_allow_html=True)

        # Gender checkboxes
        col1, col2 = st.columns([1, 1])
        with col1:
            male = st.checkbox("Male", key="male")
        with col2:
            female = st.checkbox("Female", key="female")

        # Preferences dict
        preferences = {
            "item_type": item_type,
            "color": color,
            "material": material,
            "male": male,
            "female": female
        }

        st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)
        if st.button("🔍 Find outfit", use_container_width=True):
            SessionState.update_preferences(preferences)
            SessionState.navigate_to("suggested_items")
            st.rerun() 