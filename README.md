# Look Builder

This is a project for S25-HAIID course at Innopolis University

## Description

Look Builder is a fashion styling assistant that helps users create stylish outfits based on their preferences. The application uses similarity matching to recommend clothing items and complete outfits.

## Features

- Input clothing preferences (type, color, material, gender)
- Get suggested items based on your preferences
- Receive complete outfit recommendations
- Provide feedback to improve recommendations
- Iterative outfit generation based on feedback

## Technologies Used

- Streamlit for the user interface
- Python 3.8+
- scikit-learn for similarity matching

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

## Project Structure

- `main.py`: Main application file
- `utils/`: 
  - `session_state.py`: Manages application state and contains recommendation algorithms
  - `mock_data.py`: Contains clothing item data
- `screens/`: Different screens/views of the application

## Contributing

This project was developed as part of a course assignment, but contributions are welcome through pull requests.

## License

See the LICENSE file for details.
