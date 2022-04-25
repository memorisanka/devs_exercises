colours = ["zielony", "czerwony", "niebieski", "czarny", "fioletowy", "granatowy", "niebieski", "czarny",
"czarny", "zielony", "cytrynowy", "granatowy", "niebieski", "indygo", "zielony", "czerwony"]

set_colours = set(colours)

# zwraca liczbę elementów listy i zbioru
print(f"Liczba elementów w liście colours: {len(colours)}")
print(f"Liczba elementów w zbiorze set_colours: {len(set_colours)}")

# wyświetla listę elementów zbioru jeden pod drugim
for i in set_colours:
    print(i)

# dodanie do zbioru koloru "biały"
set_colours.update({"biały"})
print(set_colours)

# usunięcie ze zbioru koloru "granatowy"
set_colours.discard("granatowy")
print(set_colours)