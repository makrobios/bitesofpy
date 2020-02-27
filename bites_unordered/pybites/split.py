import re


def get_sentences(content):
    """Return a list of sentences as extracted from the text passed in.
    A sentence starts with [A-Z] and ends with [.?!]"""
    content = ' '.join(content.split('\n'))
    pat = re.compile(r'[A-Z].*?[^A-Z]+[.!?](?:\s|$)')
    sentences = re.findall(pat, content)
    return [sent.rstrip() for sent in sentences]

