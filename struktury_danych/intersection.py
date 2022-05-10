a = set([x * 2 for x in range(15)])
b = set([y * 3 for y in range (20) if y % 2 == 0])
print(a)
print(b)

print("Listy mają przynajmniej jeden wspólny element.") if len(a.intersection(b)) > 0 else print("Nope. Listy nie mają nic wspólnego.")