waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
BMI = round((waga / wzrost ** 2), 2)
print(f"Twoje BMI jest równe: {BMI}")
if BMI < 18.5:
    print("Masz niedowagę.")
elif 18.5 <= BMI < 24:
    print("Twoja waga jest w normie. Tak trzymaj.")
elif 24 <= BMI < 26.5:
    print("Masz lekką nadwagę.")
elif 26.5 <= BMI < 30:
    print("Masz nadwagę. Zgłoś się do dietetyka.")
elif 30 <= BMI < 35:
    print("Masz nadwagę i otyłość I stopnia. Zgłoś się do dietetyka.")
elif 35 <= BMI < 40:
    print("Masz nadwagę i otyłość II stopnia. Zgłoś się do dietetyka.")
else:
    print("Masz nadwagę i otyłość III stopnia. Zgłoś się do dietetyka.")


