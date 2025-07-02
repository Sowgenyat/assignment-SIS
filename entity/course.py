class Course:
    def __init__(self, course_id=None, course_name="", course_code="", instructor_name=""):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_code = course_code
        self.__instructor_name = instructor_name
        self.__enrollments = []  # Fixed: was previously declared as `enrollments` instead of `__enrollments`
        self.__teacher = None

    def assign_teacher(self, teacher):
        if not teacher:
            raise TeacherNotFoundException("Teacher object is required.")
        self.__teacher = teacher

    def update_course_info(self, course_code, course_name, instructor):
        if not course_code or not course_name:
            raise InvalidCourseDataException("Course name and code cannot be empty.")
        self.__course_code = course_code
        self.__course_name = course_name
        self.__instructor_name = instructor

    def display_course_info(self):
        print(f"Course ID: {self.__course_id}, "
              f"Name: {self.__course_name}, "
              f"Code: {self.__course_code}, "
              f"Instructor: {self.__instructor_name}")

    def get_enrollments(self):
        return self.__enrollments

    def get_teacher(self):
        return self.__teacher

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_course_code(self):
        return self.__course_code

    def get_instructor_name(self):
        return self.__instructor_name

    # Setters (optional if needed)
    def set_course_id(self, course_id):
        self.__course_id = course_id

    def add_enrollment(self, enrollment):
        self.__enrollments.append(enrollment)
