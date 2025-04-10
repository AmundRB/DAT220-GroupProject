CREATE DATABASE IF NOT EXISTS course_management;
USE course_management;

CREATE TABLE Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL
);

CREATE TABLE Professors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL
);

CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT NOT NULL,
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES Professors(id) ON DELETE SET NULL
);

CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE NOT NULL,
    grade DECIMAL(4,2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(id) ON DELETE CASCADE
);

CREATE TABLE Assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    title VARCHAR(200) NOT NULL,
    due_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Courses(id) ON DELETE CASCADE
);
