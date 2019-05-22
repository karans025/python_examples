from student import Student

class HighSchoolStudent(Student):

    school_name = "Springfield High School"


    def get_name_capitalize(self):
        return super().get_name_capitalize() + "-HS"
