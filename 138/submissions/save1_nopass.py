class Animal:
    animals = []
    number = 100000
    def __init__(self, name):
        Animal.number += 1
        self.number = Animal.number
        self.name = name.capitalize()
        Animal.animals.append(self)
    def __str__(self):
        return f"{self.number}. {self.name}" 

    @classmethod
    def zoo(cls):
        for animal in Animal.animals:
            yield animal.__str__()


#dog = Animal('dog')
#cat = Animal('cat')
#for a in Animal.zoo():
#    print(a)
