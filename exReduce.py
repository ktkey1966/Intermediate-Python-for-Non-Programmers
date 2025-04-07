#Ex. 03_05 Reduce >exReduce.py

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Sue", 0.65), Student("Tom", 0.77), Student("Jane", 0.85)]

total_score = 0
for student in students:
    total_score += student.score

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total , students, 0)

print(round(reduce_total / len(students), 2))



#Create a reduce that will multiply all the numbers in the list KKey 3/25/25

numbers = [1, 2, 3, 4, 5]

total_multiply = reduce(lambda total, number: number * total, numbers, 1)
print(total_multiply)

