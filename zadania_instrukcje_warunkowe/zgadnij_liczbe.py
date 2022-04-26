import random
# podanie przedziału przez użytkownika
dolnyPrzedzial = int(input("Podaj dolny przedział: "))
gornyPrzedzial = int(input("Podaj górny przedział: "))
# losowanie liczby z podanego przedziału
losowaLiczba = random.randint(dolnyPrzedzial, gornyPrzedzial)
# przypisanie jako startowej liczby punktów wylosowanej liczby1
liczbaPunktow = losowaLiczba
# pierwsza próba zgadnięcia liczby
podajLiczbe = int(input("Podaj liczbę: "))


for i in range(dolnyPrzedzial, gornyPrzedzial + 1):
    if podajLiczbe < losowaLiczba:
        print("Podana liczba jest mniejsza od wylosowanej. Próbuj dalej!")
        liczbaPunktow -= 1
        podajLiczbe = int(input("Podaj liczbę ponownie: "))
    elif podajLiczbe > losowaLiczba:
        print("Podana liczba jest większa od wylosowanej. Próbuj dalej!")
        liczbaPunktow -= 1
        podajLiczbe = int(input("Podaj liczbę ponownie: "))
    else:
        print("BRAWO. To właściwa liczba!")
        break

print(f"Zdobyłeś {liczbaPunktow} punktów.")