gracz1 = input("Gracz 1: papier, nożyce, kamień? ")
gracz2 = input("Gracz 2: papier, nożyce, kamień? ")
if gracz1 == gracz2:
    print("Remis")
elif gracz1 == "papier" and gracz2 == "nożyce":
    print("Wygrał Gracz 2")
elif gracz1 == "papier" and gracz2 == "kamień":
    print("Wygrał Gracz 1")
elif gracz1 == "nożyce" and gracz2 == "papier":
    print("Wygrał Gracz 1")
elif gracz1 == "nożyce" and gracz2 == "kamień":
    print("Wygrał Gracz 2")
elif gracz1 == "kamień" and gracz2 == "papier":
    print("Wygrał Gracz 2")
elif gracz1 == "kamień" and gracz2 == "nożyce":
    print("Wygrał Gracz 1")
else:
    print("Błędne dane. Wprowadź ponownie. Pamiętaj o użyciu wyłącznie małych liter!")

