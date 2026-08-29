class Student:
    # class variable
    class_year = 2024
    num_students = 0

    def __init__(self, name, age, grade):
        # instance variables
        self.name = name
        self.age = age
        self.grade = grade
        Student.num_students += 1


student1 = Student("John", 20, "A")
student2 = Student("Jane", 22, "B")
student3 = Student("Bob", 21, "C")

print(
    f"Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}, Class Year: {Student.class_year}, Total Students: {Student.num_students}"
)
