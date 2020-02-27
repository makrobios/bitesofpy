from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    
    def __init__(self, number):
        self.number = number
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.number:
            self.number -= 1
            return 'Egg'
        raise StopIteration

eggs = EggCreator(3)

for egg in eggs:
    print(egg)