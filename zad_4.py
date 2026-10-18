def compare_sum(a: int, b: int, c: int) -> bool:
    if a+b >= c:
        return 1
    else:
        return 0

a = 5
b = 4
c = 1

wynik = compare_sum(a,b,c)
if(wynik):
    print("Suma jest wieksza lub rowna")
else:
    print("Suma jest mniejsza")