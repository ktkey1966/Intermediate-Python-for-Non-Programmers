#Ex: 06_04 Pickle the To-Do List KKey 04/01/2025
import sys
import pickle

file_name = "todo_pickle.txt"
todos = []

#Read File
try:
    file = open(file_name, "rb")
    todos = pickle.load(file)
    file.close()
except:
    pass

print(todos)


#Add Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")



#Remove Todo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_remove = int(sys.argv[2])
        if index_to_remove > 0:
            index_to_remove -= 1
            del(todos[index_to_remove])
        else:
            print("Wrong number")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

print(todos)


#Save File
file = open(file_name, "wb")
pickle.dump(todos, file)
file.close()


#Print List
if len(todos) == 0:
    print("You have no To-Do's :)")
else:
    print("\nHere's your To-Do List:\n")
    for x in range(len(todos)):
        print(f"{x+1}. {todos[x]}", end="") #end="" removes the new line

#Print Commands
print("\n*************************\n")





    

