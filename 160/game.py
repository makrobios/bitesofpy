import csv
import os
from urllib.request import urlretrieve
import pysnooper

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    urlretrieve(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )

#@pysnooper.snoop()
def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_mapping = dict()

    with open(BATTLE_DATA) as bdata:
        defender = bdata.readline().split(',')[1:]

        for line in bdata.readlines():
            attacker, *result = line.split(",")
            defeat_mapping[attacker] = [ defender[idx].strip()
                                        for idx, winner in enumerate(result) 
                                        if winner.strip() == 'win' ] 
    return defeat_mapping


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    # ...
    if not all([player in defeat_mapping.keys() for player in [player1, player2]]):
        raise ValueError(f"Please provide one of the following choices: \n {defeat_mapping.keys()}")
    if player1 == player2:
        return "Tie"
    elif player2 in defeat_mapping[player1]:
        return player1 
    else:
        return player2 

