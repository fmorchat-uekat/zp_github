import student as stud
import library as lib
import employee as emp
import order as ord
import book as b


lib1 = lib.Library("Katowice",
               "Mariacka 8",
               "66-666",
               "9:00-17:00",
               "322-233-000")
lib2 = lib.Library("Warszawa",
               "Długa 20",
               "00-001",
               "12:00-18:30",
               "nie podano")

book1 = b.Book("Zabic drozda",
             lib1,
             "27-01-1960",
             "Abraham",
             "Lincoln",
             450)
book2 = b.Book("Pan Tadeusz",
             lib2,
             "28-06-1834",
             "Adam",
             "Mickiewicz",
             600)
book3 = b.Book("Zew Cthulhu",
             lib2,
             "18.01.1912",
             "Howard P.",
             "Lovecraft",
             380)
book4 = b.Book("Styria",
             lib2,
             "27.02.2024",
             "Mariusz",
             "Maszczyk",
             284)
book5 = b.Book("Piąta księga",
             lib1,
             "25-10-2026",
             "Barack",
             "Obama",
             67)

emp1 = emp.Employee("Jan",
                "Tadeusz",
                "27-01-2021",
                "17-12-1984",
                "Katowice",
                "Smutna 1",
                "87-564",
                '22222222222')
emp2 = emp.Employee("Karina",
                "Kowalczyk",
                "19-10-2009",
                "08-05-1990",
                "Sosnowiec",
                "Rudna 14",
                "40-012",
                "brak")
emp3 = emp.Employee("Justyna",
                "Polańska",
                "20-02-2022",
                "15-09-2000",
                "Siedlce",
                "Ostatnia 9/5b",
                "80-085",
                "322683838")

stud1 = stud.Student("Alojzy",
                      [90, 65])
stud2 = stud.Student("Błażej",
                      [9000000])
stud3 = stud.Student("Maria",
                      [865, 20, 35, 47])

order1 = ord.Order(emp3,
               stud2,
               [book2, book3, book4],
               "26-10-2026")
order2 = ord.Order(emp1,
               stud1,
               [book1, book5],
               "27-10-2026")

print(str(order1))
print(str(order2))
