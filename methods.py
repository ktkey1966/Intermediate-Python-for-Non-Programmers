import random


class Dog: 
    info = "Is a domestic animal"

    def __init__(self, name):
        print("This dog barks")
        self.lucky_number = random.randint(1, 10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("Chestnut")
dog2 = Dog("Sheba")

dog1.bark()
dog2.bark()


                # Exercise: 3 Use the Chair class from the previous exercise and create an method 
                # that uses one of the instance variables.
class Chair:                           
    info = "Is a piece of furniture"    

    def __init__(self):
        self.color = "brown"

    def paint(self):
        return self.color + " chair"

my_chair = Chair()                     
my_chair.color = "brown"
print(my_chair.paint())                # Call the method using the instance of the class.



