import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items
import time

def render():
    """Render the Suggested Items screen using the custom embedder and mock dataset"""
    st.header("Suggested Items")

    # Get user preferences from session state
    preferences = st.session_state.user_preferences

    # Find best matches using the scalable embedder
    suggested = SessionState.find_best_matches(preferences, clothing_items, top_k=3)
    st.session_state.suggested_items = suggested

    with st.container():
        st.subheader("Please select the item that best matches your preferences:")

        for item in st.session_state.suggested_items:
            with st.container():
                st.write(f"**Type:** {item['item_type']}")
                st.write(f"Color: {item['color']}, Material: {item['material']}, Gender: {item['gender']}, Style: {item['style']}")

                if st.button(f"Select", key=f"select_{item['id']}"):
                    SessionState.select_item(item)
                    SessionState.navigate_to("loading")
                    time.sleep(1)
                    SessionState.navigate_to("suggested_look")
                    st.rerun()

            st.divider()

        if st.button("Done"):
            if st.session_state.selected_item is not None:
                SessionState.navigate_to("loading")
                st.rerun()
            else:
                st.error("Please select an item first")
                time.sleep(2)
                st.rerun()

        if st.button("See more options"):
            st.info("This feature will be available in a future update")
            time.sleep(2)
            st.rerun() 