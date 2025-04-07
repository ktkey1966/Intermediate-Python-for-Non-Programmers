#Ex. 03_02 Begin >exSwitch.py 
# Note: Switch statements require Python 3.10 or higher
'''
direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case _:
        print("Invalid direction")'

'''

#Ex. Create a switch statement that will print the following numbers: KKey 3/25/25

direction = input("Enter a number: ")

match direction:
    case "1":
        print("This is One")
    case "2":
        print("This is Two")
    case "3":
        print("This is Three")
    case "4":
        print("This is Four")
    case "5":
        print("This is Five")
    case _:
        print("This is an invalid number :( ")
