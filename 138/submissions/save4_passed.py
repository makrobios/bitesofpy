class Animal:
    animals = []
    number = 10000
    def __init__(self, name):
        Animal.number += 1
        self.number = Animal.number
        self.name = name.capitalize()
        Animal.animals.append(self)
    def __str__(self):
        return f"{self.number}. {self.name}" 

    @classmethod
    def zoo(cls):
        result = ""
        for animal in Animal.animals:
            result += animal.__str__()
        return result
           
