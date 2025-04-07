#Ex: 05_03 create a ReadFile.py to read the file created in exFile.py KKey 3/30/2025

#file = open("fileme.txt", "r")

# file_text = file.read()
# print(file_text)

# lines = file.readlines()
# print(lines)


# for line in file:
#     print(line)

# file.close()

#Create a file numbers.txt with a few numbers in it
#Mulitply all the numbers in the file, print result

file = open("exnumber.txt", "r")

total = 1
for line in file:
    try:
        number = float(line)
        total *= number
    except Exception as e:
        pass

print(total)

file.close()




