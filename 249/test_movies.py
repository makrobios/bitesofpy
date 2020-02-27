import os
import random
import string
import pytest
from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture()
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    # setup Database
    mdb = MovieDb( DB, DATA, TABLE )  
    mdb.init()
    
    yield mdb
    # teardown
    mdb.drop_table()
# write tests for all MovieDb's query / add / delete


def test_db_init(db):
    assert db.table == "movies"
@pytest.mark.parametrize('query, expected',[
         [{"year":"1939"}, 2],
         [{"year":"1994"}, 1], 
         [{"score_gt":7}, 10],
         [{"score_gt":9.3}, 0] 
         ])
def test_db_query(db, query, expected):
    assert len(db.query(**query)) == expected 

def test_add_to_db(db):
    assert len(db.query(title="Star Wars")) == 0 
    db.add("Star Wars", 1974, 9)
    assert len(db.query(title="Star Wars")) == 1 

def test_delete_from_db(db):
    db.add("Star Wars", 1974, 9)
    assert len(db.query(title="Star Wars")) == 1 
    db.delete(11)
    assert len(db.query(title="Star Wars")) == 0 