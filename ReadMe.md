# Student Analytics App

## Overview
The Student Analytics App is a web application built with Flask that allows for the management of student data, including grades and attendance. The application provides interfaces for both administrators and students, enabling efficient data handling and visualization.

## Features
- User registration and login
- Admin interface for uploading student grades via CSV files
- Student interface for viewing grades, timetable, and subject selection
- Visualization of average scores and attendance

## Project Structure
```
student-analytics-app
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── templates               # HTML templates
│   ├── frontend.html       # Main user interface
│   ├── admin.html          # Admin interface for CSV uploads
│   └── student.html        # Student interface for grades and timetable
├── static                  # Static files
│   ├── css
│   │   └── style.css       # CSS styles for the application
│   └── js
│       └── main.js         # JavaScript for frontend interactions
├── uploads                 # Directory for uploaded CSV files
└── README.md               # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd student-analytics-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage
- **Admin Functions**: Admins can register users and upload student grades through the admin interface.
- **Student Functions**: Students can log in to view their grades, timetable, and subject selection options.

## Future Development
- Implement the timetable and subject selection features.
- Enhance the user interface with improved styling and layout.
- Add error handling and validation for file uploads.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.