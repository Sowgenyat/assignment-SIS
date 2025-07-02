#TASK 4

-- TASK 4
-- 1.query to calculate the average number of students enrolled in each course. Use aggregate functions and subqueries to achieve this
select avg(student_count) as avgpercrs
from (
    select course_id, count(student_id) as student_count
    from enrollments
    group by course_id
) as enrollmentcounts;


-- 2.Identify the student(s) who made the highest payment.
select   concat(s.first_name,' ',last_name),p.amount
from students s
join payments p on s.student_id = p.student_id
where p.amount = (select max(amount)from payments);

-- 3 Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the course(s) with the maximum enrollment count.

select max(noofenrolls) as maxi from
(select course_id,count(enrollment_id) as noofenrolls
from enrollments
group by course_id) as noofenrollment;


-- 4. the total payments made to courses taught by each teacher. Use subqueries to sum payments for each teacher's courses.
select t.teacher_id,t.first_name,
(select sum(p.amount)
from payments p
join enrollments e on p.student_id = e.student_id
join courses c on e.course_id = c.course_id
where c.teacher_id = t.teacher_id) as total_payments
from teacher t;


-- 5 Identify students who are enrolled in all available courses. Use subqueries to compare a student's enrollments with the total number of courses.

select s.student_id, s.first_name
from students s
where (
    select count(e.course_id)
    from enrollments e
    where e.student_id = s.student_id
) = (
    select count( c.course_id)
    from courses c
);

-- 6.Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to find teachers with no course assignments.

select first_name from teacher
where  teacher_id not in (select course_id from courses where teacher_id is not null );

-- 7.Calculate the average age of all students. Use subqueries to calculate the age of each student based on their date of birth.

select avg(student_age) as average_age
from (select timestampdiff(year, date_of_birth, curdate()) as student_age from students
) as agesubquery;

-- 8.Identify courses with no enrollments. Use subqueries to find courses without enrollment records.
select course_id ,course_name from courses
where course_id not  in (select course_id from enrollments where enrollment_id is not null);

--  9.Calculate the total payments made by each student for each course they are enrolled in. Use subqueries and aggregate functions to sum payments.

select student_id,first_name ,
(select sum(amount) from payments
where payments.student_id=students.student_id
group by student_id)
from students ;

-- 10.Identify students who have made more than one payment. Use subqueries and aggregate functions to count payments per student and filter for those with counts greater than one.
select student_id from students
where student_id in(select student_id from payments
group by student_id
having count(amount)>1
);
-- 11. calculate the total payments made by each student. Join the "Students"table with the "Payments" table and use GROUP BY to calculate the sum of payments for each
;select concat(first_name,' ',last_name),sum(amount)
from students
join payments using(student_id)
group by student_id;

-- 12.Retrieve a list of course names along with the count of students enrolled in each course. UseJOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY tocount enrollments.
select course_id,count(enrollment_id)
from courses join enrollments using(course_id)
group by course_id;

-- 13.Calculate the average payment amount made by students. Use JOIN operations between the"Students" table and the "Payments" table and GROUP BY to calculate the average.
select avg(amount)
from students
join payments using(student_id);


