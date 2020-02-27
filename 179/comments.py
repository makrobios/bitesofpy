import re

def strip_comments(code):
    # see Bite description
    multi = re.sub(r'( +)?""".*?"""\n', '', code, flags=re.DOTALL)
    comment = re.sub(r"^(\s+)?#.*\n","",multi, flags=re.MULTILINE)
    inline = re.sub(r"(.*?)  # .*\n",r"\1",comment)
    return inline
