import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    length_check = 5 < len(password) < 13
    digit_check = any(c.isdigit() for c in password)
    upper_check = sum([c.isupper() for c in password]) > 0
    lower_check = sum([c.islower() for c in password]) > 1
    punct_check = any([c for c in password if c in PUNCTUATION_CHARS])
    notused_check = password not in used_passwords

    if (
        length_check
        and digit_check
        and upper_check
        and lower_check
        and punct_check
        and notused_check
    ):
        used_passwords.update({password})
        return True
