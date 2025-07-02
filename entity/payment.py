class Payment:
    def __init__(self, payment_id=None, student=None, amount=0.0, payment_date=""):
        if not student:
            raise StudentNotFoundException()
        self.__payment_id = payment_id
        self.__student = student
        self.__amount = amount
        self.__payment_date = payment_date

    def get_student(self):
        return self.__student

    def get_payment_amount(self):
        return self.__amount

    def get_payment_date(self):
        return self.__payment_date
