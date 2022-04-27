albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza',
          'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

for album in albums.keys():
    print(album)

menu = """
    MENU
    ----------------------------------
    Wybierz:
    1 - wyszukiwarka wykonawców po nazwie albumu
    2 - dodawanie pozycji do słownika;
    3 - usuwanie rekordu ze słownika;
    4 - wyjście z programu.
    ----------------------------------"""

flag = True
while flag:
    print(menu)
    choose_menu = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))
    if choose_menu == 1:
        search = input("Podaj nazwę albumu, którego wykonawcę chcesz poznać: ")
        if search.title() in albums.keys():
            print(f"""Autorem albumu "{search.title()}" jest {albums[search.title()]}. """)
        else:
            print("Brak danych.")
    elif choose_menu == 2:
        album_name = input("Podaj nazwę albumu: ")
        artist = input("Podaj wykonawcę: ")
        albums.update({album_name.title(): artist.title()})
    elif choose_menu == 3:
        delete_album = (input("Który album chcesz usunąć?  ")).title()
        del albums[delete_album]
    elif choose_menu == 4:
        print("Koniec działania programu.")
        flag = False
    else:
        print("Błąd działania programu.")

print(albums)

