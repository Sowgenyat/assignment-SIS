#TASK 3

-- TASK 3
-- task3 1. to calculate the total payments made by a specific student. You will need to join the "Payments" table with the "Students" table based on the student's ID.
select concat(s.first_name, ' ', s.last_name) as student_name,sum(p.amount) as total_payments
from students s
join
payments p on s.student_id = p.student_id
where s.student_id=2;

-- task3 2. Write an SQL query to retrieve a list of courses along with the count of students enrolled in each course. Use a JOIN operation between the "Courses" table and the "Enrollments" table.
select c.course_id,c.course_name,count(e.student_id) as noofstudents
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;

--task3 3.Write an SQL query to find the names of students who have not enrolled in any course. Use a
LEFT JOIN between the "Students" table and the "Enrollments" table to identify students
without enrollments.*/
select concat(s.first_name, ' ', s.last_name) as student_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.course_id is null;

-- task3 4. to retrieve the first name, last name of students, and the names of the courses they are enrolled
select s.first_name,s.last_name,c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id;

-- task3 5list the names of teachers and the courses they are assigned to.
select t.first_name,c.course_name
from teacher t
join courses c on t.teacher_id = c.teacher_id;


-- task3 6.Retrieve a list of students and their enrollment dates for a specific course.
select  s.first_name,s.last_name,e.enrollment_date,c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
where c.course_name = 'data structures';

-- task3 7. Find the names of students who have not made any payments
select s.first_name,s.last_name from students s
left join payments p on s.student_id = p.student_id
where p.payment_id is null;

-- task3 8. Identify courses that have no enrollments
select c.course_name
from courses c
left join enrollments e on c.course_id = e.course_id
where e.enrollment_id is  null;

-- task3 9.students who are enrolled in more than one course. Use a self-join*/

select e1.student_id,max(enrollment_id)
from enrollments e1
join enrollments e2 on e1.student_id = e2.student_id ;

-- task3 10.10. Find teachers who are not assigned to any courses. Use a LEFT JOIN

select concat(t.first_name,' ',last_name)
from teacher t
left join courses c on t.teacher_id = c.teacher_id
where c.course_id is null;