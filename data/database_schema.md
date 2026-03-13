Students
---------
student_id (PK)
first_name
last_name
year_group


Courses
---------
course_id (PK)
course_name


Enrolments
---------
enrolment_id (PK)
student_id (FK)
course_id (FK)
grade
