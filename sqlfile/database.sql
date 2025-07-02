create database sisdb;
use sisdb;

create table students (
student_id int primary key auto_increment,
first_name varchar(50),
last_name varchar(50),
date_of_birth date,
email varchar(100),
phone_number varchar(15)
);

alter table students add column balance decimal(10, 2) default 0;


select*from students;
drop table students;


select* from teacher;
drop table teacher;

create table teacher (
teacher_id int primary key auto_increment,
first_name varchar(50),
last_name varchar(50),
email varchar(100),
 expertise varchar(100)
);

select * from teacher;
drop table courses;

create table courses (
course_id int primary key auto_increment,
course_name varchar(100),
credits int,
teacher_id int references teacher(teacher_id),
course_code varchar(30),
instructor_name varchar(80)
);

select * from courses;
create table enrollments (
enrollment_id int primary key auto_increment,
enrollment_date date,
student_id int references students(student_id),
course_id int references courses(course_id)
);

select * from enrollments;
drop table payments;

create table payments (
payment_id int primary key auto_increment,
amount decimal(10,2),
payment_date date,
student_id int references students(student_id));

insert into students (first_name, last_name, date_of_birth, email, phone_number) values
('alice', 'johnson', '2001-07-15', 'alice.j@email.com', '3456789012'),
('bob', 'lee', '1998-12-03', 'bob.lee@email.com', '4567890123'),
('carol', 'williams', '2000-01-20', 'carol.w@email.com', '5678901234'),
('grace', 'wilson', '2001-02-05', 'grace.w@email.com', '9012345678'),
('harry', 'clark', '2000-08-27', 'harry.c@email.com', '0123456789');
insert into teacher (first_name, last_name, email,expertise) values
('alan', 'turing', 'alan.turing@email.com','data structures'),
('donald', 'knuth', 'donald.knuth@email.com','algorithms'),
('james', 'gosling', 'james.g@email.com','computer networks'),
('guido', 'van rossum', 'guido.vr@email.com','operating systems'),
('dennis', 'ritchie', 'dennis.r@email.com','operating system');
insert into courses (course_name, credits, teacher_id,course_code,instructor_name) values
('data structures', 4, 1,'mn3','alan'),
('algorithms', 4, 2,'lk8','guido'),
('computer networks', 3, 3,'oi8','james'),
('databases', 3, 4,'sw2','guido'),
('operating systems', 4, 5,'lk89','dennis');
insert into enrollments (student_id, course_id, enrollment_date) values
(1, 1, '2024-01-10'),
(2, 2, '2024-01-12'),
(3, 3, '2024-01-15'),
(4, 4, '2024-01-20'),
(5, 5, '2024-02-01');
insert into payments (student_id, amount, payment_date) values
(1, 1000.00, '2024-01-15'),
(2, 950.00, '2024-01-17'),
(3, 1200.00, '2024-01-20'),
(4, 1100.00, '2024-01-25'),
(5, 900.00, '2024-02-01');



