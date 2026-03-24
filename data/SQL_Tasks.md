# SQL Practice Tasks – School Database

These tasks use the `school_full.db` database. Try writing SQL queries to complete each task.  

---

## **Task 1: List all students**

Write a query to display all columns from the `Students` table.

**Hints:**  
- Use the `SELECT *` command  
- Table name: `Students`

---

## **Task 2: Find all Computer Science courses**

Write a query to show the course name and the teacher's full name (first and last) for all courses that are **Computer Science**.

**Hints:**  
- Use `JOIN` between `Courses` and `Teachers`  
- Filter with `WHERE course_name = 'Computer Science'`

---

## **Task 3: Show students with grades above 80**

Write a query to list the first name, last name, course name, and grade for students who scored more than 80 in any class.

**Hints:**  
- Join `Students`, `Enrolments`, `Classes`, and `Courses`  
- Filter with `WHERE grade > 80`

---

## **Task 4: Average grade per student**

Write a query to calculate the **average grade** for each student across all their classes. Show the student's full name and average grade.

**Hints:**  
- Use `AVG(grade)`  
- Group by student

---

## **Task 5: Count students per teacher**

Write a query to find how many students each teacher teaches. Show the teacher’s full name and the total number of students.

**Hints:**  
- Join `Teachers`, `Courses`, `Classes`, and `Enrolments`  
- Use `COUNT(enrolment_id)`  
- Group by teacher

---
