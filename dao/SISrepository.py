from abc import ABC, abstractmethod

class SISRepository(ABC):
    @abstractmethod
    def create_student(self, student):
        pass
    @abstractmethod
    def create_course(self, course):
        pass
    @abstractmethod
    def enroll_student(self, enrollment):
        pass
    @abstractmethod
    def assign_teacher(self, teacher, course_id):
        pass
    @abstractmethod
    def record_payment(self, payment):
        pass
