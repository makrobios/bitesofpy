from collections import namedtuple
import random
import string
import itertools
import pysnooper

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    deck = []
    numbers = [str(num) for num in NUMBERS]
    actions = random.choices(ACTIONS, k=n)
    rnd_cards = random.sample( range(n * 4), n)

    if n > 26:
        raise ValueError("given n is too big, 26 is maximum")

    for idx, (card, num) in enumerate( itertools.product(string.ascii_uppercase[:n],
                                                      numbers) ):
        action = None
        if idx in rnd_cards:
            action = actions.pop(0)
        deck.append(PawCard(card + str(num) , action))
    return deck