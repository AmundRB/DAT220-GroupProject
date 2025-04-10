USE course_management;

INSERT INTO Students (name, email, enrollment_date) VALUES
('Alice Johnson', 'alice@example.com', '2023-09-01'),
('Bob Smith', 'bob@example.com', '2023-09-01'),
('Carol White', 'carol@example.com', '2023-09-02'),
('David Brown', 'david@example.com', '2023-09-02'),
('Eva Green', 'eva@example.com', '2023-09-03'),
('Frank Black', 'frank@example.com', '2023-09-03'),
('Grace Lee', 'grace@example.com', '2023-09-04'),
('Henry King', 'henry@example.com', '2023-09-04'),
('Isla Moore', 'isla@example.com', '2023-09-05'),
('Jack Wilson', 'jack@example.com', '2023-09-05');

INSERT INTO Professors (name, department) VALUES
('Dr. Brown', 'Computer Science'),
('Dr. Green', 'Mathematics'),
('Dr. Taylor', 'Physics'),
('Dr. Hall', 'Engineering'),
('Dr. Young', 'Biology'),
('Dr. Adams', 'Chemistry'),
('Dr. Nelson', 'History'),
('Dr. Baker', 'English'),
('Dr. Wright', 'Philosophy'),
('Dr. Scott', 'Psychology');


INSERT INTO Courses (name, description, credits, professor_id) VALUES
('Database Systems', 'Introduction to relational databases.', 3, 1),
('Linear Algebra', 'Matrices and vectors.', 4, 2),
('Physics I', 'Mechanics and thermodynamics.', 4, 3),
('Engineering Basics', 'Intro to engineering concepts.', 3, 4),
('Genetics', 'Principles of heredity.', 3, 5),
('Organic Chemistry', 'Carbon-based chemical reactions.', 4, 6),
('World History', 'Events that shaped the modern world.', 3, 7),
('English Literature', 'Analysis of literary texts.', 3, 8),
('Ethics', 'Philosophical principles of right and wrong.', 3, 9),
('Intro to Psychology', 'Fundamentals of human behavior.', 3, 10);

INSERT INTO Enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2023-09-05', 85.5),
(2, 1, '2023-09-05', 90.0),
(1, 2, '2023-09-06', 78.0),
(3, 2, '2023-09-06', 88.0),
(4, 3, '2023-09-07', 91.0),
(5, 4, '2023-09-07', 75.0),
(6, 5, '2023-09-08', 89.0),
(7, 6, '2023-09-08', 82.0),
(8, 7, '2023-09-09', 93.0),
(9, 8, '2023-09-09', 84.0);

INSERT INTO Assignments (course_id, title, due_date) VALUES
(1, 'SQL Basics', '2023-10-01'),
(1, 'Joins and Queries', '2023-10-08'),
(2, 'Matrix Operations', '2023-10-05'),
(2, 'Vector Spaces', '2023-10-12'),
(3, 'Newtonian Laws', '2023-10-07'),
(4, 'Bridge Design Project', '2023-10-10'),
(5, 'DNA Replication', '2023-10-09'),
(6, 'Hydrocarbons', '2023-10-11'),
(7, 'Ancient Civilizations', '2023-10-06'),
(8, 'Shakespeare Essay', '2023-10-13');
