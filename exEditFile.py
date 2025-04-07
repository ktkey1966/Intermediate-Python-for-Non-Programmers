#Ex: 05_04 Create an edit file KKey 3/30/2025

#Read
# file = open("fileme.txt", "r")
# lines = file.readlines()
# file.close()

#Edit
#lines.insert(0, "This is a new line\n")

#lines[2] = "Hello, I am a new line\n"


# lines[-1] = lines[-1] + "\n"
# lines.append("This is the last line\n")

# #Write
# file = open("fileme.txt", "w")
# file.writelines(lines)
# file.close()


# Ex: Multiply each number in the exnumber.txt file by 2

#Read
file = open("exnumber.txt", "r")
lines = file.readlines()
file.close()

#Edit
for i in range(len(lines)):
    

    try:
        number = float(lines[i]) * 2
        lines[i] = f"{number}\n"
    except Exception as e:
        pass

# #Write
file = open("exnumber.txt", "w")
file.writelines(lines)
file.close()
