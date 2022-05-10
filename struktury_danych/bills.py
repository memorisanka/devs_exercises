bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ["Roman",  "Ziemniaki", 2.0],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
    ['Rosie', 'Coffe', 4.90],
]

dict_bill = {}
names = []
for i in bill_items:
    names.append(i[0])
print(names)
unique_names = list(set(names))
print(unique_names)
for name in unique_names:
    dict_bill.update({name: {"potrawy": {"name": name, "price": 0}, "cena": 0}})

for i in bill_items:
    dict_bill[i[0]]["potrawy"].append(i[1])
    dict_bill[i[0]]["cena"] += i[2]
print(dict_bill)
