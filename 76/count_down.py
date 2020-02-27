import re
from functools import singledispatch
import datetime
import itertools

@singledispatch
def count_down(string):
    # TODO: Learn how to use singledispatch!
    start = len(string)
    # range going backwards starting from length of input string
    for i in range(start, 0, -1):
        print(string[:i])

@count_down.register(int)
def __(integer):
    string = str(integer)
    count_down(string)

@count_down.register(float)
def __(flt):
    string = str(flt)
    count_down(string)

@count_down.register(range)
@count_down.register(list)
def __(lst):
    lst = list(lst)
    string = ''.join( str(item) for item in lst )
    count_down(string)

@count_down.register(dict)
def __(dct):
    string = ''.join( str(key) for key in dct.keys() )
    count_down(string)

@count_down.register(tuple)
def __(tple):
    string = ''.join( str(key) for key in tple )
    count_down(string) 

@count_down.register(set)
def __(s):
    string = ''.join( str(item) for item in list(s))
    count_down(string)

@count_down.register(type)
def __(types):
    raise ValueError(f'{types} is not supported')


@count_down.register(re.Pattern)
@count_down.register(itertools.compress)   
@count_down.register(datetime.datetime)
def __(types):
    raise ValueError(f'{types} is not supported')
    
