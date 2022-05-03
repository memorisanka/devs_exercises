lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, "3"]

print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
print(lista1[0], lista1[3])
lista2[1] = lista3[1]
print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
lista3[2] = input("Wprowadź dowolny tekst: ")
print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
print(f"Lista 3 ma {len(lista3)} elementy.")
lista1.append("Słowo")
print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
del lista1[2]
print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
lista1.extend(lista3)
print(f"Lista 1: {lista1}\nlista 2: {lista2}\nlista 3: {lista3}")
