def czy_parzysta():
    """Program sprawdza, czy co najmniej jedna z podanych liczb jest liczbą parzystą."""
    liczba1 = int(input("Wprowadź pierwszą liczbę: "))
    liczba2 = int(input("Wprowadź drugą liczbę: "))
    if liczba1 % 2 == 0 or liczba2 % 2 == 0:
        return "Przynajmniej jedna z podanych liczb jest liczbą parzystą."
    else:
        return "Żadna z podanych liczb nie jest liczbą parzystą."

print(czy_parzysta())