import unicodedata

def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    accented = []
    for line in text.splitlines():
        for word in line.split():
            for char in word:
                if unicodedata.decomposition(char):
                    accented.append(char.lower())   
    return sorted(accented)

