-- Create Students table
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_group INTEGER
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
);

-- Create Enrolments table (links students and courses)
CREATE TABLE Enrolments (
    enrolment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(course_id) REFERENCES Courses(course_id)
);

-- Insert Students
INSERT INTO Students VALUES (1,'Alice','Carter',12);
INSERT INTO Students VALUES (2,'Ben','Davies',12);
INSERT INTO Students VALUES (3,'Charlie','Singh',12);
INSERT INTO Students VALUES (4,'Daisy','Patel',12);
INSERT INTO Students VALUES (5,'Ethan','Hughes',12);
INSERT INTO Students VALUES (6,'Fatima','Khan',12);

-- Insert Courses
INSERT INTO Courses VALUES (1,'Computer Science');
INSERT INTO Courses VALUES (2,'Mathematics');
INSERT INTO Courses VALUES (3,'Physics');

-- Insert Enrolments
INSERT INTO Enrolments VALUES (1,1,1,78);
INSERT INTO Enrolments VALUES (2,1,2,82);
INSERT INTO Enrolments VALUES (3,2,1,65);
INSERT INTO Enrolments VALUES (4,2,3,70);
INSERT INTO Enrolments VALUES (5,3,1,91);
INSERT INTO Enrolments VALUES (6,4,2,79);
INSERT INTO Enrolments VALUES (7,5,3,74);
INSERT INTO Enrolments VALUES (8,6,1,95);
