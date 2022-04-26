sentence = input("Podaj dowolne zdanie: ")
punctuation_mark = [".", ",", ":", ";", "!", "?"]
for i in sentence:
    if i in punctuation_mark:
        sentence = sentence.replace(i, "")
print(sentence)

t_sentence = tuple(sentence.split(" "))
print(t_sentence)
for word in t_sentence:
    print(word + " ", end="")
print("\n")
print(f'''Pierwsze słowo w krotce to: "{t_sentence[0]}", natomiast czwarte to: "{t_sentence[3]}".''')

s_sentence = set(sentence.split(" "))
print(f"Długość zbioru to: {len(s_sentence)}")
for word in s_sentence:
    print(word  + " ", end="")
print("\n")
print(f'''Pierwsze słowo w zbiorze to: "{(list(s_sentence))[0]}", natomiast czwarte to: "{(list(s_sentence))[3]}".''')

if t_sentence[0] == (list(s_sentence))[0] and t_sentence[3] == (list(s_sentence))[3]:
    print("Elementy pierwszy i czwarty są takie same.")
else:
    print("Elementy pierwszy i czwarty nie są takie same.")
