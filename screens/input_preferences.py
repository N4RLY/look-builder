import streamlit as st
from utils.session_state import SessionState
from utils.simple_embedder import SimpleEmbedder
import time

def render(embedder: SimpleEmbedder):
    """Render the Input Preferences screen"""
    st.header("Input Preferences")
    
    with st.container():
        st.subheader("Select your item's parameters:")
        
        # Item type selection
        item_types = ["shirt", "dress", "pants", "shoes", "accessories"]
        item_type = st.selectbox("Item type:", item_types)
        
        # Color selection
        colors = ["white", "black", "blue", "red", "green", "yellow", "purple", "orange", "pink", "brown", "gray"]
        color = st.selectbox("Color:", colors)
        
        # Material selection
        materials = ["cotton", "wool", "linen", "polyester", "leather", "silk", "denim", "canvas"]
        material = st.selectbox("Material:", materials)
        
        st.caption("Specifying one or multiple parameters is optional")
        
        # Gender selection
        col1, col2 = st.columns(2)
        with col1:
            male = st.checkbox("Male")
        with col2:
            female = st.checkbox("Female")
            
        gender = "male" if male else "female" if female else ""
        
        # Update preferences in session state
        preferences = {
            "item_type": item_type,
            "color": color,
            "material": material,
            "gender": gender
        }
        
        # Find outfit button
        if st.button("🔍 Find outfit", use_container_width=True):
            SessionState.update_preferences(preferences)
            
            # Find similar items based on preferences
            query_item = {
                "type": item_type,
                "color": color,
                "material": material,
            }
            
            similar_items = embedder.find_similar_items(query_item, top_n=5)
            
            if similar_items:
                SessionState.set_suggested_items(similar_items)
                # Navigate to loading screen and rerun
                SessionState.navigate_to("loading")
                st.rerun()
            else:
                st.error("No matching items found. Please try different parameters.")
                time.sleep(2)
                st.rerun() 