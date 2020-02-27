import json
import re

def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            movies.append(json.loads(f.read()))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    awards = [(movie['Title'], movie['Awards']) for movie in movies]
    result = []
    for award in awards:
        noms = re.search('(\d+) nomination', award[1]).group(1)
        result.append((award[0], int(noms)))
    return max(result, key=lambda x: x[1])


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    pass
