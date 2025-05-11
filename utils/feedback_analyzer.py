import pandas as pd
import os
import matplotlib.pyplot as plt
import streamlit as st

class FeedbackAnalyzer:
    """Utility class for analyzing feedback data"""
    
    @staticmethod
    def load_feedback_data(csv_path="feedback_data.csv"):
        """Load feedback data from CSV file"""
        if not os.path.isfile(csv_path):
            return None
        
        try:
            return pd.read_csv(csv_path)
        except Exception as e:
            print(f"Error loading feedback data: {e}")
            return None
    
    @staticmethod
    def get_summary_stats(data):
        """Get summary statistics for feedback data"""
        if data is None or len(data) == 0:
            return None
        
        summary = {
            "total_entries": len(data),
            "avg_rating": data["rating"].mean() if "rating" in data.columns else None,
            "liked_count": data["liked"].sum() if "liked" in data.columns else None,
            "disliked_count": len(data) - data["liked"].sum() if "liked" in data.columns else None
        }
        
        return summary
    
    @staticmethod
    def plot_ratings_distribution(data):
        """Plot the distribution of ratings"""
        if data is None or "rating" not in data.columns:
            return None
        
        fig, ax = plt.subplots()
        data["rating"].value_counts().sort_index().plot(kind="bar", ax=ax)
        ax.set_xlabel("Rating")
        ax.set_ylabel("Count")
        ax.set_title("Distribution of Ratings")
        
        return fig
    
    @staticmethod
    def plot_preferences_distribution(data, preference_col):
        """Plot the distribution of a specific preference"""
        if data is None or preference_col not in data.columns:
            return None
        
        fig, ax = plt.subplots()
        data[preference_col].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_title(f"Distribution of {preference_col}")
        
        return fig
    
    @staticmethod
    def export_to_excel(data, output_path="feedback_analysis.xlsx"):
        """Export feedback data to Excel with additional analysis"""
        if data is None:
            return None
        
        with pd.ExcelWriter(output_path) as writer:
            # Write raw data
            data.to_excel(writer, sheet_name="Raw Data", index=False)
            
            # Write summary stats
            summary = FeedbackAnalyzer.get_summary_stats(data)
            if summary:
                pd.DataFrame([summary]).to_excel(writer, sheet_name="Summary", index=False)
            
            # Write pivot tables
            if "item_type" in data.columns and "rating" in data.columns:
                pivot = pd.pivot_table(
                    data, 
                    values="rating", 
                    index="item_type", 
                    aggfunc=["mean", "count"]
                )
                pivot.to_excel(writer, sheet_name="Item Type Analysis")
            
            if "color" in data.columns and "rating" in data.columns:
                pivot = pd.pivot_table(
                    data, 
                    values="rating", 
                    index="color", 
                    aggfunc=["mean", "count"]
                )
                pivot.to_excel(writer, sheet_name="Color Analysis")
        
        return output_path 