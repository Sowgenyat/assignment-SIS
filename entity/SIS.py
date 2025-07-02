from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from entity.enrollment  import Enrollment
from entity.payment import Payment


class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []
    def enroll_student_in_course(self, student, course):
        if not student:
            raise StudentNotFoundException()
        if not course:
            raise CourseNotFoundException()
        student.enroll_in_course(course)
        print(f"Enrolled {student._Student__first_name} in {course._Course__course_name}")

    def assign_teacher_to_course(self, teacher, course):
        if not teacher:
            raise TeacherNotFoundException()
        if not course:
            raise CourseNotFoundException()
        course.assign_teacher(teacher)
        print(f"Assigned {teacher._Teacher__first_name} to {course._Course__course_name}")

    def record_payment(self, student, amount, payment_date):
        if not student:
            raise StudentNotFoundException()
        if amount <= 0:
            raise PaymentValidationException()
        student.make_payment(amount, payment_date)
        print(f"Recorded payment of ₹{amount} on {payment_date} for {student._Student__first_name}")

    def generate_enrollment_report(self, course):
        print(f"Enrollment Report for {course._Course__course_name}:")
        for student in course.get_enrollments():
            print(f" - {student._Student__first_name} {student._Student__last_name}")

    def generate_payment_report(self, student):
        print(f"Payment Report for {student._Student__first_name}:")
        for amount, date in student.get_payment_history():
            print(f" - ₹{amount} on {date}")

    def calculate_course_statistics(self, course):
        enrollments = course.get_enrollments()
        num_students = len(enrollments)
        print(f"Course Statistics for {course._Course__course_name}:")
        print(f" - Total Enrollments: {num_students}")

    def add_enrollment(self, student, course, enrollment_date):
        enrollment = Enrollment(student, course, enrollment_date)
        student.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
        self.enrollments.append(enrollment)

    def assign_course_to_teacher(self, course, teacher):
        teacher.assigned_courses.append(course)

    def add_payment(self, student, amount, payment_date):
        payment = Payment(student, amount, payment_date)
        student.payments.append(payment)
        self.payments.append(payment)

    def get_enrollments_for_student(self, student):
        return student.enrollments

    def get_courses_for_teacher(self, teacher):
        return teacher.assigned_courses