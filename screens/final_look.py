import streamlit as st
from utils.session_state import SessionState

def render():
    """Render the Final Look screen"""
    st.header("Final Look")
    
    if st.session_state.outfit is None:
        st.error("No outfit recommendation found. Please start over.")
        if st.button("Start Over"):
            SessionState.reset()
            SessionState.navigate_to("input_preferences")
            st.rerun()
        return
    
    with st.container():
        st.subheader("Your Look:")
        
        # Get the base item and recommendations
        base_item = st.session_state.outfit["base_item"]
        recommended_items = st.session_state.outfit["recommended_items"]
        
        # Create a box for the outfit details
        with st.container():
            st.write("### Why this look:")
            st.write(f"You selected a **{base_item['color']} {base_item['material']} {base_item['item_type']}** — a perfect base for an elegant and versatile office style.")
            
            st.write("### Recommended outfit:")
            
            # List each recommended item with bullets
            for item in recommended_items:
                if "pants" in item["item_type"]:
                    st.write(f"• **Trousers:** {item['color']} {item['material']}")
                elif "shoes" in item["item_type"]:
                    st.write(f"• **Shoes:** {item['color']} {item['material']}")
                elif "accessories" in item["item_type"]:
                    st.write(f"• **Accessories:** {item.get('description', '')}")
            
            # Add optional jacket if available
            st.write("• **Optional jacket:** Lightweight wool blazer in a neutral color (grey or dark blue)")
            
            # Add style and usage context
            st.write(f"##### Look style: {base_item['style']}")
            st.write(f"##### Usage context: {base_item.get('usage_context', 'No specific usage context provided.')}")
        
        # Thank you message
        st.write("Thank you for trusting me with your style!")
        st.write("I hope your new look brings you confidence and inspiration.")
        
        # Create another look button
        if st.button("Create another look", use_container_width=True):
            # Reset and start over
            SessionState.reset()
            SessionState.navigate_to("input_preferences")
            st.rerun() 