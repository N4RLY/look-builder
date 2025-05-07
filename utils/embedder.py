import json
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ClothingEmbedder:
    """Embedder class for clothing items using sentence-transformers"""
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """Initialize the embedder with a model"""
        self.model = SentenceTransformer(model_name)
        self.clothing_items = {}
        self.embeddings = {}
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
            
    def generate_embeddings(self):
        """Generate embeddings for all clothing items"""
        if not self.item_list:
            print("No clothing items loaded. Please load data first.")
            return False
            
        # Create text descriptions for embedding
        texts = []
        for item in self.item_list:
            # Combine relevant fields for embedding
            text = f"{item['name']} {item['description']} {item['type']} {item['color']} {item['material']} {item['style']}"
            texts.append(text)
            
        # Generate embeddings
        embeddings = self.model.encode(texts)
        
        # Store embeddings with their item IDs
        self.embeddings = {item['id']: embedding for item, embedding in zip(self.item_list, embeddings)}
        
        return True
        
    def find_similar_items(self, query_item: Dict[str, Any], top_n: int = 5) -> List[Dict[str, Any]]:
        """Find similar items based on embeddings"""
        if not self.embeddings:
            print("No embeddings available. Please generate embeddings first.")
            return []
            
        # Create a query text for embedding
        query_text = f"{query_item.get('type', '')} {query_item.get('color', '')} {query_item.get('material', '')}"
        
        # Generate embedding for the query
        query_embedding = self.model.encode(query_text)
        
        # Calculate similarity scores
        similarities = {}
        for item_id, embedding in self.embeddings.items():
            similarity = cosine_similarity([query_embedding], [embedding])[0][0]
            similarities[item_id] = similarity
            
        # Sort by similarity and get top N
        sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        
        # Find the actual items
        result_items = []
        for item_id, _ in sorted_items[:top_n]:
            for item in self.item_list:
                if item['id'] == item_id and item['type'] == query_item.get('type', ''):
                    result_items.append(item)
                    break
        
        return result_items
        
    def generate_outfit(self, base_item: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete outfit based on a base item"""
        outfit = {"base_item": base_item, "recommended_items": []}
        
        # Get the style from the base item
        base_style = base_item.get('style', '')
        
        # Find matching items for different categories
        categories = ["pants", "shoes", "accessories"]
        if base_item['type'] == 'pants':
            categories = ["shirts", "shoes", "accessories"]
            
        for category in categories:
            category_items = []
            for item in self.item_list:
                if item['type'] in category and item['style'] == base_style:
                    category_items.append(item)
            
            # Add the best matching item from this category
            if category_items:
                outfit["recommended_items"].append(category_items[0])
        
        return outfit 