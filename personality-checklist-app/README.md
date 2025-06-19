# Personality Checklist App

## Overview
The Personality Checklist App is a web application designed to help users explore their personality traits by answering a series of interactive questions. The results are then cross-referenced with the characteristics of the 12 apostles of Jesus Christ, providing users with insights into their personality in a fun and engaging way.

## Features
- Interactive questionnaire to assess personality traits.
- Results that align user traits with the characteristics of the 12 apostles.
- User-friendly interface with responsive design.
- Easy navigation through the application.

## Project Structure
```
personality-checklist-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── results.html
│   └── static
│       └── style.css
├── tests
│   └── test_app.py
├── requirements.txt
├── config.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/personality-checklist-app.git
   ```
2. Navigate to the project directory:
   ```
   cd personality-checklist-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   flask run
   ```
2. Open your web browser and go to `http://127.0.0.1:5000` to access the app.
3. Follow the prompts to complete the personality checklist and view your results.

## Testing
To run the tests, use the following command:
```
pytest tests/test_app.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.