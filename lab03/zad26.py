class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)
        else:
            print("Student nie istnieje!")

    def get_grades(self, name):
        return self.students.get(name, "Student nie istnieje!")
klasa = Student()
klasa.add_student("Jan")
klasa.add_grade("Jan", 5)
klasa.add_grade("Jan", 4)
print(klasa.get_grades("Jan"))  
