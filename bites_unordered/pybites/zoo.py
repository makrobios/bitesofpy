class Animal:
    animals = []
    number = 10000
    def __init__(self, name):
        Animal.number += 1
        self.number = Animal.number
        self.name = name.capitalize()
        self.animals.append(self)
    def __str__(self):
        return f"{self.number}. {self.name}" 

    @classmethod
    def zoo(cls):
        return '\n'.join([str(animal) for animal in cls.animals]) 
                    # result = ""
                    # for animal in Animal.animals:
                        # result += animal.__str__()
                    # return result
           


# dog = Animal('dog')
# cat = Animal('cat')
# print(Animal.zoo())
