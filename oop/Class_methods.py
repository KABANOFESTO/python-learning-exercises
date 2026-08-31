class Student:
    Counter = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.Counter += 1
        Student.total_gpa += gpa

    def display_info(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")

    @classmethod
    def get_student_count(cls):
        return f"Total number of students: {cls.Counter}"

    @classmethod
    def get_average_gpa(cls):
        if cls.Counter == 0:
            return 0.0
        return f"Average GPA of students: {cls.total_gpa / cls.Counter:.2f}"


student1 = Student("Alice", 3.5)
student2 = Student("Bob", 3.7)
student3 = Student("Charlie", 3.9)

print(Student.get_student_count())  # Returns "Total number of students: 3"
print(Student.get_average_gpa())
