import json

def reverseDictionary(**kwargs):
    print(kwargs)
    dictionary = dict()
    for key, value in kwargs.items():
        dictionary[value] = key
    print(dictionary)
    with open("output.txt", "w") as outfile:
        json.dump(dictionary, outfile)

reverseDictionary(a=1, b=2, c=3)