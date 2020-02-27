# https://stackoverflow.com/a/12472564

def flatten(S):
    S = list(S)
    if list(S) == []:
        return S
    if isinstance(S[0], (list, tuple)):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

lol = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
print(flatten(lol))
