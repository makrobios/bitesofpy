import json
import re
import csv

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    valid_json = []
    delim = re.compile(r'\||;')
    members = re.sub(delim,',',members)
    for line in csv.DictReader(members.splitlines()[1:]):
        _id = line['id']
        first = line['first_name']
        last = line['last_name']
        mail = line['email']
        
        valid_json.append({'id':_id
                            ,'first_name':first
                            ,'last_name': last
                            ,'email' : mail })
    return json.dumps(valid_json)

print(convert_to_json())