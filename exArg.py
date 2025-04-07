#Ex: 05_01 Arguments.py KKey 3/30/2025

import sys


#Ex: Make a script that mulitplies all number arguments passed to it
#Ex: 05_02 Arguments.py 2 3 4 5

total = 1
del(sys.argv[0])
for argument in sys.argv:
    try:
        number = float(argument)
        total *= number
    except Exception as e:
        print(e)
        print("Only number are excepted") 
        sys.exit(1)

print(total)

