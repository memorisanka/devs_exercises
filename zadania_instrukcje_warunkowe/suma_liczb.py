podana_liczba = int(input("Wprowadź dowolną liczbę dodatnią: "))
suma = 0
if podana_liczba < 0:
   print("Musisz podać liczbę dodatnią.")
   suma = 0
else:
    for liczba in range(podana_liczba + 1):
        suma += liczba

print(f"Suma liczb od 0 do {podana_liczba} to: {suma}")
print("KONIEC")

# jak dałam if pod for to nie drukował mi się komunikat, że trzeba
# podać liczbę dodatnią.
