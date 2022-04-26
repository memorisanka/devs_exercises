my_favourite_colours = {"czarny", "beżowy", "szary", "zielony"}
user_favourite_colours = set(((input("Podaj swoje ulubione kolory oddzielone wyłącznie spacją: ")).split(" ")))
print(user_favourite_colours)

if my_favourite_colours == user_favourite_colours:
    print("Zbiory są takie same.")
else:
    print(f"Kolory wybrane jednocześnie przez obu użytkowników: {my_favourite_colours & user_favourite_colours}")
    print(f"Kolory wybrane wyłącznie przez usera: {user_favourite_colours - my_favourite_colours}")
    print(f"Kolory wybrane wyłącznie przez autora: {my_favourite_colours - user_favourite_colours}")