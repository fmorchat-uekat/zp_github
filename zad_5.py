def is_present(l: list, a: int) -> bool:
    for item in list:
        if item == a:
            return 1
    return 0

list = ["Adam", 8, "chleb", 999]
liczba = 8

wynik = is_present(list, liczba)
if(wynik):
    print("Liczba pojawia sie w liscie")
else:
    print("Liczba nie pojawia sie w liscie")
