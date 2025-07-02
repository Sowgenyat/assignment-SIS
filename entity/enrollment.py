class Enrollment:
    def __init__(self, enrollment_id=None, student=None, course=None, enrollment_date=""):
        if not student or not course:
            raise InvalidEnrollmentDataException()
        self.__enrollment_id = enrollment_id
        self.__student = student
        self.__course = course
        self.__enrollment_date = enrollment_date
        student.enrollments.append(self)
        course.enrollments.append(self)
    def get_student(self):
        return self.__student

    def get_course(self):
        return self.__course
