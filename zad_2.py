import zad_1

class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str
    def __init__(self, city: str, street: str, zip: str, hrs: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip
        self.open_hours = hrs
        self.phone = phone
    def __str__(self):
        return f'Biblioteka w miescie {self.city}, na ulicy {self.street}, kod pocztowy {self.zip_code}. Otwarta w godzinach {self.open_hours}, nr telefonu {self.phone}.'

class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str
    def __init__(self, name: str, sname: str, hdate: str, bdate: str, city: str, street: str, zip: str, phone: str):
        self.first_name = name
        self.last_name = sname
        self.hire_date = hdate
        self.birth_date = bdate
        self.city = city
        self.street = street
        self.zip_code = zip
        self.phone = phone
    def __str__(self):
        return f'{self.first_name}  {self.last_name}, urodzony dnia {self.birth_date}. Zatrudniony od dnia {self.hire_date}. Zamieszkaly na ulicy {self.street} w miescie {self.city} (kod pocztowy {self.zip_code}), nr telefonu: {self.phone}.'

class Book:
    name: str ##ksiazka musi miec nazwe!
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int
    def __init__(self, name:str, library: Library, date: str, aname: str, surname: str, pages: int):
        self.name = name
        self.library = library
        self.publication_date = date
        self.author_name = aname
        self.author_surname = surname
        self.number_of_pages = pages
    def __str__(self):
        ret = f'Ksiazka {self.name} autorstwa {self.author_name} {self.author_surname}, wydana w dniu {self.publication_date}. Posiada az {self.number_of_pages} stron. O bibliotece: ' + self.library.__str__()
        return ret
class Order:
    employee: Employee
    student: zad_1.Student
    books: list
    order_date: str
    def __init__(self, employee: Employee, student: zad_1.Student, books: list, order: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order
    def __str__(self):
        ret = f'Zamowienie zlozone przez {self.student.name}, przyjete przez {self.employee.first_name} {self.employee.last_name}, zlozone dnia {self.order_date}. O ksiazkach: '
        for book in self.books:
            ret = ret + book.__str__()
        return ret

lib1 = Library("Katowice","Mariacka 8", "66-666","9:00-17:00","322-233-000")
lib2 = Library("Warszawa","Długa 20","00-001","12:00-18:30","nie podano")

book1 = Book("Zabic drozda",lib1,"27-01-1960","Abraham","Lincoln",450)
book2 = Book("Pan Tadeusz",lib2,"28-06-1834","Adam","Mickiewicz",600)
book3 = Book("Zew Cthulhu",lib2,"18.01.1912","Howard P.","Lovecraft",380)
book4 = Book("Styria",lib2,"27.02.2024","Mariusz","Maszczyk",284)
book5 = Book("Piąta księga",lib1,"25-10-2026","Barack","Obama",67)

emp1 = Employee("Jan","Tadeusz","27-01-2021","17-12-1984","Katowice","Smutna 1","87-564",'22222222222')
emp2 = Employee("Karina","Kowalczyk","19-10-2009","08-05-1990","Sosnowiec","Rudna 14","40-012","brak")
emp3 = Employee("Justyna","Polańska","20-02-2022","15-09-2000","Siedlce","Ostatnia 9/5b","80-085","322683838")

stud1 = zad_1.Student("Alojzy", [90,65])
stud2 = zad_1.Student("Błażej", [9000000])
stud3 = zad_1.Student("Maria", [865,20,35,47])

order1 = Order(emp3, stud2, [book2, book3, book4], "26-10-2026")
order2 = Order(emp1, stud1, [book1, book5], "27-10-2026")

print(str(order1))
print(str(order2))