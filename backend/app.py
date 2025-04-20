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

if __name__ == '__main__':
    app.run()
