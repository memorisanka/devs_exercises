# squere
for i in range(6):
    for j in range(7):
        print("*", end="")
    print()

print()

# empty squere
stars = ["*****", "*   *", "*   *", "*   *", "*****"]
for i in stars:
    print(i)

print()

for i in range(5):
    if i == 0 or i == 4:
        print("*****")
    else:
        print("*   *")
print()

# tree
tree = ["   *   ", "  ***  ", " ***** ", "*******"]
for i in tree:
    print(i)