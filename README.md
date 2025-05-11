# Look Builder

This is a project for S25-HAIID course at Innopolis University

## Description

Look Builder is a fashion styling assistant that helps users create stylish outfits based on their preferences. The application uses similarity matching to recommend clothing items and complete outfits, implementing interactive Human-AI Interaction Design patterns.

## Features

- Input clothing preferences (type, color, material, gender)
- Get suggested items based on your preferences
- Receive complete outfit recommendations
- Provide feedback to improve recommendations
- Iterative outfit generation based on feedback
- Admin dashboard for analyzing user feedback

## Technologies Used

- Streamlit for the user interface
- Python 3.8+
- scikit-learn for similarity matching
- pandas and numpy for data processing

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On Mac/Linux: `source .venv/bin/activate`
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```
3. The application will open in your default web browser
4. To access the admin dashboard:
   ```
   streamlit run admin_dashboard.py
   ```

## Project Structure

- `main.py`: Entry point and main application logic
- `admin_dashboard.py`: Dashboard for analyzing user feedback
- `screens/`: Contains modular UI screens
  - `input_preferences.py`: Screen for users to specify initial preferences
  - `loading.py` & `outfit_loading.py`: Loading screens
  - `suggested_items.py`: Shows items matching user preferences 
  - `suggested_outfits.py`: Displays complete outfit options
  - `clarify_feedback.py`: Allows users to provide detailed feedback
  - `final_look.py`: Presents the final recommended outfit
  - `feedback.py`: Collects user feedback on recommendations
- `utils/`: 
  - `session_state.py`: Manages application state and recommendation algorithms
  - `mock_data.py`: Contains clothing item data
  - `feedback_analyzer.py`: Processes and analyzes user feedback

## Application Flow

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

### Information on addressing HAIID principles and patterns can be found in the project report

## Contributing

This project was developed as part of a course assignment, but contributions are welcome through pull requests.

## License

See the LICENSE file for details.
