import json
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple
import numpy as np

class SimpleEmbedder:
    """Simple embedder class for clothing items that doesn't require external ML libraries"""
    
    def __init__(self):
        """Initialize the simple embedder"""
        self.clothing_items = {}
        self.item_list = []
        
    def load_clothing_data(self, data_path: str = 'data/clothing_items.json'):
        """Load clothing data from JSON file"""
        try:
            with open(data_path, 'r') as f:
                self.clothing_items = json.load(f)
                
            # Create a flat list of all items
            self.item_list = []
            for category, items in self.clothing_items.items():
                self.item_list.extend(items)
                
            return True
        except Exception as e:
            print(f"Error loading clothing data: {e}")
            return False
            
    def find_similar_items(self, query_item: Dict[str, Any], top_n: int = 5) -> List[Dict[str, Any]]:
        """Find similar items based on simple attribute matching"""
        if not self.item_list:
            print("No clothing items loaded. Please load data first.")
            return []
            
        # Filter items by type
        type_matches = [item for item in self.item_list if item['type'] == query_item.get('type', '')]
        
        # If no type matches, return empty list
        if not type_matches:
            return []
            
        # Calculate similarity scores based on attribute matching
        item_scores = []
        for item in type_matches:
            score = 0
            
            # Match on color
            if item['color'] == query_item.get('color', ''):
                score += 3
                
            # Match on material
            if item['material'] == query_item.get('material', ''):
                score += 2
                
            item_scores.append((item, score))
            
        # Sort by score (descending) and get top N
        sorted_items = sorted(item_scores, key=lambda x: x[1], reverse=True)
        result_items = [item for item, _ in sorted_items[:top_n]]
        
        return result_items
        
    def generate_outfit(self, base_item: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete outfit based on a base item"""
        outfit = {"base_item": base_item, "recommended_items": []}
        
        # Get the style from the base item
        base_style = base_item.get('style', '')
        
        # Find matching items for different categories
        categories = ["pants", "shoes", "accessories"]
        if base_item['type'] == 'pants':
            categories = ["shirt", "shoes", "accessories"]
            
        for category in categories:
            category_items = []
            for item in self.item_list:
                if item['type'] in category and item['style'] == base_style:
                    category_items.append(item)
            
            # Add the best matching item from this category
            if category_items:
                outfit["recommended_items"].append(category_items[0])
        
        return outfit 