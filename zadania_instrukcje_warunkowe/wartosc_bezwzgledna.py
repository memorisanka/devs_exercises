liczbaUzytkownika = int(input("Podaj dowolną liczbę dodatnią lub ujemną: "))
print(abs(liczbaUzytkownika))
if liczbaUzytkownika < 0:
    print(liczbaUzytkownika * (-1))
else:
    print(liczbaUzytkownika)