#Ex. 03_03 Map >exMap.py

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Sue", 0.65), Student("Tom", 0.77), Student("Jane", 0.85)]

student_results = []

for student in students:
    # if student.score >= 0.7:
    #     student_results.append(f"{student.name} Passed")
    # else:
    #     student_results.append(f"{student.name} Failed")


    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed")

#Short version of the code above
map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed", students))

print(map_results)

#Create a map that multiplies all these numbers by 2

numbers = [1, 2, 3, 4, 5]

for number in numbers:
     print(number * 2)
