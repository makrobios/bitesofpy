import string
import random

def gen_key(parts=4, chars_per_part=8):
    code = ''
    for part in range(parts):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=chars_per_part))
        code = '-'.join([code, part])
    return code.lstrip('-')

print((gen_key()))