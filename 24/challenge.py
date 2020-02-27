from abc import ABC, abstractmethod

class Challenge(ABC):
    @abstractmethod
    def __init__(self, number, title):
        self.number = number 
        self.title = title 
        
    @abstractmethod
    def verify(self, number):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass
     
class BlogChallenge(Challenge):
    def __init__(self, number, title, merged_prs):
        super(BlogChallenge, self).__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, no):
        self.no = no 
        return True if self.no in self.merged_prs else False 
    
    @property   
    def pretty_title(self):
        return f'PCC{self.number} - {self.title}'

class BiteChallenge(Challenge):

    def __init__(self, number, title, result):
        super(BiteChallenge, self).__init__(number, title)
        self.result = result

    def verify(self, _res):
        self._res = _res
        return True if self._res == self.result else False

    @property
    def pretty_title(self):
        return f'Bite {self.number}. {self.title}' 
