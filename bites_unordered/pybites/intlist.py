#Pybites Bite 158 https://codechalleng.es/bites/158/

import statistics

class IntList(list):
    '''IntList takes a list of only ints as input'''
    
    def __init__(self, liste):
        super().__init__()
        self.liste = self.convertToInt(liste)
       # self.mean = 0
    def convertToInt(self, other):
        convlist = []
        if not isinstance(other, list):
            other = [other]
        for item in other:
            try:
                 1 + item
                 convlist.append(int(item))
            except (TypeError) as e:
                print('IntList only takes a list of integers')
                raise 
        return convlist   
    def __iadd__(self, other):
        other = self.convertToInt(other)
        self.liste = self.liste + other
        return self.liste
        
    def append(self, other):
        other = self.convertToInt(other)
        if not isinstance(other, list):
            other = [other]
        self.liste = self.liste + other
    
    def __add__(self, other):
        other = self.convertToInt(other)
        return IntList(self.list + other)
    
    @property
    def mean(self):
        return sum(self.liste) / len(self.liste)
    
    @property
    def median(self):
        return statistics.median(self.liste)

#a = IntList([1,2,3])
#a.append(['a',['a'],{'a':1}])
#print(a.liste)
#a += [1,2,3]
#print(a)
