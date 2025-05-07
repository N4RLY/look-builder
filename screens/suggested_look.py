import streamlit as st
from utils.session_state import SessionState

def render():
    """Render the Suggested Look screen"""
    st.header("Screen 4: Suggested Look")
    
    if st.session_state.outfit is None:
        st.error("No outfit recommendation found. Please start over.")
        if st.button("Start Over"):
            SessionState.reset()
            SessionState.navigate_to("input_preferences")
            st.experimental_rerun()
        return
    
    with st.container():
        st.subheader("Your suggested look:")
        
        # Get the base item and recommendations
        base_item = st.session_state.outfit["base_item"]
        recommended_items = st.session_state.outfit["recommended_items"]
        
        # Create a box for the outfit details
        with st.container():
            st.write("### Why this look:")
            st.write(f"You selected a **{base_item['color']} {base_item['material']} {base_item['type']}** — a perfect base for an elegant and versatile office style.")
            
            st.write("**Recommended outfit:**")
            
            # List each recommended item with bullets
            for item in recommended_items:
                if "pants" in item["type"]:
                    st.write(f"• **Trousers:** {item['color']} {item['material']} {item['name'].split()[0]}")
                elif "shoes" in item["type"]:
                    st.write(f"• **Shoes:** {item['color']} {item['material']} {item['name'].split()[0]}")
                elif "accessories" in item["type"]:
                    st.write(f"• **Accessories:** {item['description']}")
            
            # Add optional jacket if available
            st.write("• **Optional jacket:** Lightweight wool blazer in a neutral color (grey or dark blue)")
            
            # Add style and usage context
            st.write(f"**Look style:** {base_item['style']}")
            st.write("**Usage context:**")
            st.write(f"{base_item['usage_context']}")
        
        # Feedback buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👍 I like it"):
                # Store positive feedback
                SessionState.set_feedback(liked=True)
                # Navigate to final look
                SessionState.navigate_to("final_look")
                st.experimental_rerun()
                
        with col2:
            if st.button("👎 I don't like it, show me other options"):
                # Navigate to clarify feedback
                SessionState.set_feedback(liked=False)
                SessionState.navigate_to("clarify_feedback")
                st.experimental_rerun() 