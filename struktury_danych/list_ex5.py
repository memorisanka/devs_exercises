text = input("Podaj dowolne zdanie: ")
# usunięcie znaków interpunkcyjnych
interpunction = [",", ".", ":", ";", "-"]
for i in text:
    if i in interpunction:
        text = text.replace(i, "")
# utworzenie listy słów i podanie liczby wyrazów
text = text.split(" ")
if len(text) == 1:
    print(f"Długość podanego zdania to {len(text)} wyraz.")
elif 1 < len(text) <= 4:
    print(f"Długość podanego zdania to {len(text)} wyrazy.")
elif len(text) >= 5:
    print(f"Długość podanego zdania to {len(text)} wyrazów.")
else:
    print(f"Błędne dane.")

# szukanie słów zaczynających się od dużej litery
count = 0
for word in text:
    if word[0].isupper():
        print(f"Słowo zaczynające się dużą literą: {word}")
        count += 1

if count == 0:
    print("Brak słów zaczynających się na dużą literę.")

# sprawdzenie, czy w zdaniu są podane na liście list_of_words wyrazy
list_of_words = ["i", "w", "na", "pod", "dla"]

count2 = 0
for char in text:
    if char in list_of_words:
        print(f'''Słowo "{char}" ma indeks: {text.index(char)}.''')
        count2 += 1

if count2 == 0:
    print('''W podanym zdaniu brak słów: „i”, „w”, „na”, „pod”, „dla".''')

# zwrócienie listy posortowanej w porządku odwrotnym do alfabetycznego
print(sorted(text, reverse=True))
