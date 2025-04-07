#Ex 06_03 Pickling in Python KKey 04/01/2025
import pickle


class ToDo:
    def __init__(self, title, important, category = "Normal"):
        self.title = title
        self.important = important
        self.category = category
todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category="Study")]


age = 3344556677

file = open("text.txt", "wb")
pickle.dump(todos, file)
file.close()


file = open("text.txt", "rb")
new_todos = pickle.load(file)
file.close()

print(new_todos)




