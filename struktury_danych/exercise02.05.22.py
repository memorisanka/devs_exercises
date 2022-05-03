import json
import pickle
# nukleotydy = {"A": "Adenina", "C": "Cytozyna", "G": "Guanina"}
# nukl_2 = {"X": "Nienzany",  "T" : "Tymina"}
# nukl_3 = {"U": "Uranium", "C": "Cytozona"}
#
# nukleotydy = {**nukleotydy, **nukl_2, **nukl_3}
# nukleotydy.update(nukl_2)
# for nukl in nukleotydy:
#     print(nukl)
#
# for nukl in nukleotydy.values():
#     print(nukl)
#
# # print(nukleotydy.get('x', "Nie ma takiego klucza"))
# nukleotyd = input("Podaj symbol")
# if nukleotydy.get(nukleotyd) != None:
#     pass
# else:
#     pass
#
#
#
# nukleotydy['U'] = "Uracyl"
# print(nukleotydy)
# del nukleotydy['U']
# nukleotydy.clear()

x = [1, 2, 3]
y = x
x.append(4)
import copy
z = [[1], [2], [3]]
print(id(z[0]))
u = z.copy()
print(z.append([4]))
z[0].append(4)
print(z)
print(u)
p = copy.deepcopy(z)
print(z)
print(p)
p[0].append(10)
print(z)

print(p)
q = json.load(json.dumps(z))
n = pickle.loads(pickle.dumps(z))

