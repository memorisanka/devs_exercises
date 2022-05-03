n = int(input("Podaj dowolną liczbę naturalną: "))
A = set()
for number in range(0, n+1):
    if number % 2 == 0:
        A.add(number)

B = set()
for number in range(0, n+1):
    if number % 3 == 2:
        B.add(number)

# zamiana na tuple a frozenset?
C = set(A.union(B))
D = set(A.intersection(B))
E = set(A.difference(B))
F = set(A.symmetric_difference(B))
# C = tuple(A | B)
# D = tuple(A & B)
# E = tuple(A - B)
# F = tuple(A ^ B)

for i in C:
    B.add(i)
for j in D:
    B.add(j)
for k in E:
    B.add(k)
for l in F:
    B.add(l)

print(f"Długość zbioru A: {len(A)}")
print(f"Zbiór A: {A}")
print(f"Długość zbioru B: {len(B)}")
print(f"Zbiór B: {B}")

print(A.issubset(B))
if A & B == A:
    print("Zbiór A zawiera się w zbiorze B.")
else:
    print("Zbiór A nie zawiera się w zbiorze B.")

