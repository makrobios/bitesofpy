from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'

# Decorator Factory
def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def wrap(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            nonlocal start, end
            text = list(kwargs['text'])
            #end = len(text) if end > len(text) else end
            if not start > len(text):
                if end > len(text):
                    end = len(text)
                elif end < 0:
                    end = 0
                start = 0 if start < 0 else start
                DOTS = (end - start) * DOT
                text[start:end] = DOTS
            text = ''.join(text)
            return func(text)
        return wrapped_func
    return wrap


