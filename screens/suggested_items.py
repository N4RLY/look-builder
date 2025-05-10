import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items
import time

def filter_items_by_preferences(items, preferences):
    """Filter items by non-empty user preferences (exact match)."""
    filtered = []
    for item in items:
        match = True
        for key, value in preferences.items():
            if value and item.get(key) != value:
                match = False
                break
        if match:
            filtered.append(item)
    return filtered

def render():
    """Render the Suggested Items screen using the custom embedder and mock dataset"""
    st.header("Suggested Items")

    # Get user preferences from session state
    preferences = st.session_state.user_preferences

    # Use attribute-based filtering for core item selection
    all_suggested = filter_items_by_preferences(clothing_items, preferences)
    st.session_state.suggested_items_all = all_suggested

    # Track pagination index in session state
    if 'suggested_items_index' not in st.session_state:
        st.session_state.suggested_items_index = 0
    page_size = 3
    start = st.session_state.suggested_items_index
    end = start + page_size
    current_batch = all_suggested[start:end]
    total = len(all_suggested)

    with st.container():
        st.subheader("Please select the item that best matches your preferences:")

        for item in current_batch:
            with st.container():
                st.write(f"**Type:** {item['item_type']}")
                st.write(f"Color: {item['color']}, Material: {item['material']}, Gender: {item['gender']}, Style: {item['style']}")

                if st.button(f"Select", key=f"select_{item['id']}"):
                    SessionState.select_item(item)
                    SessionState.navigate_to("loading")
                    time.sleep(1)
                    SessionState.navigate_to("suggested_outfits")
                    st.rerun()

            st.divider()

        # Pagination controls
        col1, col2, col3 = st.columns([1,2,1])
        with col1:
            if st.session_state.suggested_items_index > 0:
                if st.button("Back"):
                    st.session_state.suggested_items_index = max(0, st.session_state.suggested_items_index - page_size)
                    st.rerun()
            else:
                st.write("")
        with col2:
            st.markdown(f"<div style='text-align:center; font-size:0.95rem;'>Page {start//page_size+1} of {((total-1)//page_size)+1}</div>", unsafe_allow_html=True)
        with col3:
            if end < total:
                if st.button("See more options"):
                    st.session_state.suggested_items_index += page_size
                    st.rerun()
            else:
                st.write("") 