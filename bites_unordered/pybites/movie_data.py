#Pybites Bite 30 https://codechalleng.es/bites/30/ 

import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

#BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/home/ch/programming/pybites/data/'

fname = 'movie_metadata.csv'
#remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
#urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')
directors = defaultdict(list)

def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    file = csv.DictReader(open(MOVIE_DATA))
    for movie in file:
        director = movie['director_name']
        title = movie['movie_title'].strip()
        try:
            year = int(movie['title_year'].strip())
            if year < 1961:
                continue
        except ValueError:
            continue
        score = float(movie['imdb_score'])
        score = round(score,1)
        directors[director].append(Movie(title, year, score))
    return directors

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total_score = 0
    num_of_movies = len(movies)
    mean_score = 0
    for num, movie in enumerate(movies):
        total_score+=movie.score
    return round(total_score/num_of_movies,1)

def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    avg_scores = []
    score = 0 
    for director in directors:
        movies = directors[director]
        num_of_movies = len(movies)
        if num_of_movies < MIN_MOVIES:
            continue
        for movie in movies:
            score += movie.score
        score = round(score / num_of_movies,1)
        avg_scores.append((director, score))
        score = 0
    return sorted(avg_scores,key=lambda x:-x[1])

#out = get_movies_by_director()

#calc_mean_score(out['Woody Allen'])

# avg = get_average_scores(out)

# print(avg[0])

