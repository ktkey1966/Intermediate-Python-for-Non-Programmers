#Ex. 03_04 Filter >exFilter.py

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Sue", 0.65), Student("Tom", 0.77), Student("Jane", 0.85)]

failing_students = []
for student in students:
    if student.score < 0.7:
        failing_students.append(student)

filter_list= list(filter(lambda student: student.score < 0.7, students))

print(filter_list)



#Create a filter that will return all even numbers from the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)