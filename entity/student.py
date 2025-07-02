

class Student:
    def __init__(self, student_id=None, first_name="", last_name="", date_of_birth="", email="", phone_number=""):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__phone_number = phone_number
        self.__courses = []
        self.__payments = []
        self.__enrollments = []

    def enroll_in_course(self, course):
        if course in self.__courses:
            raise DuplicateEnrollmentException("Student already enrolled in this course.")
        self.__courses.append(course)

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        if not first_name or not email:
            raise InvalidStudentDataException("First name and email are required.")
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__phone_number = phone_number

    def make_payment(self, amount, payment_date):
        if amount <= 0:
            raise PaymentValidationException("Payment amount must be positive.")
        self.__payments.append((amount, payment_date))

    def display_student_info(self):
        print(f"ID: {self.__student_id}, "
              f"Name: {self.__first_name} {self.__last_name}, "
              f"DOB: {self.__date_of_birth}, "
              f"Email: {self.__email}, "
              f"Phone: {self.__phone_number}")


    def get_student_id(self):
        return self.__student_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_enrolled_courses(self):
        return self.__courses

    def get_payment_history(self):
        return self.__payments

    def get_enrollments(self):
        return self.__enrollments


    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_enrollments(self, enrollments):
        self.__enrollments = enrollments