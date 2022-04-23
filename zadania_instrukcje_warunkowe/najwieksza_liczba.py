def maximum1():
    """Funkcja pobiera od użytkownika trzy liczby
    i zwraca największą liczbę z podanych - sposób bez warunku"""
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    liczba3 = int(input("Podaj trzecią liczbę: "))
    return f"Największą z podanych liczb jest: {max(liczba1, liczba2, liczba3)}."


def maximum2():
    """Funkcja pobiera od użytkownika trzy liczby
    i zwraca największą liczbę z podanych - sposób z warunkiem"""
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    liczba3 = int(input("Podaj trzecią liczbę: "))
    if liczba1 > liczba2 and liczba1 > liczba3:
        return f"Największą liczbą jest {liczba1}"
    elif liczba2 > liczba1 and liczba2 > liczba3:
        return f"Największą liczbą jest {liczba2}"
    else:
        return f"Największą liczbą jest {liczba3}"


print(maximum1())
print(maximum2())


