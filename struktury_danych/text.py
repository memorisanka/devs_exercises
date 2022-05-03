text = "Once upon a midnight dreary, while I pondered, weak and weary, " \
       "Over many a quaint and curious volume of forgotten lore, While I nodded, " \
       "nearly napping, suddenly there came a tapping, As of someone gently rapping, " \
       "rapping at my chamber door. This visitor, I muttered, tapping at my chamber door " \
       "- Only this, and nothing more."

#utworzenie pustego słownika, aby zapisać w nim liczbę wystąpień każdego słowa
counts = dict()
# usunięcie znaków interpunkcyjnych
interpunction = [",", ".", ":", ";", "-"]
for i in text:
    if i in interpunction:
        text = text.replace(i, "")
# utworzenie listy słów
words = text.split(" ")
# zliczenie wystąpień każdego słowa do słownika
for word in words:
    if word in words:
        counts.update({word: words.count(word)})
print(counts)
