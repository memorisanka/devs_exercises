text = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains " \
       "all of the letters of the English alphabet"

len_words = [len(word) for word in text.split(" ") if word.lower() != "the"]
print(len_words)