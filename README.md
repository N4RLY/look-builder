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

1. User inputs preferences (type, color, material, gender)
2. System suggests matching items using similarity algorithms
3. User selects a preferred item
4. System generates complete outfit options based on the selected item
5. User provides context or additional feedback if needed
6. System presents final outfit with explanations for each choice
7. User provides feedback to improve future recommendations

## Human-AI Interaction Design

The project implements several HAID patterns:
- User-supervised automation for outfit suggestions
- Feedback collection mechanisms for continuous improvement
- Clear explanations for why specific items were selected
- Adaptive recommendations based on user preferences and context

## Documentation

For more detailed information about the project, including the full approach, future work, and HAID design principles, please see `documentation.md`.

## Contributing

This project was developed as part of a course assignment, but contributions are welcome through pull requests.

## License

See the LICENSE file for details.
