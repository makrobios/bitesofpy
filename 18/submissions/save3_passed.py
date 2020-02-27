import re
import os
import urllib.request
from collections import defaultdict
# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)
freq = defaultdict(int)
stopwords = list()
with open(stopwords_file) as stop:
    for line in stop:
        stopwords.append(line.strip())

def get_harry_most_common_word():
    with open(harry_text) as harry:
        count = 0
        for line in harry:
            count += 1
            line = re.sub(r"'|,|\.|;","",line).lower()
            for word in line.split():
                if word not in stopwords and word.isalpha():
                    # with defaultdict:
                    freq[word] += 1
                    # without defaultdict: 
                    # if freq.get(word):
                    #     freq[word] += 1
                    # else:
                    #     freq[word] = 1
        return sorted(freq.items(),key=lambda x: x[1])[-1]
         
