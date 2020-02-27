import re

def chkchar(*args, pw, mode=(True, )):
    result = []
    for method in args:
        result.append( [ getattr(char, method)() for char in pw ] )
    for test in zip(*result):
        if mode == test:
            return True
    else:
        return False

def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    pw = password
    score = 0 
    score += sum([ chkchar("isupper", pw=pw) and chkchar("islower", pw=pw),
                   chkchar("isdigit", pw=pw) and chkchar("isalpha", pw=pw),
                   chkchar("isalnum", "isprintable", pw=pw, mode= (False, True)) ])
    if len(pw) > 7:
        score += 1
        if not re.findall(r"(.)\1",pw[:8]):
            score += 1
    return score