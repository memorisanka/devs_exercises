
print(f"To jest program obliczający BMI.")
print("*" * 30)
wzrost = 1.60
wiek = 35
wzrostUzytkownika = float(input("Podaj swój wzrost w metrach: "))
wagaUzytkownika = int(input("Podaj swoją wagę w kilogramach: "))
BMI = round(wagaUzytkownika / (wzrostUzytkownika ** 2), 2)
print("*" * 30)
print(f"Twoje BMI wynosi {BMI}.")
