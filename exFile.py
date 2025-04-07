#Ex. 05_02 create a file in python KKey 3/30/2025
                    #This creates a file in the current directory

# file = open("fileme.txt", "x")

# file.write("This is my test file")

# file.close()

                    #Overwrite the file
# file = open("fileme.txt", "w")

# file.write("I can write to a file!")

# file.close()


                    #Append to the file
# file = open("fileme.txt", "a")

# file.write("I can append this file!")

# file.close()



#Ex. Create a file named after the first argument passed to the script

import sys

file_name = sys.argv[1]

print(file_name, "w")

file.close()
