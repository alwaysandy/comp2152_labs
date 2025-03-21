from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.major = p_major

student = Student("Andy", 30, 150, "Mathematics")
print(student.name)