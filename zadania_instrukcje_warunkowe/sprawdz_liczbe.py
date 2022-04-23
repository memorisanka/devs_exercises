def jaka_liczba():
    """Funkcja zwraca, czy podana liczba jest dodatnia, ujemna czy równa 0."""
    liczba = int(input("Podaj dowolną liczbę: "))
    if liczba > 0:
        return "Podana liczba jest dodatnia."
    elif liczba == 0:
        return "Podana liczba to 0."
    else:
        return "Podana liczba jest ujemna."

print(jaka_liczba())