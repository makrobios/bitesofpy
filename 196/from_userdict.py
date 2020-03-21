from collections import UserDict
from typing import Any

class JsUser(UserDict):
    def __init__(self, **mettigel):
        super().__init__(mettigel)

    def __getattr__(self, key):
        return self.__dict__["data"][key]

    # def __setattr__(self, key, val):
    #     self[key] = val


    # def __delattr__(self, key):
    #     del self[key]
    
    # def __getitem__(self, key):

# class JsUser(UserDict)
jsuser = JsUser(a=1, b=2, c=3)
jsuser.a
jsuser.c = 100
print(jsuser)

# class UserDict
# userdict = UserDict(a=1, b=20)
# print(userdict)


