from csv import DictReader
import os
from urllib.request import urlretrieve
from collections import Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = 'bite_output_log.txt'
DATA = os.path.join(TMP, LOGS)
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
if not os.path.isfile(DATA):
    urlretrieve(f'{S3}/{LOGS}', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        self.data = data
        self.result = []
        with open(self.data) as d:
            for row in DictReader(d.readlines()):
                self.result.append(row)
            return self.result
        
    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({row['bite'] for row in self.result})

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({ row['bite'] 
                      for row in self.result 
                        if row['completed'] == 'True'}) 

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({ row['user'] for row in self.result}) 

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len({ row['user'] 
                      for row in self.result
                        if row['completed'] == 'True'})

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        self.unique_bites = {row['bite'] for row in self.result}
        self.just_bites = [row['bite'] for row in self.result]
        return max([( bite, self.just_bites.count(bite) ) 
            for bite in self.unique_bites], key=lambda x: x[1])[0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        users = [ bite['user'] 
                  for bite in self.result 
                  if bite['completed'] == 'True' ]
        return Counter(users).most_common(n=1)[0][0]
        