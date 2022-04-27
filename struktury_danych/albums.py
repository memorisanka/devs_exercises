albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza',
          'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

for album in albums.keys():
    print(album)

search = input("Podaj nazwę albumu, którego wykonawcę chcesz poznać: ")
if search.title() in albums.keys():
    print(f"""Autorem albumu "{search.title()}" jest {albums[search.title()]}. """)
else:
    print("Brak danych.")

