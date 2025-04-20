from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        connection_timeout=5,
        auth_plugin='mysql_native_password',
        use_pure=True,
        allow_local_infile=True,
        raise_on_warnings=True
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/courses')
def courses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT Courses.id, Courses.name, Courses.description, Courses.credits, Professors.name AS professor
        FROM Courses
        LEFT JOIN Professors ON Courses.professor_id = Professors.id
    """)
    courses = cursor.fetchall()
    conn.close()
    return render_template('courses.html', courses=courses)

@app.route('/enrollments', methods=['GET', 'POST'])
def enrollments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get course list for the dropdown
    cursor.execute("SELECT id, name FROM Courses")
    courses = cursor.fetchall()

    students = []
    selected_course_id = None

    if request.method == 'POST':
        selected_course_id = request.form['course_id']
        cursor.execute("""
            SELECT Students.id, Students.name, Students.email, Enrollments.grade
            FROM Enrollments
            JOIN Students ON Enrollments.student_id = Students.id
            WHERE Enrollments.course_id = %s
        """, (selected_course_id,))
        students = cursor.fetchall()

    conn.close()
    return render_template('enrollments.html', courses=courses, students=students, selected_course_id=selected_course_id)

@app.route('/students/<int:student_id>')
def student_detail(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get student info
    cursor.execute("SELECT * FROM Students WHERE id = %s", (student_id,))
    student = cursor.fetchone()

    # Get student's courses and grades
    cursor.execute("""
        SELECT Courses.name AS course_name, Enrollments.grade
        FROM Enrollments
        JOIN Courses ON Enrollments.course_id = Courses.id
        WHERE Enrollments.student_id = %s
    """, (student_id,))
    courses = cursor.fetchall()

    # Calculate average grade
    cursor.execute("""
        SELECT AVG(grade) AS avg_grade
        FROM Enrollments
        WHERE student_id = %s
    """, (student_id,))
    avg_result = cursor.fetchone()
    avg_grade = avg_result['avg_grade'] if avg_result['avg_grade'] is not None else "N/A"

    conn.close()
    return render_template('student_detail.html', student=student, courses=courses, avg_grade=avg_grade)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    enrollment_date = request.form['enrollment_date']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Students (name, email, enrollment_date)
        VALUES (%s, %s, %s)
    """, (name, email, enrollment_date))
    conn.commit()
    conn.close()
    return redirect(url_for('students'))

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('students'))



if __name__ == '__main__':
    app.run()
