#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""
from collections import namedtuple
from collections import Counter
import operator

Pair = namedtuple('Pair', 'wine cheese similarity')

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

def _get_similarity(cheese, wine):
    common = Counter(cheese.lower()) & Counter(wine.lower())
    lenc = len(cheese)
    lenw = len(wine)
    similarity = sum(common.values()) / (1 + pow(lenc - lenw, 2))
    return Pair(cheese, wine, similarity)

def _make_similarity_matrix(wine_type="all"):
    try :
        winelist = { 'red' : RED_WINES, 
                     'white' : WHITE_WINES,
                     'sparkling' : SPARKLING_WINES } 
        if wine_type == 'all':
            wines = winelist['red'] + winelist['white'] + winelist['sparkling']
        else:
            wines = winelist[wine_type]
    except KeyError:
        raise ValueError
    scores = []
    for cheese in CHEESES:
        for wine in wines:
            scores.append( _get_similarity(wine, cheese) )
    return scores
    

def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    scores = _make_similarity_matrix(wine_type)
    best_match = max(scores, key = lambda x: x.similarity)
    return (best_match.wine, best_match.cheese, best_match.similarity)


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    scores = _make_similarity_matrix()
    wines = []
    for wine in RED_WINES + WHITE_WINES + SPARKLING_WINES:
        score = [score for score in scores if score.wine == wine]
        # sorted "-x.similarity" reverses sort order
        bestfive = sorted(score, key=lambda x: (-x.similarity, x), reverse=False)[:5]
        wines.append( (wine, [best.cheese for best in bestfive]) )
    return sorted(wines, key= lambda x: x[0])
