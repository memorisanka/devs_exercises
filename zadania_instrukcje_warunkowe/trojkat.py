def trojkat():

    """Po podaniu długości boków funkcja zwraca informację, czy trójkąt jest prostokątny."""

    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długośc boku b: "))
    c = int(input("Podaj długośc boku c: "))
    if a + b == c ** 2 or a + c == b ** 2 or b + c == a ** 2:
        return "Trójkąt jest prostokątny."
    else:
        return "Trójkąt nie jest prostokątny."


print(trojkat())
