import streamlit as st
from utils.session_state import SessionState
from utils.mock_data import clothing_items, outfits
import time

def find_all_outfits_with_item(item_id, outfits_data):
    """Find all outfits that contain the given item ID."""
    matching_outfits = []
    for outfit in outfits_data:
        if item_id in outfit:
            matching_outfits.append(outfit)
    return matching_outfits

def generate_alternative_outfits(selected_item, items, outfits_data, max_outfits=5):
    """Generate multiple outfit options for the selected item.
    
    Returns a list of outfit dictionaries, each containing:
    - "outfit_items": List of item dictionaries for all items in the outfit
    - "outfit_ids": The raw outfit IDs
    """
    # First, find exact outfits containing this item
    exact_outfits = find_all_outfits_with_item(selected_item["id"], outfits_data)
    
    # Convert to list of outfit dictionaries
    outfit_options = []
    id_to_item = {item["id"]: item for item in items}
    
    # Add exact matches first
    for outfit_ids in exact_outfits:
        outfit_items = [id_to_item[item_id] for item_id in outfit_ids if item_id in id_to_item]
        outfit_options.append({
            "outfit_items": outfit_items,
            "outfit_ids": outfit_ids
        })
    
    # If we don't have enough, add suggested outfits based on co-occurrence similarity
    if len(outfit_options) < max_outfits:
        # Get suggested outfit based on co-occurrence
        suggested = SessionState.recommend_outfit(selected_item, items, outfits_data)
        
        # Only add if it's not already in our options
        suggested_ids = [item["id"] for item in suggested["recommended_items"]] + [selected_item["id"]]
        suggested_ids.sort()  # Sort for consistent comparison
        
        # Check if this suggested outfit is already in our list
        is_duplicate = False
        for existing in outfit_options:
            existing_ids = sorted([item["id"] for item in existing["outfit_items"]])
            if existing_ids == suggested_ids:
                is_duplicate = True
                break
        
        if not is_duplicate and suggested["recommended_items"]:
            outfit_options.append({
                "outfit_items": [selected_item] + suggested["recommended_items"],
                "outfit_ids": suggested_ids
            })
    
    return outfit_options[:max_outfits]

def render():
    """Render the Suggested Outfits screen - shows multiple outfit options for the selected item."""
    st.header("Choose Your Outfit")
    
    # Get the selected item from session state
    selected_item = st.session_state.selected_item
    if selected_item is None:
        st.error("No item selected. Please go back and select an item first.")
        if st.button("Go Back"):
            SessionState.navigate_to("suggested_items")
            st.rerun()
        return
    
    # Display the selected item
    st.subheader("Your Selected Item")
    st.write(f"**{selected_item['item_type']}** — {selected_item['color']}, {selected_item['material']}, {selected_item['gender']}, {selected_item['style']}")
    
    # Generate multiple outfit options
    outfit_options = generate_alternative_outfits(selected_item, clothing_items, outfits, max_outfits=3)
    
    if not outfit_options:
        st.warning("No outfit options found for this item. Let's try our recommendation system.")
        # Use the base recommendation system directly
        outfit = SessionState.recommend_outfit(selected_item, clothing_items, outfits)
        SessionState.set_outfit(outfit)
        SessionState.navigate_to("suggested_look")
        st.rerun()
    
    # Show the outfit options
    st.subheader("Choose an outfit option:")
    
    for i, outfit_option in enumerate(outfit_options):
        with st.container():
            st.write(f"**Outfit Option {i+1}**")
            st.write("Items in this outfit:")
            for item in outfit_option["outfit_items"]:
                if item["id"] == selected_item["id"]:
                    st.write(f"• **{item['item_type']}** — {item['color']}, {item['material']} (Your selected item)")
                else:
                    st.write(f"• {item['item_type']} — {item['color']}, {item['material']}, {item['gender']}, {item['style']}")
            
            # Button to select this outfit
            if st.button(f"Choose Outfit {i+1}", key=f"choose_outfit_{i}"):
                # Create the outfit dictionary in the expected format
                outfit_dict = {
                    "base_item": selected_item,
                    "recommended_items": [item for item in outfit_option["outfit_items"] if item["id"] != selected_item["id"]]
                }
                SessionState.set_outfit(outfit_dict)
                SessionState.navigate_to("suggested_look")
                st.rerun()
            
            st.divider()
    
    # Button to go back to item selection
    if st.button("Go Back to Item Selection"):
        SessionState.navigate_to("suggested_items")
        st.rerun() 