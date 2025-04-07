#Ex. 03_01 begin >advanced_if.py

age = 18
height = 210

#and
if age >= 8 and height >= 135:
    print("You cand ride the roller coaster!")

#or
if age >= 17 or height >= 160:
    print("You can ride the SUPER COASTER!")

#elif (else if)
if height < 120:
    print("Sorry, you can't ride the roller coaster :(")
elif height < 135:
    print("You can have a roller coaster adventure!")
elif height < 200:
    print("You can have a SUPER ADVENTURE!")
else:
    print("You are too tall for the rides :(")



# Exercise: Create an if statement using both "and" and "or" operators with the following variables KKey 3/25/25:
size = 12
weight = 134


if size >= 10 and weight <= 135 or size <= 10 and weight >= 135:
    print("This is a good size for you!")
   

