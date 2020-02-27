import re

text = '4 points by okken 3\xa0hours ago\n                                \n                                | 0 comments'

a = re.search(r'\| (\d+)', text)

print(a.group(1))
