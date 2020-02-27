import re

lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor!
Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat?
Sed viverra tellus in hac habitasse platea dictumst vestibulum.
Morbi tempus iaculis urna id volutpat.
Enim blandit volutpat maecenas volutpat.
""".strip().splitlines()

text = " ".join(lorem_ipsum)

def _make_upper(match):
    return match.group(0).upper()

def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sub = re.sub(r"""^(\w)|(\.\s\w)|(\!\s\w)|(\?\s\w)""", _make_upper, text, re.X)  
    return sub

print(capitalize_sentences(text))
