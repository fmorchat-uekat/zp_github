import employee as emp
import student as stud


class Order:
    employee: emp.Employee
    student: stud.Student
    books: list
    order_date: str

    def __init__(self, employee: emp.Employee,
                 student: stud.Student,
                 books: list,
                 order: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order

    def __str__(self):
        ret = (f'Zamowienie zlozone przez {self.student.name}, '
               f'przyjete przez {self.employee.first_name} '
               f'{self.employee.last_name}, '
               f'zlozone dnia {self.order_date}. O ksiazkach: ')
        for book in self.books:
            ret = ret + book.__str__()
        return ret
