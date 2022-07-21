def ok_module_info(name: str) -> None:
    print(f"Moduł: {name} - zainstalowany poprawnie.")


def error_module_info(name: str) -> None:
    print(f"Brak modułu: {name}.")
    print(f"Instalacja: pip install {name}")
    print("---------------------------")


def get_horizon_data(nasaids: list, names: list, colors: list, sizes: list, start_date="2018-01-01"):
    """nasaids = [1, 2, 3, 4]
    funkcja bazuje na projekcie https://github.com/chongchonghe/Python-solar-system"""

    from astropy.time import Time
    from astroquery.jplhorizons import Horizons
    from numpy import double

    data = {
        "info": "Baza danych o pozycjach i prędkościach planet w określonym dniu.",
        "date": start_date
    }

    for i, nasaid in enumerate(nasaids):
        obj = Horizons(
            id=nasaid, location="@sun", epochs=Time(start_date).jd,
            id_type="id"
        ).vectors()
        print("---------------------------------------------------------------------")
        print(f"Pobieramy dane dla{names[i]}: ")
        print(obj)

        data[nasaid] = {
            "name": names[i],
            "size": sizes[i],
            "color": colors[i],
            "r": [double(obj[xi]) for xi in ["x", "y", "z"]],
            "v": [double(obj[vxi]) for vxi in ["vx", "vy", "vz"]]
        }


if __name__ == "__main__":
    print("To jest moduł dodatkowy dla projektu.")
