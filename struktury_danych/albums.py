albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza',
          'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}
#wyświetla wszystkie albumy
for album in albums:
    print(album)
#pobiera od użytkownika nazwę albumu
search = input("Podaj nazwę albumu, którego wykonawcę chcesz poznać: ").title()
#szuka, czy w słowniku jest podany autor i zwraca, kto jest jego autorem
if search in albums:
    print(f"""Autorem albumu "{search}" jest {albums.get(search)}. """)
else:
    print("Brak danych.")

