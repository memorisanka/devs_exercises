from collections import Counter
# pobranie liczby od użytkownika
number = input("Podaj dowolną liczbę: ")
# utworzenie pustego słownika na zliczenie wystąpień danej cyfry
counts = {}
# utworzenie pustej listy
numbers = []
# dodatnie do listy numbers osobno każdej cyfry z warości pobranej przez użytkownika
for i in number:
    numbers.append(i)

for num in numbers:
    counts.update({num: numbers.count(num)})
print(counts)
# print(Counter(number))