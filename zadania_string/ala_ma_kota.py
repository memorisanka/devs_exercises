liczbaKotow = int(input("Ile kotów ma Ala? "))
print(f"Dzisiaj Ala znalazła jeszcze 3 koty idąc do pracy przez park...")
liczbaKotow += 3
zdanie = f"Teraz Ala ma już {liczbaKotow} kotów."
print(zdanie)
modZdanie1 = zdanie.split(" ")
print(modZdanie1)
modZdanie2 = zdanie.replace(" ", ",")
print(modZdanie2)
modZdanie3 = zdanie.replace(" ", "\n")
print(modZdanie3)
print(zdanie.islower())
modZdanie4 = zdanie.lower()
print(modZdanie4)
modZdanie5 = zdanie.capitalize()
print(modZdanie5)
