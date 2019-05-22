students = []


def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase.append(student["name"].title())
    return student_titlecase


def print_student_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def add_student(name, student_id = 332): #Default Argument (student_id), will take this value, if not provided during the call
    student = {"name": name, "student_id": student_id}
    students.append(student)


def var_args(name, *args): # Use 2 blank lines in between function definitions
    print(name)
    print(args) # Variable number of arguments can be used here


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print("Couldn't Save File due to: {0}".format(error))


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as error:
        print("Couldn't Read File due to: {0}".format(error))

no = ["n", "N", "No", "no"]

read_file()
print_student_titlecase()

while True:
    prompt = input("Do you Want to add a student?(y/Y/yes/Yes/n/N/no/No) ")
    if prompt in no:
        break
    student_name = input("Enter Student Name: ")
    student_id = input("Enter Student Id: ")
    add_student(student_name, student_id)
    save_file(student_name)

var_args("Mark", "Something", "Another Argument", 12 , None, True)

var_kwargs("Mark", description = "Loves Python", feedback = None, pluralsight_subscriber =  True)
