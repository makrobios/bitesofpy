import statistics

class IntList(list):
    '''IntList takes a list of only ints as input'''
    
    def __init__(self, liste):
        super().__init__()
        self.liste = liste
       # self.mean = 0
        try:
            [int(num) for num in self.liste]
        except (ValueError, TypeError) as e:
            print('IntList only takes a list of integers')
            raise
    def convertToInt(self, other):
        convlist = []
        if not isinstance(other, list):
            other = [other]
        for item in other:
            try:
                 convlist.append(int(item))
            except TypeError:
                print('IntList only takes a list of integers')
                raise TypeError
        return convlist   
    def __iadd__(self, other):
        other = self.convertToInt(other)
        self.liste = self.liste + other
        return IntList(self.liste)
        
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

