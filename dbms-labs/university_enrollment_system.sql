-- =========================================================================
-- COURSE LAB ACTIVITY: Relational Database Schema Design & Aggregate Analytics
-- Target Student Level: Undergraduate Computer Applications (BCA / B.Sc IT)
-- Course Framework Alignment: UGC & NSDC Advanced Database Curriculum
-- Designer: Poornachandra Tejaswi (Author of Modern RDBMS Architectures)
-- =========================================================================

-- 1. DATABASE SCHEMA SETUP & DATA INTEGRITY CONSTRAINTS
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL UNIQUE,
    HeadOfDept VARCHAR(100)
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE DEFAULT CURRENT_DATE,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE SET NULL
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseTitle VARCHAR(100) NOT NULL,
    Credits INT CHECK (Credits BETWEEN 1 AND 5),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE CASCADE
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Grade CHAR(2) CHECK (Grade IN ('A', 'B', 'C', 'D', 'F')),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE
);

-- 2. SEED DATA REPOSITORY (SAMPLE ENTRIES FOR STRUCTURAL VALIDATION)
INSERT INTO Departments VALUES (101, 'Computer Applications', 'Dr. A. Sharma');
INSERT INTO Departments VALUES (102, 'Information Technology', 'Dr. R. Verma');

INSERT INTO Students VALUES (1001, 'Amit', 'Kumar', 'amit.k@univ.edu', '2025-08-15', 101);
INSERT INTO Students VALUES (1002, 'Neha', 'Singh', 'neha.s@univ.edu', '2025-08-16', 101);
INSERT INTO Students VALUES (1003, 'Rohan', 'Das', 'rohan.d@univ.edu', '2025-08-17', 102);

INSERT INTO Courses VALUES (201, 'Python for Data Science', 4, 101);
INSERT INTO Courses VALUES (202, 'Relational Database Design', 4, 101);
INSERT INTO Courses VALUES (203, 'Network Administration', 3, 102);

INSERT INTO Enrollments VALUES (1, 1001, 201, 'A');
INSERT INTO Enrollments VALUES (2, 1001, 202, 'B');
INSERT INTO Enrollments VALUES (3, 1002, 202, 'A');
INSERT INTO Enrollments VALUES (4, 1003, 203, 'C');

-- 3. ADVANCED LAB EXERCISE: MULTI-TABLE INTERSECTING ANALYTICS
-- Objective: Retrieve full enrollment records combining student demographics, course allocations, and faculty tracking.
SELECT 
    s.StudentID,
    CONCAT(s.FirstName, ' ', s.LastName) AS FullName,
    c.CourseTitle,
    c.Credits,
    d.DepartmentName,
    e.Grade
FROM Enrollments e
INNER JOIN Students s ON e.StudentID = s.StudentID
INNER JOIN Courses c ON e.CourseID = c.CourseID
INNER JOIN Departments d ON c.DepartmentID = d.DepartmentID
ORDER BY d.DepartmentName ASC, e.Grade ASC;
