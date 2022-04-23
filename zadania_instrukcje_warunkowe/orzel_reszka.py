import random
import time

# rzutUzytkownika = input("orzeł (o) czy reszka (r)? ")

rzutKomputera = random.randint(0, 2)
array = ['o', 'r']
wynikUzytkownika = 0
wynikKomputera = 0

rzut_komputer = random.choice(array)
games = 0
while games < 3:
    rzutUzytkownika = input("orzeł (o) czy reszka (r)? ")
    rzutKomputera = random.randint(0, 1)
    # print("3...")
    # time.sleep(1)
    # print("2...")
    # time.sleep(1)
    # print("1...")
    # time.sleep(1)
    if rzutKomputera == 0:
        print("Komputer: reszka")
    else:
        print("Komputer: orzeł")

    if rzutKomputera == 0 and rzutUzytkownika == "o":
        wynikUzytkownika += 1
    elif rzutKomputera == 1 and rzutUzytkownika == "r":
        wynikKomputera += 1
    else:
        print("REMIS")
    games += 1
print(f"Wynik:")
print(f"Użytkownik: {wynikUzytkownika}")
print(f"Komputer: {wynikKomputera}")

# wynik użytkownika i wynik komputera zawsze się zeruje
# jak zrobić, aby się nie zerował?
