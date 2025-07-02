#TASK 2

-- Tasks 2: Select, Where, Between, AND, LIKE:

-- task2 1.to insert a new student into the "Students" table
insert into students (first_name, last_name, date_of_birth, email, phone_number)
values ('john', 'doe', '1995-08-15', 'john.doe@example.com', '1234567890');

-- task2 2.to enroll a student in a course. Choose an existing student and course and insert a record into the "Enrollments" t
insert into enrollments(student_id, course_id, enrollment_date)
values (1, 2, '2025-06-15');

-- task2 3.Update the email address of a specific teacher in the "Teacher" table.
 update teacher set email='d@gmail.com'
 where teacher_id=2;
select * from teacher;

-- task2 4.to delete a specific enrollment record from the "Enrollments" table.
 delete from enrollments
 where student_id=1 AND course_id=2;
 select*from enrollments;

 -- task2 5.Update the "Courses" table to assign a specific teacher to a course.
 update courses set teacher_id=2
 where course_id=1;
  select*from courses;

  -- task2 6.Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table.

delete from enrollments where student_id = 1;
delete from students where student_id = 1;

-- task2 7.Update the payment amount for a specific payment record in the "Payments" table. Choose any payment record and modify the payment amount.
update payments
set amount = 1800.00
where student_id = 5 and payment_date = '2024-02-01';
