def is_even(a: int) -> bool:
    if a%2==0:
        return 1
    else:
        return 0

a = 7
iseven = is_even(a)
if(iseven):
    print("liczba parzysta")
else:
    print("Liczba nieparzysta")
