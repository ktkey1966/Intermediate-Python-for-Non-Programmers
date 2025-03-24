
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("this is a name error")
    print(e)
except ZeroDivisionError:
    print("Hey, You can't divide by 0")
except Exception as e:
    print("Some other error")

class MyBaddError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise MyBaddError("Word has to have at least one letter!")
    return word.upper()

#print(upper_fun(""))

print("after")

            # Exercise: 5 Create a try and except block that catches a Error.

try:
    int("john")
except:
    print("This is not a number")
