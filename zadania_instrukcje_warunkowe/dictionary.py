menu = ("""
MENU SŁOWNIKA
-----------------------------------------------------
Dodaj słowo wraz z definicją - wybierz 1
Znajdź definicję słowa - wybierz 2
Usuń słowo wraz z definicją ze słownika - wybierz 3
Zakończ program - wybierz 4
-----------------------------------------------------
""")
# what_to_do = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))


dictionary = {}
flag = True
while flag:
    print(menu)
    what_to_do = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))
    if what_to_do == 1:
        word = input("Podaj słowo: ")
        definition = input("Podaj definicję podanego słowa: ")
        dictionary.update({word: definition})
    elif what_to_do == 2:
        find_definition = input("Podaj słowo, którego definicję chcesz uzyskać: ")
        print(dictionary[find_definition])
    elif what_to_do == 3:
        delete_word = input("Które słowo wraz z definicją chcesz usunąć? ")
        dictionary.pop(delete_word, "Nie ma takiego słowa.")
    elif what_to_do == 4:
        flag = False
    else:
        print("Błąd działania programu.")

# while 0 < what_to_do <= 3:
#     if what_to_do == 1:
#         word = input("Podaj słowo: ")
#         definition = input("Podaj definicję podanego słowa: ")
#         dictionary.update({word: definition})
#         what_to_do = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))
#     elif what_to_do == 2:
#         find_definition = input("Podaj słowo, którego definicję chcesz uzyskać: ")
#         print(dictionary[find_definition])
#         what_to_do = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))
#     elif what_to_do == 3:
#         delete_word = input("Które słowo wraz z definicją chcesz usunąć? ")
#         dictionary.pop(delete_word, "Nie ma takiego słowa.")
#         what_to_do = (int(input("Wybierz działanie (wpisz cyfrę od 1-4): ")))
#     else:
#         print("Błąd działania programu.")
# else:
#     print("Koniec programu.")
