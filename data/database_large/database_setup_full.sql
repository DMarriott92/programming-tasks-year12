-- ======= Students Table =======
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_group INTEGER
);

-- ======= Teachers Table =======
CREATE TABLE Teachers (
    teacher_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    subject TEXT
);

-- ======= Courses Table =======
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- ======= Classes Table =======
CREATE TABLE Classes (
    class_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    room TEXT,
    schedule TEXT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- ======= Enrolments Table =======
CREATE TABLE Enrolments (
    enrolment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    class_id INTEGER,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES Students(student_id),
    FOREIGN KEY(class_id) REFERENCES Classes(class_id)
);

-- ===================== INSERT DATA =====================

-- Students
INSERT INTO Students VALUES (1,'Alice','Carter',12);
INSERT INTO Students VALUES (2,'Ben','Davies',12);
INSERT INTO Students VALUES (3,'Charlie','Singh',12);
INSERT INTO Students VALUES (4,'Daisy','Patel',12);
INSERT INTO Students VALUES (5,'Ethan','Hughes',12);
INSERT INTO Students VALUES (6,'Fatima','Khan',12);
INSERT INTO Students VALUES (7,'George','Brown',12);
INSERT INTO Students VALUES (8,'Hannah','Wilson',12);
INSERT INTO Students VALUES (9,'Isaac','Taylor',12);
INSERT INTO Students VALUES (10,'Jessica','Moore',12);

-- Teachers
INSERT INTO Teachers VALUES (1,'Mr','Robinson','Computer Science');
INSERT INTO Teachers VALUES (2,'Ms','Smith','Mathematics');
INSERT INTO Teachers VALUES (3,'Mrs','Lewis','Physics');

-- Courses
INSERT INTO Courses VALUES (1,'Computer Science',1);
INSERT INTO Courses VALUES (2,'Mathematics',2);
INSERT INTO Courses VALUES (3,'Physics',3);

-- Classes
INSERT INTO Classes VALUES (1,1,'Room 101','Mon 9am');
INSERT INTO Classes VALUES (2,1,'Room 101','Wed 11am');
INSERT INTO Classes VALUES (3,2,'Room 202','Tue 10am');
INSERT INTO Classes VALUES (4,3,'Lab 1','Thu 1pm');

-- Enrolments
INSERT INTO Enrolments VALUES (1,1,1,78);
INSERT INTO Enrolments VALUES (2,1,2,82);
INSERT INTO Enrolments VALUES (3,2,1,65);
INSERT INTO Enrolments VALUES (4,2,3,70);
INSERT INTO Enrolments VALUES (5,3,1,91);
INSERT INTO Enrolments VALUES (6,3,4,88);
INSERT INTO Enrolments VALUES (7,4,2,79);
INSERT INTO Enrolments VALUES (8,5,3,74);
INSERT INTO Enrolments VALUES (9,6,1,95);
INSERT INTO Enrolments VALUES (10,7,1,68);
INSERT INTO Enrolments VALUES (11,8,2,90);
INSERT INTO Enrolments VALUES (12,9,3,69);
INSERT INTO Enrolments VALUES (13,10,1,81);
