from util.dbconnect import get_connection
from entity.course import Course
from tabulate import tabulate
import datetime
from decimal import Decimal

class SISRepositoryImpl:

    def create_student(self, student):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if student.get_student_id() is not None:
                query = """
                INSERT INTO students (student_id, first_name, last_name, date_of_birth, email, phone_number)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (
                    student.get_student_id(),
                    student.get_first_name(),
                    student.get_last_name(),
                    student.get_date_of_birth(),
                    student.get_email(),
                    student.get_phone_number()
                )
            else:
                query = """
                INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (
                    student.get_first_name(),
                    student.get_last_name(),
                    student.get_date_of_birth(),
                    student.get_email(),
                    student.get_phone_number()
                )
            cursor.execute(query, values)
            conn.commit()
            print("Student added successfully.")
        except Exception as e:
            print(" Error inserting student:", e)
        finally:
            cursor.close()
            conn.close()

    def create_course(self, course):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO courses (course_name, course_code, instructor_name)
                VALUES (%s, %s, %s)
            """
            values = (
                course.get_course_name(),
                course.get_course_code(),
                course.get_instructor_name()
            )
            cursor.execute(query, values)
            conn.commit()
            print("Course added successfully.")
        except Exception as e:
            print(" Error inserting course:", e)
        finally:
            cursor.close()
            conn.close()

    def add_teacher(self, teacher):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO teacher (first_name, last_name, email, expertise)
                VALUES (%s, %s, %s, %s)
            """
            values = (
                teacher.get_first_name(),
                teacher.get_last_name(),
                teacher.get_email(),
                teacher.get_expertise()
            )
            cursor.execute(query, values)
            conn.commit()
            print("Teacher added successfully!")
        except Exception as e:
            print(f"Error adding teacher: {e}")
        finally:
            cursor.close()
            conn.close()

    def enroll_student_in_course(self, student_id, course_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO enrollments (student_id, course_id, enrollment_date)
                VALUES (%s, %s, %s)
            """
            values = (student_id, course_id, datetime.date.today())
            cursor.execute(query, values)
            conn.commit()
            print("Student enrolled in course successfully!")
        except Exception as e:
            print(f"Error enrolling student: {e}")
        finally:
            cursor.close()
            conn.close()

    def assign_teacher_to_course_by_code(self, teacher_id, course_code):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT course_id FROM courses WHERE course_code = %s", (course_code,))
            result = cursor.fetchone()
            if not result:
                print(f" Course with code {course_code} not found.")
                return
            course_id = result[0]
            cursor.execute("UPDATE courses SET teacher_id = %s WHERE course_id = %s", (teacher_id, course_id))
            conn.commit()
            print(f"Teacher assigned to course {course_code}")
        except Exception as e:
            conn.rollback()
            print("Error assigning teacher:", e)
        finally:
            cursor.close()
            conn.close()

    def add_payment(self, student_id, amount, payment_date):
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                # Step 1: Check if student exists
                cur.execute("SELECT first_name FROM students WHERE student_id = %s", (student_id,))
                result = cur.fetchone()
                if not result:
                    print("Student not found.")
                    return
                name = result[0]

                # Step 2: Insert payment
                cur.execute("""
                    INSERT INTO payments (student_id, amount, payment_date)
                    VALUES (%s, %s, %s)
                """, (student_id, Decimal(str(amount)), payment_date))

            conn.commit()
            print(f" ₹{amount} payment recorded for {name}.")
        except Exception as e:
            conn.rollback()
            print(" Error recording payment:", e)
        finally:
            conn.close()

    def get_enrollments_by_course_name(self, course_name):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                SELECT s.student_id, CONCAT(s.first_name, ' ', s.last_name), e.enrollment_date
                FROM students s
                JOIN enrollments e ON s.student_id = e.student_id
                JOIN courses c ON e.course_id = c.course_id
                WHERE c.course_name = %s
            """
            cursor.execute(query, (course_name,))
            return cursor.fetchall()
        except Exception as e:
            print("Error fetching enrollment report:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def get_enrollment_report_by_course(self, course_name):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                SELECT s.student_id, s.first_name, s.last_name, e.enrollment_date
                FROM students s
                JOIN enrollments e ON s.student_id = e.student_id
                JOIN courses c ON e.course_id = c.course_id
                WHERE c.course_name = %s
            """
            cursor.execute(query, (course_name,))
            return cursor.fetchall()
        except Exception as e:
            print("Error fetching enrollment report:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def enroll_student_in_course_by_name(self, student_id, course_name, enrollment_date):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT course_id FROM courses WHERE course_name = %s", (course_name,))
            result = cursor.fetchone()
            if not result:
                print(f"Course '{course_name}' not found.")
                return
            course_id = result[0]
            cursor.execute("""
                INSERT INTO enrollments (student_id, course_id, enrollment_date)
                VALUES (%s, %s, %s)
            """, (student_id, course_id, enrollment_date))
            conn.commit()
            print(f"Enrolled in course: {course_name}")
        except Exception as e:
            conn.rollback()
            print(" Error enrolling student:", e)
        finally:
            cursor.close()
            conn.close()

    def get_course_by_code(self, course_code):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses WHERE course_code = %s", (course_code,))
            row = cursor.fetchone()
            if row:
                return Course(course_id=row[0], course_name=row[1], course_code=row[2], instructor_name=row[3])
            return None
        except Exception as e:
            print("Error retrieving course by code:", e)
            return None
        finally:
            cursor.close()
            conn.close()





