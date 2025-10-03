from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pandas as pd
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # IMPORTANT: Change this to a strong, unique secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#models for the timetable

import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# loading the dataset
csv = pd.read_csv(r"C:\Users\USER\Desktop\@CaxtoneTechKenya\student analytics\model for study hours prediction\Hours.csv")

# clean the data (inplace)
csv.dropna(inplace=True)

# drop all rows that have at least one zero value
csv = csv.loc[(csv != 0).all(axis=1)]

# setup the features target for each model
def mathe():
    return 7

def eng(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "RE", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("ENG", axis=1)
    y = df["ENG"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def kisw(data):
    df = csv.copy()
    df.drop(["RE", "ENG", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("KISW", axis=1)
    y = df["KISW"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def bio(data):
    df = csv.copy()
    df.drop(["KISW", "ENG", "PHY", "CHE", "RE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("BIO", axis=1)
    y = df["BIO"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def phy(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "ENG", "CHE", "RE", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("PHY", axis=1)
    y = df["PHY"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def che(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "RE", "ENG", "HIST", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("CHE", axis=1)
    y = df["CHE"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def hist(data):
    df = csv.copy()
    df.drop(["RE", "KISW", "BIO", "PHY", "CHE", "ENG", "GEO", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("HIST", axis=1)
    y = df["HIST"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def geo(data):
    df = csv.copy()
    df.drop(["RE", "KISW", "BIO", "PHY", "CHE", "HIST", "ENG", "COMP", "BUS", "MATH"], axis=1, inplace=True)
    X = df.drop("GEO", axis=1)
    y = df["GEO"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def comp(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "ENG", "BUS", "MATH", "RE"], axis=1, inplace=True)
    X = df.drop("COMP", axis=1)
    y = df["COMP"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def bus(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "ENG", "MATH", "RE"], axis=1, inplace=True)
    X = df.drop("BUS", axis=1)
    y = df["BUS"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def re(data):
    df = csv.copy()
    df.drop(["KISW", "BIO", "PHY", "CHE", "HIST", "GEO", "COMP", "BUS", "MATH", "ENG"], axis=1, inplace=True)
    X = df.drop("RE", axis=1)
    y = df["RE"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    data_df = pd.DataFrame(data, columns=X.columns)
    pred = model.predict(data_df)
    return math.trunc(pred[0])

def getPreds(MATHEMATICS, ENGLISH, KISWAHILI, BIOLOGY, PHYSICS, CHEMISTRY, HISTORY, GEOGRAPHY, COMPUTER, BUSINESS, CRE):
    total = ENGLISH + KISWAHILI + BIOLOGY + PHYSICS + CHEMISTRY + HISTORY + GEOGRAPHY + COMPUTER + BUSINESS + CRE
    feature_vector = [[MATHEMATICS, ENGLISH, KISWAHILI, BIOLOGY, PHYSICS, CHEMISTRY, HISTORY, GEOGRAPHY, COMPUTER, BUSINESS, CRE, total, 28]]  # example extended input
    math_pred = mathe()
    eng_pred = eng(feature_vector)
    kisw_pred = kisw(feature_vector)
    bio_pred = bio(feature_vector)
    phy_pred = phy(feature_vector)
    chem_pred = che(feature_vector)
    history_pred = hist(feature_vector)
    geo_pred = geo(feature_vector)
    comp_pred = comp(feature_vector)
    business_pred = bus(feature_vector)
    cre_pred = re(feature_vector)
    return [math_pred, eng_pred, kisw_pred, bio_pred, phy_pred, chem_pred, history_pred, geo_pred, comp_pred, business_pred, cre_pred]
#example usage here
#getPreds(5, 54, 55, 54, 34, 45, 7, 8, 9, 5, 8)
#-------------------------------------------------------------------

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(8), nullable=False)  # 'admin' or 'student'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    admission_number = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False) # For student login
    role = db.Column(db.String(8), nullable=False, default='student') # always 'student'

class GradeTrend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    mark = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(8), nullable=False)
    exam_date = db.Column(db.DateTime, default=datetime.now)

# Utility
def mark_to_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 75 and mark < 80:
        return "A-"
    elif mark >= 70 and mark < 75:
        return "B+"
    elif mark >= 65 and mark < 70:
        return "B"
    elif mark >= 60 and mark < 65:
        return "B-"
    elif mark >= 55 and mark < 60:
        return "C+"
    elif mark >= 50 and mark < 55:
        return "C"
    elif mark >= 45 and mark < 50:
        return "C-"
    elif mark >= 40 and mark < 45:
        return "D+"
    elif mark >= 35 and mark < 40:
        return "D"
    elif mark >= 30 and mark < 35:
        return "D-"
    else:
        return "E"

# Routes
@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/hours')
def predict_hours():
    # Use session to get logged-in user info
    user_id = session.get('user_id')
    role = session.get('role')

    if not user_id or role != 'student':
        return jsonify({'message': 'Access denied or not logged in as student'}), 403

    student = Student.query.get(user_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    # Fetch the latest marks for the student, per subject
    latest_grades = {}
    for subject in EXPECTED_COLUMNS - {'Admission_Number'}:
        grade_entry = GradeTrend.query.filter_by(student_id=student.id, subject=subject).order_by(GradeTrend.exam_date.desc()).first()
        if grade_entry:
            latest_grades[subject] = grade_entry.mark
        else:
            latest_grades[subject] = 0  # or default value if no marks available

    # Prepare input for getPreds with correct order and columns:
    # MATHEMATICS, ENGLISH, KISWAHILI, BIOLOGY, PHYSICS, CHEMISTRY, HISTORY, GEOGRAPHY, COMPUTER, BUSINESS, CRE
    # Fill missing marks with zero or appropriate default
    input_data = [
        latest_grades.get('MATHEMATICS', 0),
        latest_grades.get('ENGLISH', 0),
        latest_grades.get('KISWAHILI', 0),
        latest_grades.get('BIOLOGY', 0),
        latest_grades.get('PHYSICS', 0),
        latest_grades.get('CHEMISTRY', 0),
        latest_grades.get('HISTORY', 0),
        latest_grades.get('GEOGRAPHY', 0),
        latest_grades.get('COMPUTER', 0),
        latest_grades.get('BUSINESS', 0),
        latest_grades.get('CRE', 0),
    ]

    predicted_hours = getPreds(*input_data)

    # Map prediction to subject names for clarity
    subjects = ['MATHEMATICS', 'ENGLISH', 'KISWAHILI', 'BIOLOGY', 'PHYSICS', 'CHEMISTRY', 'HISTORY', 'GEOGRAPHY', 'COMPUTER', 'BUSINESS', 'CRE']
    predictions = dict(zip(subjects, predicted_hours))

    return jsonify({'admission_number': student.admission_number, 'predicted_hours': predictions}), 200

@app.route('/register', methods=['POST'])
def register_user(): # Renamed to avoid conflict with function name 'register'
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'User already exists'}), 400
    hashed_pw = generate_password_hash(data['password'])
    user = User(username=data['username'], password_hash=hashed_pw, role=data.get('role', 'student')) # Default role
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login_user(): # Renamed to avoid conflict with function name 'login'
    data = request.get_json()
    username_or_adm = data['username']
    password = data['password']

    user = User.query.filter_by(username=username_or_adm).first()
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        session['role'] = user.role
        return jsonify({'role': user.role, 'message': 'Logged in as Admin/User'}), 200

    student = Student.query.filter_by(admission_number=username_or_adm).first()
    if student and check_password_hash(student.password_hash, password):
        session['user_id'] = student.id
        session['role'] = student.role
        return jsonify({'role': student.role, 'message': 'Logged in as Student'}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'message': 'Logged out'}), 200

# Route for adding new students (creating their credentials)
@app.route('/students', methods=['GET', 'POST'])
def handle_students(): # Renamed to avoid conflict with function name 'students'
    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['name', 'admission_number', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Missing required fields for student creation.'}), 400

        if Student.query.filter_by(admission_number=data['admission_number']).first():
            return jsonify({'message': 'Student with this admission number already exists'}), 400

        password_hash = generate_password_hash(data['password'])
        student = Student(name=data['name'], admission_number=data['admission_number'], password_hash=password_hash)
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': 'Student credentials created successfully'}), 201
    else: # GET request to fetch all students
        students = Student.query.all()
        return jsonify([
            {'id': s.id, 'name': s.name, 'admission_number': s.admission_number}
            for s in students
        ])

# NEW: Route to add individual subject grades
@app.route('/grades', methods=['POST'])
def add_grade():
    data = request.get_json()
    admission_number = data.get('admission_number')
    subject = data.get('subject')
    mark = data.get('mark')

    if not all([admission_number, subject, mark is not None]):
        return jsonify({'message': 'Missing data (admission_number, subject, or mark).'}), 400

    student = Student.query.filter_by(admission_number=admission_number).first()
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    try:
        mark_value = float(mark)
        grade_value = mark_to_grade(mark_value)
        new_grade = GradeTrend(
            student_id=student.id,
            subject=subject,
            mark=mark_value,
            grade=grade_value,
            exam_date=datetime.now()
        )
        db.session.add(new_grade)
        db.session.commit()
        return jsonify({'message': 'Grade added successfully'}), 201
    except ValueError:
        return jsonify({'message': 'Invalid mark value. Must be a number.'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding grade: {str(e)}'}), 500

@app.route('/admin/student/<adm>')
def admin_student_dashboard(adm):
    student = Student.query.filter_by(admission_number=adm).first()
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    grades = GradeTrend.query.filter_by(student_id=student.id).all()
    # Calculate average mark for this student
    total_student_marks = sum(g.mark for g in grades) if grades else 0
    student_average_mark = (total_student_marks / len(grades)) if grades else 0

    return jsonify({
        'name': student.name,
        'admission_number': student.admission_number,
        'average_mark': round(student_average_mark, 2),
        'grades': [
            {'subject': g.subject, 'mark': g.mark, 'grade': g.grade, 'exam_date': g.exam_date.strftime('%Y-%m-%d')}
            for g in grades
        ],
        'class_position': '',  # To be implemented on a per-class basis
        'overall_position': ''  # To be implemented globally
    })

@app.route('/student/grades')
def student_grades():
    user_id = session.get('user_id')
    role = session.get('role')

    if not user_id or role != 'student':
        return jsonify({'message': 'Access denied or not logged in as student'}), 403

    student = Student.query.get(user_id)
    if not student:
        return jsonify({'message': 'Student not found in session'}), 404

    grades = GradeTrend.query.filter_by(student_id=student.id).all()
    # Calculate average mark for this student
    total_student_marks = sum(g.mark for g in grades) if grades else 0
    student_average_mark = (total_student_marks / len(grades)) if grades else 0

    return jsonify({
        'name': student.name,
        'admission_number': student.admission_number,
        'average_mark': round(student_average_mark, 2),
        'grades': [
            {'subject': g.subject, 'mark': g.mark, 'grade': g.grade, 'exam_date': g.exam_date.strftime('%Y-%m-%d')}
            for g in grades
        ],
        'class_position': '',
        'overall_position': ''
    })

@app.route('/student/trend')
def student_trend():
    user_id = session.get('user_id')
    role = session.get('role')

    if not user_id or role != 'student':
        return jsonify({'message': 'Access denied or not logged in as student'}), 403

    student = Student.query.get(user_id)
    if not student:
        return jsonify({'message': 'Student not found in session'}), 404

    trends = GradeTrend.query.filter_by(student_id=student.id).order_by(GradeTrend.exam_date.asc()).all() # Order by asc for trend analysis
    subject_marks = {}
    for t in trends:
        subject_marks.setdefault(t.subject, []).append(t.mark)

    dropped, added = [], []
    for subject, marks in subject_marks.items():
        if len(marks) >= 2: # Need at least two points to see a trend
            # Compare latest mark with earliest mark for a simple trend
            diff = marks[-1] - marks[0]
            if diff < 0:
                dropped.append({'subject': subject, 'extent': abs(diff)})
            elif diff > 0:
                added.append({'subject': subject, 'extent': diff})
    dropped.sort(key=lambda x: -x['extent'])
    added.sort(key=lambda x: -x['extent'])

    chart_trends = [] # Prepare data for charting
    for t in trends:
        chart_trends.append({
            'subject': t.subject,
            'mark': t.mark,
            'exam_date': t.exam_date.strftime('%Y-%m-%d')
        })

    return jsonify({'trends_data': chart_trends, 'dropped_subjects': dropped, 'added_subjects': added})


# NEW/ADJUSTED: Overall Visualization Endpoint (e.g., average mark across all students)
@app.route('/visualization')
def get_overall_visualization():
    all_grades = GradeTrend.query.all()
    if not all_grades:
        return jsonify({'average_mark': 0, 'subject_averages': {}}), 200

    total_marks = sum(g.mark for g in all_grades)
    overall_average_mark = total_marks / len(all_grades)

    # Calculate average mark per subject
    subject_marks_sum = {}
    subject_marks_count = {}
    for grade in all_grades:
        subject_marks_sum[grade.subject] = subject_marks_sum.get(grade.subject, 0) + grade.mark
        subject_marks_count[grade.subject] = subject_marks_count.get(grade.subject, 0) + 1

    subject_averages = {
        subject: round(subject_marks_sum[subject] / subject_marks_count[subject], 2)
        for subject in subject_marks_sum
    }

    return jsonify({
        'overall_average_mark': round(overall_average_mark, 2),
        'subject_averages': subject_averages
    }), 200


# Define the expected columns
EXPECTED_COLUMNS = {
    'Admission_Number', 'MATHEMATICS', 'ENGLISH', 'KISWAHILI', 
    'BIOLOGY', 'PHYSICS', 'CHEMISTRY', 'HISTORY', 'GEOGRAPHY', 
    'COMPUTER', 'BUSINESS', 'CRE'
}

# --- Other required imports and setup (e.g., db, Student, GradeTrend, mark_to_grade) ---

@app.route('/upload_grades', methods=['POST'])
def upload_grades():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)
    
    try:
        if filepath.lower().endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filepath.lower().endswith('.xlsx'):
            df = pd.read_excel(filepath)
        else:
            return jsonify({'message': 'Invalid file format. Only CSV and XLSX are supported.'}), 400
    except Exception as e:
        return jsonify({'message': f'Error reading file: {str(e)}'}), 400
        
    # --- New code to validate columns ---
    # Convert dataframe columns to a set for easy comparison
    uploaded_columns = set(df.columns.str.strip()) # .str.strip() handles potential whitespace in column names
    
    # Check if all expected columns are present
    if not EXPECTED_COLUMNS.issubset(uploaded_columns):
        missing = EXPECTED_COLUMNS - uploaded_columns
        return jsonify({'message': f'Missing required columns in the file: {", ".join(missing)}'}), 400
    
    # Check if there are any extra, unexpected columns
    extra_columns = uploaded_columns - EXPECTED_COLUMNS
    if extra_columns:
        return jsonify({'message': f'File contains invalid extra columns: {", ".join(extra_columns)}'}), 400

    grades_added = 0
    
    # Iterate through the DataFrame rows to process the grades
    for _, row in df.iterrows():
        admission_number = str(row['Admission_Number']).strip()
        student = Student.query.filter_by(admission_number=admission_number).first()
        
        if student:
            for subject in EXPECTED_COLUMNS - {'Admission_Number'}:
                try:
                    mark_value = float(row[subject])
                    grade_value = mark_to_grade(mark_value)
                    
                    trend = GradeTrend(
                        student_id=student.id,
                        exam_date=datetime.now(),
                        subject=subject,
                        mark=mark_value,
                        grade=grade_value
                    )
                    db.session.add(trend)
                    grades_added += 1
                except (ValueError, KeyError):
                    # Log or handle rows with invalid mark values gracefully
                    print(f"Skipping row for student {admission_number} due to invalid mark for subject {subject}.")
        else:
            print(f"Skipping row for unknown student with admission number: {admission_number}")
            
    db.session.commit()
    return jsonify({'message': f'{grades_added} grades uploaded and trends updated successfully.'})

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Ensure tables are created before running the app
    app.run(debug=True)