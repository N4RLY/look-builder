# Look Builder: Project Report

## 1. Overview

**Look Builder** is an interactive fashion styling assistant developed for the S25-HAIID course at Innopolis University. The application helps users create stylish outfits tailored to their preferences using similarity matching. The system iteratively improves recommendations based on user feedback, aiming to provide a personalized and engaging experience.

---

## 2. Stack and Technologies Used

### Backend & Core Logic
- **Python 3.8+**: The primary programming language for all application logic.
- **scikit-learn**: Utilized for cosine similarity calculations between item embeddings.
- **pandas, numpy**: For data manipulation and processing.

### Frontend
- **Streamlit**: Provides a rapid, interactive web interface for the application, allowing for quick prototyping and user-friendly design.

### Project Structure
- `main.py`: Entry point and main application logic, controlling screen navigation.
- `screens/`: Contains modular UI screens (input_preferences, suggested_items, loading, suggested_look, etc.).
- `utils/`: 
  - `session_state.py`: Manages application state across screens and contains recommendation logic.
  - `mock_data.py`: Provides clothing item data for the application.

### Dependency Management
- All dependencies are listed in `requirements.txt`:
  - streamlit==1.28.0
  - pandas==2.0.3
  - numpy==1.24.3
  - scikit-learn==1.2.2

---

## 3. Approach

### User Flow
1. **Input Preferences** (`input_preferences.py`): Users specify clothing preferences (type, color, material, gender).
2. **Suggested Items** (`suggested_items.py`): The system suggests items matching the preferences using similarity matching.
3. **Suggested Outfits** (`suggested_outfits.py`): Complete outfit options are generated based on the selected item.
4. **Suggested Look** (`suggested_look.py`): A complete outfit is presented with item details.
5. **Clarification Feedback** (`clarify_feedback.py`): Users can provide more detailed feedback if needed.
6. **Feedback** (`feedback.py`): Users can provide feedback on the suggested outfit.
7. **Final Look** (`final_look.py`): The final recommended outfit is presented, with explanations for each choice.

### Recommendation Engine
- **Similarity Calculation**: The system uses cosine similarity to find the most similar items to the user's query.
- **Outfit Generation**: The `recommend_outfit` method assembles a coherent outfit based on the style of a selected base item, matching items from different categories.
- **Data Structure**: Clothing items are organized in the mock_data.py file with detailed attributes (id, item_type, color, material, style, etc.).

### Modularity
- Each screen is implemented as a separate module in the `screens` directory, making the codebase maintainable and extensible.
- Session state is managed centrally through the `SessionState` class to ensure a smooth multi-step user experience.
- The application uses a component-based design pattern where each screen is responsible for its own rendering and state management.

---

## 4. Future Work

Several features and improvements are planned for future updates:

- **Custom Outfit Embedder**: Develop and integrate a custom embedding model trained on a dataset of real outfits, so that compatible clothing items are close in vector space.
- **Outfit Dataset Integration**: Curate or acquire a dataset of real-world outfits to train and evaluate a custom embedder, improving the quality and realism of recommendations.
- **LLM-Driven Feedback Evaluation**: Incorporate large language models to interpret and evaluate user feedback, enabling more nuanced adjustments to recommendations.
- **Expanded Item Catalog**: Add more diverse clothing items with additional attributes and categories to the dataset.
- **Image Integration**: Incorporate images for clothing items to enhance the user experience.
- **Enhanced Personalization**: Implement user profiles to store preferences and past selections for more personalized recommendations.
- **Mobile Optimization**: Improve the UI for mobile devices using Streamlit's responsive design capabilities.
- **Accessibility Improvements**: Ensure the app is usable by people with disabilities by following web accessibility guidelines.

---

## 5. Conclusion

The current implementation provides a functional styling assistant with similarity-based recommendations and a multi-step user experience. The next major steps are to build a custom outfit embedder using real outfit data and to leverage LLMs for smarter feedback handling and recommendation refinement.
