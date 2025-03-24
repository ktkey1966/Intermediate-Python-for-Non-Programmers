import random


class Dog: 
    info = "Is a domestic animal"

    def __init__(self, name):
        print("This dog barks")
        self.lucky_number = random.randint(1, 10)
        self.name = name


dog1 = Dog("Chestnut")
dog2 = Dog("Sheba")


print(dog1.name)
print(dog2.name)    



                                        # Exercise: 2
                                        # Create a instance variable

class Chair:                            # Create a class named Chair
    info = "Is a piece of furniture"    # Create a class variable inside the class.


my_chair = Chair()                      # Create an instance of the class.
my_chair.color = "brown"                # Create an instance variable.

