import random

class Animal:
    info = "A living organism that feeds on organic matter"

    def __init__(self, name):
        print("This animal is alive")
        self.name = name

class Dog(Animal): 
    info = "Is a domestic animal"

    def __init__(self, name):
        super().__init__(name)
        print("This dog barks very loudly")
        self.lucky_number = random.randint(1,10)
        self.fur = ""

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

class Dachshund(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("This dog is a Dachshund")

dog1 = Dachshund("Chestnut")



# Exercise: 4 Create a inheritance, add a parent class and a child class.

#import random

class Furniture:
    info="large movable equipment, such as tables and chairs"

    def __init__(self, wood):
        print("This furniture is made of wood")
        #self.material = wood

class Chair(Furniture):                           
    info = "Is a piece of furniture"    

    def __init__(self, wood):
        super().__init__(wood)
        self.color = ""
        self.material = wood
        
    def paint(self):
        return self.color + " chair"

class Sofa(Chair):
    
    def __init__(self, wood):
        super().__init__(wood)
        print("This sofa is a 3-seater")

my_chair = Chair("wood")                
my_chair.color = "brown"
print(my_chair.paint())      
