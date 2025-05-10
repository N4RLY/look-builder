import streamlit as st
from utils.session_state import SessionState
from utils.simple_embedder import SimpleEmbedder
import time

def render(embedder: SimpleEmbedder):
    """Render the Suggested Items screen"""
    st.header("Suggested Items")
    
    with st.container():
        st.subheader("Please select the item that best matches yours:")
        
        # Display each suggested item as a clickable option
        for item in st.session_state.suggested_items:
            with st.container():
                st.write(f"**{item['name']}**")
                st.write(f"Description: {item['description']}")
                
                # Create a button for each item
                if st.button(f"Select", key=f"select_{item['id']}"):
                    # Select this item
                    SessionState.select_item(item)
                    
                    # Move to loading screen
                    SessionState.navigate_to("loading")
                    
                    # Generate outfit recommendation
                    outfit = embedder.generate_outfit(item)
                    SessionState.set_outfit(outfit)
                    
                    # Give a brief pause for loading screen visibility
                    time.sleep(2)
                    
                    # Navigate to suggested look screen
                    SessionState.navigate_to("suggested_look")
                    st.rerun()
            
            # Add a separator between items
            st.divider()
        
        # Add "Done" button at the bottom
        if st.button("Done"):
            if st.session_state.selected_item is not None:
                # If an item was selected, navigate to loading
                SessionState.navigate_to("loading")
                st.rerun()
            else:
                # If no item was selected, show error
                st.error("Please select an item first")
                time.sleep(2)
                st.rerun()
                
        # Show more options button (not implemented in MVP)
        if st.button("See more options"):
            st.info("This feature will be available in a future update")
            time.sleep(2)
            st.rerun() 