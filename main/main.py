from datetime import datetime
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from dao.SISrepositoryimpl  import SISRepositoryImpl
from tabulate import tabulate
import re

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return re.match(r"^\d{10}$", phone)

def display_menu():
    print("\n====== Student Information System Menu =====")
    print("1.   Add New Student")
    print("2.   Add New Course")
    print("3.   Add New Teacher")
    print("4.   Enroll Student in a Course")
    print("5.   Assign Teacher to a Course")
    print("6.   Record Payment for Student")
    print("7.   View Student Enrollments")
    print("8.   Generate Enrollment Report (by Course Name)")
    print("9.  Register: Enroll New Student")
    print("10.  Assign: Assign New Teacher")
    print("11.  Record Jane Johnson’s ₹500 Payment")
    print("12.  Report: Enrollment for 'Computer Science 101'")
    print("13.  Exit")

def main():
    repo = SISRepositoryImpl()

    while True:
        display_menu()
        choice = input("Enter your choice (1-15): ").strip()

        if choice == "1":
            student_id = input("Enter Student ID (optional): ") or None
            student_id = int(student_id) if student_id else None
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            date_of_birth = input("Enter DOB (YYYY-MM-DD): ")

            email = input("Enter Email: ")
            while not is_valid_email(email):
                print("Invalid email format.")
                email = input("Enter Email: ")
            phone = input("Enter 10-digit Phone Number: ")
            while not is_valid_phone(phone):
                print("Invalid phone number.")
                phone = input("Enter Phone Number: ")

            student = Student(student_id, first_name, last_name, date_of_birth, email, phone)
            repo.create_student(student)

        elif choice == "2":
            course_id = input("Enter Course ID (optional): ") or None
            course_id = int(course_id) if course_id else None
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            course = Course(course_id, course_name, course_code, instructor)
            repo.create_course(course)

        elif choice == "3":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            expertise = input("Enter Expertise: ")
            teacher = Teacher(first_name=first_name, last_name=last_name, email=email, expertise=expertise)
            repo.add_teacher(teacher)

        elif choice == "4":
            try:
                student_id = int(input("Enter Student ID: "))
                course_id = int(input("Enter Course ID: "))
                repo.enroll_student_in_course(student_id, course_id)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == "5":
            try:
                teacher_id = int(input("Enter Teacher ID: "))
                course_code = input("Enter Course Code: ")
                repo.assign_teacher_to_course_by_code(teacher_id, course_code)
            except ValueError:
                print(" Invalid input. Please enter valid values.")

        elif choice == "6":
            try:
                sid = int(input("Enter Student ID: "))
                amount = float(input("Enter Payment Amount: "))
                date = input("Enter Payment Date (YYYY-MM-DD): ")
                repo.add_payment(sid, amount, date)
            except Exception as e:
                print("Error recording payment:", e)


        elif choice == "7":
            course_name = input("Enter Course Name to generate enrollment report: ")
            report = repo.get_enrollment_report_by_course(course_name)
            if report:
                print(tabulate(report, headers=["Student ID", "First Name", "Last Name", "Enrollment Date"],
                               tablefmt="grid"))
            else:
                print(f" No enrollments found for course '{course_name}'.")

        elif choice == "8":
            course_name = input("Enter course name: ")
            report = repo.get_enrollments_by_course_name(course_name)
            if report:
                print(tabulate(report, headers=["Student ID", "Name", "Enrollment Date"], tablefmt="grid"))
            else:
                print(" No enrollments found")



        elif choice == "9":
            student_id = 200
            student = Student(student_id, "John", "Doe", "1995-08-15", "john.doe@example.com", "9876543210")
            repo.create_student(student)
            repo.enroll_student_in_course_by_name(sid, "Introduction to Programming", datetime.today().date())
            repo.enroll_student_in_course_by_name(sid, "Mathematics 101", datetime.today().date())

        elif choice == "10":
            teacher_id = 201
            repo.add_teacher(Teacher(teacher_id, "Sarah", "Smith", "sarah.smith@example.com", "CS"))
            repo.assign_teacher_to_course_by_code(teacher_id, "CS302")

        elif choice == "11":
            repo.add_payment(1, 500.0, "2023-04-10")

        elif choice == "12":
            course_name = "Computer Science 101"
            report = repo.get_enrollment_report_by_course(course_name)
            if report:
                print(tabulate(report, headers=["Student ID", "First Name", "Last Name", "Enrollment Date"], tablefmt="grid"))
            else:
                print(" No enrollments found")

        elif choice == "13":
            print("Thank you")
            break

        else:
            print("Invalid choice. Please select from 1 to 15.")

if __name__ == "__main__":
    main()
