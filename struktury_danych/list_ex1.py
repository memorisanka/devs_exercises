import string
# translate
sentence = "Komu wody, komu wody?"
# usunięcie znaków interpunkcyjnych
array = string.punctuation
punctation_mark = [",", ".", ":", ";", "!", "?"]
for letter in sentence:
    if letter in punctation_mark:
        sentence = sentence.replace(letter, "")
# utworzenie listy słów
l_sentence = sentence.split()
print(l_sentence)
# odwrócenie kolejności listy
rev_sentence = l_sentence[::-1]
print(rev_sentence)
print(array)
