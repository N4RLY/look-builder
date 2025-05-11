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

## 6. Human-AI Interaction Design

### System Classification [1]
- **Initiation Spectrum**: Human-as-prompter model where users initiate interactions by specifying preferences and contexts
- **Intelligence Scope**: Performs both analysis (clothing classification) and synthesis (outfit recommendations)
- **Cognitive Mode**: Combines rational analysis (matching style categories) with interpretive understanding (contextual appropriateness)

### HAID Design Principles [2]
- **AI Capabilities**:
  - Recognition: Classifies clothing items based on user descriptions
  - Reasoning: Applies style matching logic to create cohesive outfits
  - Generation: Creates complete outfit recommendations adapted to context

- **Interactive Attributes**:
  - Directability: Users guide the system through preferences and contextual specifications
  - Adaptability: System incorporates feedback to improve recommendations
  - Transparency: Explanations provided for why items were selected together

- **Trust Enablers**:
  - Clear explanations for styling choices in the final look screen
  - Feedback collection to demonstrate user input is valued
  - Confidence signals about style combinations

### Human-AI Collaboration
- **Collective Goals**: Combine human preference with AI style analysis to create contextually appropriate outfits
- **Task Allocation**:
  - Human: Providing preferences, specifying contexts, evaluating recommendations
  - AI: Style analysis, outfit generation, incorporating feedback

- **Interaction Flow**:
  1. User inputs initial preferences
  2. System suggests matching items
  3. User selects preferred item
  4. System generates complete outfit
  5. User provides context refinement
  6. System adjusts recommendations iteratively
  7. User offers feedback

### Addressing Design Challenges
- **Capability Uncertainty**: Implemented continuous feedback loop to improve system performance across diverse user contexts
- **Output Complexity**: 
  - Context-aware recommendations to ensure appropriate outfit suggestions
  - Clear explanations for why items work together
  
### User Explainability Features
- **Why This Outfit**: Explanations for why specific items complement each other
- **Performance Understanding**: Clear communication of system capabilities and limitations
- **What-If Scenarios**: Support for context changes to see how recommendations adapt

### Evaluation Metrics
- **Objective Fulfillment Rate**: Percentage of accepted outfit recommendations
- **Feedback Impact**: Improvement in recommendations after user feedback
- **Adaptability**: System's ability to adjust based on contextual inputs
- **Trust Development**: User-reported trust ratings after multiple interactions

---

## 7. Design Patterns

The Look Builder system implements several established Human-AI Interaction Design patterns to ensure a user-friendly, effective, and trustworthy experience.

### Value Assessment
- **Pattern 1: Determine if AI adds value**
  - The system solves the problem of choosing complementary clothing items to create cohesive outfits
  - Creates value by saving time, offering fashion expertise, and helping users create stylish outfits without needing a human stylist

### Explanation Patterns
- **Pattern 2: Set the right expectations**
  - The system offers outfit suggestions rather than claiming to provide "perfect" outfits
  - Retry functionality acknowledges that initial recommendations may not always satisfy user needs
  
- **Pattern 3: Explain the benefit, not the technology**
  - Focus is on helping users create stylish outfits for specific contexts
  - User interactions center on style outcomes rather than showcasing underlying technology
  
- **Pattern 10: Explain for understanding**
  - Outfit descriptions focus on styling information with clear explanations of why items work together
  - Explanations prioritize style rationale over technical algorithm details

### Errors & Feedback
- **Pattern 4: Be accountable for errors**
  - System acknowledges potential mismatches by offering retry functionality
  - User feedback mechanisms allow for error reporting and continuous improvement
  
- **Pattern 6: Handle precision/recall trade-offs**
  - Optimized for precision in clothing classification to ensure accurate style matching
  - Prioritizes confident identification of fewer clothing types correctly over potential misclassifications
  
- **Pattern 12: Let users give feedback**
  - Users can provide good/bad ratings and add text clarifications
  - System incorporates feedback for improved suggestions and allows for retries

### Privacy Considerations
- **Pattern 7: Be transparent about privacy**
  - System explains how user preferences are stored and used
  - *Future improvement:* Add clearer explanations of data usage policies
  
- **Pattern 8: Make it safe to explore**
  - *Future improvement:* Implement a demo mode with sample outfit suggestions before requiring user preferences

### Confidence & Automation
- **Pattern 9: Determine how to show model confidence**
  - *Future improvement:* Include qualitative confidence indicators like "classic combination" vs. "experimental pairing"
  
- **Pattern 11: Automate according to risk**
  - System automates outfit suggestions while keeping humans in the decision loop
  - Low-risk nature of fashion recommendations allows for automated initial suggestions
  
- **Pattern 13: Let users supervise automation**
  - Users supervise the process by adding context (e.g., "going to theater")
  - Feedback mechanisms and retry options ensure users maintain control

### Data Patterns
- **Pattern 5: Invest early in good data practices**
  - System requires high-quality clothing item data for proper classification
  - *Improvement area:* Expand dataset to include more diverse clothing items
  
- **Pattern 14: Actively maintain your datasets**
  - *Future improvement:* Implement regular updates to stay current with evolving fashion trends
  - Use user feedback to continuously improve and refine the dataset
  
- **Pattern 15: Embrace noisy data**
  - System designed to handle varied user inputs and sometimes contradictory feedback
  - *Improvement area:* Enhance ability to interpret diverse contextual descriptions

### Implementation Challenges
The Look Builder system addresses several inherent challenges:

- **Context understanding:** Interpreting subjective terms like "formal" or "casual" that vary culturally
- **Personalization:** Balancing general style advice with individual preferences 
- **Subjective feedback:** Converting qualitative user comments into actionable improvements
- **Explainability:** Providing useful styling rationale without overwhelming users

### Pattern Prioritization
Based on the fashion styling assistant's needs, the following patterns were prioritized:

1. **Determine if AI adds value:** Ensuring genuine utility beyond manual outfit creation
2. **Let users supervise automation:** Giving users control over subjective fashion decisions
3. **Let users give feedback:** Enabling continuous improvement through user input
4. **Embrace noisy data:** Handling variable user inputs and clothing descriptions
5. **Set the right expectations:** Clarifying that suggestions are recommendations, not perfect solutions
6. **Explain the benefit:** Helping users understand why specific items were suggested
7. **Invest in good data practices:** Ensuring accurate clothing classification
8. **Automate according to risk:** Keeping humans in the loop while providing initial suggestions

---

## 8. Conclusion

The current implementation provides a functional styling assistant with similarity-based recommendations and a multi-step user experience. The next major steps are to build a custom outfit embedder using real outfit data and to leverage LLMs for smarter feedback handling and recommendation refinement.

---

## 9. References

[1] Song, B., Zhu, Q., & Luo, J. (2024). Human-AI collaboration by design. Proceedings of the Design Society, 4, 2247-2256. https://doi.org/10.1017/pds.2024.227

[2] Zhu, Q., Luo, J., Song, B., & Wang, X. (2024). HAIC Design Principles. arXiv preprint. https://arxiv.org/html/2407.19098v1

[3] Yang, Q., Steinfeld, A., Rosé, C., & Zimmerman, J. (2020). Re-examining Whether, Why, and How Human-AI Interaction Is Uniquely Difficult to Design. Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, 1-13. https://dl.acm.org/doi/pdf/10.1145/3313831.3376301

[4] Yang, Q., Steinfeld, A., & Zimmerman, J. (2021). Unremarkable AI: Fitting Intelligent Decision Support into Critical, Clinical Decision-Making Processes. arXiv preprint. https://arxiv.org/pdf/2110.10790

[5] Qin, M., & Wang, Z. (2024). Towards a Comprehensive Understanding of the Cognitive Psychology and Human-AI Interaction Design in Chatbot Creativity Support. Frontiers in Artificial Intelligence, 7. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1456486/full
