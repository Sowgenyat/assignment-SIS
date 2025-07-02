class Teacher:
    def __init__(self, teacher_id=None, first_name="", last_name="", email="", expertise=""):
        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__expertise = expertise
        self.__assigned_courses = []


    def get_teacher_id(self):
        return self.__teacher_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_expertise(self):
        return self.__expertise

    def get_assigned_courses(self):
        return self.__assigned_courses


    def set_assigned_courses(self, course_list):
        self.__assigned_courses = course_list

    def update_teacher_info(self, first_name, last_name, email, expertise=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        if expertise:
            self.__expertise = expertise


    def display_teacher_info(self):
        print(
            f"Teacher ID: {self.__teacher_id}, "
            f"Name: {self.__first_name} {self.__last_name}, "
            f"Email: {self.__email}, "
            f"Expertise: {self.__expertise}"
        )
