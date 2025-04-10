USE course_management;

INSERT INTO Students (name, email, enrollment_date) VALUES
('Alice Johnson', 'alice@example.com', '2023-09-01'),
('Bob Smith', 'bob@example.com', '2023-09-01');

INSERT INTO Professors (name, department) VALUES
('Dr. Brown', 'Computer Science'),
('Dr. Green', 'Mathematics');

INSERT INTO Courses (name, description, credits, professor_id) VALUES
('Database Systems', 'Introduction to relational databases.', 3, 1),
('Linear Algebra', 'Matrices and vectors.', 4, 2);

INSERT INTO Enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2023-09-05', 85.5),
(2, 1, '2023-09-05', 90.0),
(1, 2, '2023-09-06', 78.0);

INSERT INTO Assignments (course_id, title, due_date) VALUES
(1, 'SQL Basics', '2023-10-01'),
(2, 'Matrix Operations', '2023-10-05');
