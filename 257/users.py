import re

def _clean_up(name):
    name = name.strip(',')
    name = re.sub(r',+', ' ', name)
    return name

def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwd = passwd.strip()
    users = {}
    for line in passwd.split('\n'):
        user = _clean_up(line.split(':')[0])
        name = line.split(':')[4]
        users[user] = name
    return users
 
