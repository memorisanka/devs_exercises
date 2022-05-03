names = input("Podaj imiona kilku swoich znajomych (oddzielone spacją): ")
lst_names = names.split(" ")
greetings = ["Jak się masz?", "Cześć!", "Hello!", "Miło Cię znowu widzieć!", "Witaj!", "Dobrze Cię znowu zobaczyć!",
             "Dawno się nie widzieliśmy!", "Jak się dzisiaj czujesz?", "Opowiedz, co u Ciebie ciekawego."]
for name, greeting in zip(lst_names, greetings):
   print(greeting, name)