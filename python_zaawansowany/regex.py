import re
from typing import Any


def if_match(match: Any) -> None:
    if match:
        print("Match!")
    else:
        print("No match!")


def if_found(search: Any) -> None:
    if search:
        print("Found!")
    else:
        print("Not found!")


def main():
    txt = "a88&^^^$6hhhfbcRg553"
    match = re.match(r'^[a-zA-Z0-9]+$', txt)
    if_match(match)

    txt2 = "gjgjjg"
    match2 = re.match(r'^b|^0', txt2)
    if_match(match2)

    txt3 = "aajfjfjfggg_uutttt"
    match3 = re.match(r'^([a-z]+)_([a-z]+)$', txt3)
    if_match(match3)

    txt4 = "hiss"
    search1 = re.search(r'.*[s]{2,}$', txt4)
    search1 = re.search(r'.*ss+', txt4)
    if_found(search1)

    txt5 = "Python should mAtch"
    search2 = re.match(r'[a-zB-Z\s]{6,}$', txt5)
    if_match(search2)

if __name__ == "__main__":
    main()