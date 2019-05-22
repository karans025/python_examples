integer = -2 #Anything Except 0 is Truthy
string = "something" #Anything except blank string is Truthy
# They both have something known as truthy values, calling the variables
# in if statements would work as if calling a boolean variable. ex:
if integer:
    print("Truthy Integer Value")
if string:
    print("Truthy String Value")
none_variable = None
if none_variable:
    print("This Won't Execute")
if integer == -2:
    print("This will Execute")
    print("Python doesn't need curly braces, Only Indentation is enough to block a code")
else:
    print("this Won't execute")
if integer and string:
    print("Using \"and\" in an If statement")
if integer or string:
    print("using \"or\" in an If statement")
if not integer:
    print("This Won't Execute")
if not none_variable:
    print("This will Execute (example of \"if not\")")
a = 1
b = 2
print("bigger") if a > b else print("smaller")
