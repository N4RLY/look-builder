import streamlit as st
import pandas as pd
import os
import sys
from pathlib import Path

# Add the project root to path
sys.path.append(str(Path(__file__).parent))

# Import utilities
from utils.feedback_analyzer import FeedbackAnalyzer

def main():
    """Main function to run the Admin Dashboard Streamlit app"""
    # Set page config
    st.set_page_config(
        page_title="Feedback Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("Feedback Dashboard")
    
    # Load feedback data
    feedback_data = FeedbackAnalyzer.load_feedback_data()
    
    if feedback_data is None or len(feedback_data) == 0:
        st.warning("No feedback data available. Please collect some feedback first.")
        return
    
    # Display summary statistics
    st.header("Summary Statistics")
    summary = FeedbackAnalyzer.get_summary_stats(feedback_data)
    if summary:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Feedback Entries", summary["total_entries"])
        with col2:
            st.metric("Average Rating", f"{summary['avg_rating']:.2f}" if summary["avg_rating"] else "N/A")
        with col3:
            st.metric("Liked vs Disliked", f"{summary.get('liked_count', 0)} / {summary.get('disliked_count', 0)}")
    
    # Display charts
    st.header("Feedback Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Ratings Distribution")
        fig = FeedbackAnalyzer.plot_ratings_distribution(feedback_data)
        if fig:
            st.pyplot(fig)
        else:
            st.info("No rating data available.")
    
    with col2:
        preference_col = st.selectbox(
            "Select preference to analyze:",
            ["item_type", "color", "material", "gender"],
            index=0
        )
        fig = FeedbackAnalyzer.plot_preferences_distribution(feedback_data, preference_col)
        if fig:
            st.pyplot(fig)
        else:
            st.info(f"No {preference_col} data available.")
    
    # Display raw data
    st.header("Raw Feedback Data")
    st.dataframe(feedback_data)
    
    # Export option
    st.header("Export Data")
    if st.button("Export to Excel"):
        output_path = FeedbackAnalyzer.export_to_excel(feedback_data)
        if output_path:
            st.success(f"Data exported to {output_path}")
            
            # Create a download button for the exported file
            with open(output_path, "rb") as file:
                st.download_button(
                    label="Download Excel file",
                    data=file,
                    file_name="feedback_analysis.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

if __name__ == "__main__":
    main() 