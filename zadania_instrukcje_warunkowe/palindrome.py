word = "sedes"
print(f"Podany przez Ciebie wyraz to: {word}")
word = word.lower()
if word == word[::-1]:
    print("Podany wyraz jest palindromem.")
else:
    print("Podany wyraz nie jest palindromem.")

