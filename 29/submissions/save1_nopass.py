def get_index_different_char(chars):
    pos = [str(char).isalpha() for char in chars]:
    if pos > 1:
        return pos.index(False)
    else:
        return pos.index(True)