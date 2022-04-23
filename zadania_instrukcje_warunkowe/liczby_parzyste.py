liczby_uzytkownika = []
for i in range(1, 11):
    liczba = int(input(f"Wprowadź liczbę nr {i}: "))
    liczby_uzytkownika.append(liczba)
print(f"Podane liczby to {liczby_uzytkownika}")
liczbyParzyste = []
for element in liczby_uzytkownika:
    if element % 2 == 0:
        liczbyParzyste.append(element)
print(f"Liczby parzyste: {liczbyParzyste}")
