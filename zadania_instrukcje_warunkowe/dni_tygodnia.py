dniTygodnia = {1: "Poniedziałek",
               2: "Wtorek",
               3: "Środa",
               4: "Czwartek",
               5: "Piątek",
               6: "Sobota",
               7: "Niedziela"}
wybierzDzien = int(input("Podaj liczbę dnia tygodnia 1 - 7: "))
print(dniTygodnia.get(wybierzDzien, "Nie ma takiego dnia."))