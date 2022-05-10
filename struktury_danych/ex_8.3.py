dict1 = {"a" : 3, "b" : 1, "c" : 10, "d" : 15, "e" : 20}
dict2 = {}
for key, value in dict1.items():
    dict2[value] = key
print(dict2)