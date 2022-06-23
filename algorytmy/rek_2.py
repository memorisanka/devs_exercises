vowels = 'aeiouyAEIOUY'
freq = {}


def v_search(txt: str, n=0) -> dict:
    while n < len(txt):
        if txt[n] in vowels:
            if txt[n] in freq:
                freq[txt[n]] += 1
            else:
                freq[txt[n]] = 1
        return v_search(txt, n + 1)


v_search("aaa AAAA bbbb ee iiii".lower())
print(freq)
