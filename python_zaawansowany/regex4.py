import re


num = "1888880.02248555"
match = re.match(r".\d+\.\d+", num)

if match:
    print("Pasuje")
else:
    print("Nie pasuje.")