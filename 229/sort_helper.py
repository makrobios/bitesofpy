# coding: utf-8
from best_programming_books import load_data, _get_soup, Book

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper(iterable, *args):
#         return func(iterable, *args)
#     return wrapper
    

# def sort_helper(iterable, *args):
#     it = iterable
#     for arg in args:
#         reverse = False
#         if arg < 0:
#             reverse = True
#         pos = abs(arg) - 1
#         it = sorted(it, key=lambda x: x[pos], reverse=reverse)
#     return it


# l = [(c, n) for c in 'abc' for n in [1,2,3] ]

# sort_helper(l, -1)


books = load_data()
sample = books[:5]
def _sort_helper(iterable, *args):
    for arg in reversed(args):
        reverse = False 
        if "-" in arg:
            reverse = True
        arg = arg.strip("-")
        iterable.sort(key= lambda x: getattr(x, arg), reverse=reverse)
    return iterable

print("*Unsorted*:::")
print([(b.title, b.rating, b.year) for b in sample])
print("*Sorted*:::")
print([(b.title, b.rating, b.year) for b in _sort_helper(sample, "year")])

