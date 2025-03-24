#Exercise Challenge: Methods
#Write a method to get a student's average score.
#You're given a class named Student with a Scores property.
#Create a method named average_score that calculates the average score of a student.

show_expected_result = False

class Student:
    scores = [65,75,85,95]

    def average_score(self):
        return sum(self.scores) / len(self.scores)

student = Student()
result = student.average_score()
print(result)
