def greeting(name: str, surname: str) -> str:
    return "Cześć " + name + " " + surname + "!"

name = "Filip"
surname = "Morchat"
wynik = greeting(name, surname)
print(wynik)