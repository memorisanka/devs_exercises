alphabet = []
alphabet_rev = []

for i in range(97, 123):
    alphabet.append(chr(i))
for j in range(90, 64, -1):
    alphabet_rev.append(chr(j))

print(alphabet)
print(alphabet_rev)
