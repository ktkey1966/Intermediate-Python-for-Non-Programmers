#Ex. Return a list of students who's name starts with "M". Use the filter function.

show_expected_result = False

class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def __repr__(self): 
		return f"{self.name}: {self.score}"
	
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark A.", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55), Student("Mark B.", 0.70), Student("Mark C.", 0.68)]



def m_students():
	return list(filter(lambda student: student.name.startswith("M") and student.score >= 0.7, students))
	
    #return list(filter(lambda student: len(student.name) > 0 and student.name[1] == "a" , students)) 

    #return list(filter(lambda student: student.name == "Mark" and student.score >= 0.7, students)) 
print(m_students())