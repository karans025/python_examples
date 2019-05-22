students = []


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as error:
        print("Couldn't Read File due to: {0}".format(error))


def read_students(f):  #Generator Function
    for line in f:
        yield line


def double(x):
    return x * 2


double = lambda x: x * 2 # lambda function, similar functionality to the one defined above

read_file()
print(students)
