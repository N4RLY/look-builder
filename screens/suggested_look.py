import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items, outfits

def render():
    """Render the Suggested Look screen"""
    st.header("Suggested Look")
    
    # If no outfit is set, generate it from the selected item
    if st.session_state.outfit is None:
        selected_item = st.session_state.selected_item
        if selected_item is not None:
            outfit = SessionState.recommend_outfit(selected_item, clothing_items, outfits)
            SessionState.set_outfit(outfit)
        else:
            st.error("No outfit recommendation found. Please start over.")
            if st.button("Start Over"):
                SessionState.reset()
                SessionState.navigate_to("input_preferences")
                st.rerun()
            return
    
    with st.container():
        st.subheader("Your suggested look:")
        
        # Get the base item and recommendations
        base_item = st.session_state.outfit["base_item"]
        recommended_items = st.session_state.outfit["recommended_items"]
        
        st.write(f"**Base item:** {base_item['item_type']} — {base_item['color']}, {base_item['material']}, {base_item['gender']}, {base_item['style']}")
        
        if recommended_items:
            st.write("**Recommended items to complete your look:**")
            for item in recommended_items:
                st.write(f"- {item['item_type']} — {item['color']}, {item['material']}, {item['gender']}, {item['style']}")
        else:
            st.write("No additional items found for this look.")
        
        # Feedback buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👍 I like it"):
                SessionState.set_feedback(liked=True)
                SessionState.navigate_to("feedback")
                st.rerun()
                
        with col2:
            if st.button("👎 I don't like it, show me other options"):
                SessionState.set_feedback(liked=False)
                SessionState.navigate_to("clarify_feedback")
                st.rerun() 