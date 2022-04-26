from pprint import pprint
people = {"67030456789": {"kolor_oczu": "niebieski",
                        "imie": "Jan",
                        "nazwisko": "Kowalski",
                        "wiek": 55},
          "65071423571": {"kolor_oczu": "zielony",
                        "imie": "Amelia",
                        "nazwisko": "Krawiec",
                        "wiek": 57},
          "87031505671": {"kolor_oczu": "brązowy",
                        "imie": "Janusz",
                        "nazwisko": "Pucuś",
                        "wiek": 35},
          "88042745098": {"kolor_oczu": "zielony",
                        "imie": "Izabela",
                        "nazwisko": "Gęsipiórek",
                        "wiek": 34},
          "09273006745": {"kolor_oczu": "szary",
                        "imie": "Rufus",
                        "nazwisko": "Weider",
                        "wiek": 12}}
mothers = ["Anna", "Zofia", "Irena", "Angelika", "Renata"]
wzrost = [192, 131, 210, 193, 173]

for person, mother, height in zip(people, mothers, wzrost):
    people[person]["Matka"] = mother
    people[person]['wzrost'] = height

# for pesel in people:
#     if pesel == "67030456789":
#         people["67030456789"].update({"imie_matki": "Anna"})
#     if pesel == "65071423571":
#         people["65071423571"].update({"imie_matki": "Alina"})
#     if pesel == "87031505673":
#         people["87031505673"].update({"imie_matki": "Genowefa"})
#     if pesel == "88042745098":
#         people["88042745098"].update({"imie_matki": "Julia"})
#     if pesel == "09273006745":
#         people["09273006745"].update({"imie_matki": "Franciszka"})


# usuwa dane osoby z peselem kończącym się na "1", ale nie usuwa samego peselu
for pesel in list(people.keys()):
    if pesel.endswith("1"):
        del people[pesel]
        # people[pesel].clear()
#pprint(people)

#
# # nie wiem, jak wydrukować bez {}
for key in people:
    print(f"Nr Pesel: {key}")
    for key, value in people[key].items():
        print(f"{key} : {value}")