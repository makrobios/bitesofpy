from collections import UserDict
from typing import Any


class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, val):
        self[key] = val 

    def __delattr__(self, key):
        del self[key]

class JsUser(UserDict):

    # def __init__(self, **mettigel):
    #     super().__init__(**mettigel)

    def __getattr__(self, key):
        return self.data[key]


    def __setattr__(self, key, val):
        self[key] = val


    # def __delattr__(self, key):
    #     del self.data[key]

# class JsObject
# jsobj = JsObject(a = 1, b = 2, c = 3)
# print(jsobj)

# class UserDict
# userdict = UserDict(a=1, b=20)
# print(userdict)

# class JsUser(UserDict)
jsuser = JsUser(a=1, b=2, c=3)
print(jsuser)