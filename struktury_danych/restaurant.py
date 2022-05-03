orders = {"Klient_1335": {"nazwa_potrawy": "rosół", "ocena": 5, "rachunek": 20.0},
            "Klient_222": {"nazwa_deseru": "lody waniliowe", "rachunek": 5.0 }}

for key in orders:
    print(key)
    for key, value in orders[key].items():
        print(f"{key} : {value}")